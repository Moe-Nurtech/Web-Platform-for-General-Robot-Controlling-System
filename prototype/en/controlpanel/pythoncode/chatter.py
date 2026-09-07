import logging
import os
import numpy as np
import pandas as pd
from sklearn_crfsuite import CRF
import glob
from nltk.tokenize import word_tokenize
import re
from tqdm import tqdm
from datetime import datetime as dt
import pickle
import sqlite3
from random import choice, sample
import json
from math import ceil
import sys
from nltk.tag.stanford import StanfordPOSTagger
from pathlib import Path
from pint import UnitRegistry
import matplotlib.pyplot as plt
from pprint import pprint
import requests
import urllib.parse
import time
import wikipedia

wikipedia.set_lang("ar")
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
if sys.platform == 'win32':
    java_path = "C:\\Program Files\\Java\\jdk-12.0.2\\bin\\java.exe"
    os.environ['JAVAHOME'] = java_path

try:
    # import tensorflow as ft
    from tensorflow import get_default_graph
    from keras.models import load_model
    from keras.models import Model, Input
    from keras.layers import Embedding, Dense, GRU, Bidirectional
    from keras.preprocessing.text import Tokenizer
    from keras.preprocessing import sequence
    from keras.utils import to_categorical
    from keras.losses import categorical_crossentropy
    from keras.optimizers import RMSprop
except ImportError:
    raise


class Chatter:
    def __init__(self):
        self.maxlen = 25
        self.missing_ent = ''
        try:
            os.remove('incomplete')
        except FileNotFoundError:
            pass
        self.check = False
        self.glove_dimensions = 300
        self.count = 1
        self.entities_guide = json.load(open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/reference/entities_names.json'), 'r', encoding='utf8'))

        self.number_system = {
            'واحد': 1,
            'اثنان': 2,
            'ثلاثه': 3,
            'اربعه': 4,
            'خمسه': 5,
            'سته': 6,
            'سبعه': 7,
            'ثمانيه': 8,
            'تسعه': 9,
            'عشره': 10
        }

        if os.path.isfile(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/khwarizmi.h5')) and os.path.isfile(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/khwarizmi.tkn')):
            self.model = load_model(str(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/khwarizmi.h5')))
            self.tkn = pickle.load(open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/khwarizmi.tkn'), 'rb'))
            self.graph = get_default_graph()
        self.tagger = StanfordPOSTagger(str(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/arabic.tagger')),
                                        path_to_jar=str(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/stanford-postagger.jar')))
        self.required_entities = json.load(open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/reference/required_entities.json'), 'r', encoding='utf8'))
        self.required_entities_responses = json.load(open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/reference/required_entities_responses.json'),
                                                          'r', encoding='utf8'))
        self.default_value_entities = json.load(open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/reference/default_value_entities.json'),
                                                     'r', encoding='utf8'))
        chats = glob.glob(str(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/intents/*.chat')))
        self.entity_intents = {}
        self.intents = {}
        for chat in chats:
            with open(chat, 'r', encoding='utf8') as f:
                con = f.read()
                ents = list(set(re.findall(r'\[(.*?)\]', con)))
                self.intents['.'.join(os.path.split(chat)[1].split('.')[:-1])] = ents
                if ents:
                    self.entity_intents['.'.join(os.path.split(chat)[1].split('.')[:-1])] = ents

    @staticmethod
    def display_hisotry(history):
        for metric in list(history.history.keys()):
            m = history.history[metric]

            epochs = range(1, len(m) + 1)

            plt.plot(epochs, m, 'b', label='Training ' + metric.title())
            plt.title('Training ' + metric.title())
            plt.legend()

            plt.show()

    @staticmethod
    def _build_intent_model(out_len, word_index):
        input_seq = Input(shape=(None,), dtype='int32', name='text')
        embed_text = Embedding(len(word_index), 100, name='embed')(input_seq)
        seq_layers = Bidirectional(GRU(32))(embed_text)

        out = Dense(out_len, activation='softmax')(seq_layers)

        model = Model(input_seq, out)

        return model

    @staticmethod
    def decontracted(phrase):
        phrase = re.sub(r"أ", "ا", phrase)
        phrase = re.sub(r"إ", "ا", phrase)
        phrase = re.sub(r"ة", "ه", phrase)
        return phrase

    def _setup_intents(self):
        chats_csv = []
        chats = list(self.intents.keys())
        for intent in chats:
            chat = Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/intents/' + intent + '.chat')
            intent_name = str('.'.join(os.path.split(chat)[1].split('.')[:-1]))
            with open(chat, 'r', encoding='utf8') as of:
                content = of.read()
                convs = content.split('\n')
                convs = list(filter(bool, convs))

                entities_names = self.intents[intent]
                if not entities_names:
                    for conv in convs:
                        chats_csv.append([intent_name, self.decontracted(conv)])
                    continue
                entities = []
                for entity_alias in entities_names:
                    entity_name = self.entities_guide.get(entity_alias)
                    if entity_name == 'num':
                        vals = [str(k) for k in range(500)]
                    elif entity_name == 'year':
                        vals = [str(k) for k in range(1000, 2500)]
                    else:
                        vals = []
                        ent_vals = list(map(
                            lambda z: z.split(','),
                            list(filter(bool,
                                        open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/entities/'
                                                  + entity_name + '.ent'), 'r', encoding='utf8').read().split('\n')))))
                        for v in ent_vals:
                            vals += v
                        if len(vals) > 500:
                            vals = sample(vals, 500)
                    entities.append([vals, entity_alias])
                entities.sort(key=lambda x: len(x[0]), reverse=True)
                final_convs = []
                for i, (entity_vals, entity_name) in enumerate(entities):
                    new_convs = []
                    if i == 0:
                        if len(convs) <= len(entity_vals):
                            convs = (convs * ceil((len(entity_vals) / len(convs))))[:len(entity_vals)]
                        else:
                            entity_vals = (entity_vals * ceil(len(convs) / len(entity_vals)))[:len(convs)]
                        if len(entities) != i + 1:
                            for (val, conv) in zip(entity_vals, convs):
                                new_convs.append(conv.replace('[' + entity_name + ']', str(val)))
                            convs = new_convs.copy()
                        else:
                            for conv, val in zip(convs, entity_vals):
                                new_conv = conv.replace('[' + entity_name + ']', str(val))
                                if new_conv:
                                    final_convs.append(conv.replace('[' + entity_name + ']', str(val)) + '\n')
                    else:
                        if len(convs) <= len(entity_vals):
                            convs = (convs * ceil((len(convs) / len(entity_vals) ** -1)))[:len(entity_vals)]
                        else:
                            entity_vals = (entity_vals * ceil(len(convs) / len(entity_vals)))[:len(convs)]
                        if len(entities) != i + 1:
                            for conv, val in zip(convs, entity_vals):
                                new_convs.append(conv.replace('[' + entity_name + ']', str(val)))
                            convs = new_convs.copy()
                        else:
                            for conv, val in zip(convs, entity_vals):
                                new_conv = conv.replace('[' + entity_name + ']', str(val))
                                if new_conv:
                                    final_convs.append(conv.replace('[' + entity_name + ']', str(val)) + '\n')
                final_convs = list(map(lambda z: z.replace('\n', ''), final_convs))

                for final_conv in final_convs:
                    chats_csv.append([intent_name, self.decontracted(final_conv)])
        return chats_csv

    def train_intents(self):
        chats = self._setup_intents()

        df = pd.DataFrame(chats, columns=['intent', 'conv']).sample(frac=1).reset_index(drop=True)
        df['id'] = df['intent'].factorize()[0]
        id_df = df[['intent', 'id']].sort_values('id')
        id_to_intent = dict(id_df[['id', 'intent']].values)

        convs = df['conv']
        labels = np.array(df['id'])

        filters = '!"#$%&(),.:;<=>?@[\\]^_`{|}~\t\n"\'،><؛×÷`ًٌٍَُِ][ـ:"؟.,ْ~'

        tokenizer = Tokenizer(filters=filters, oov_token='', num_words=2953)
        tokenizer.fit_on_texts(convs)
        sequences = tokenizer.texts_to_sequences(convs)
        word_index = tokenizer.word_index

        x = sequence.pad_sequences(sequences, maxlen=self.maxlen, padding='post', truncating='post')
        labels = np.asarray(labels)
        y = to_categorical(labels)

        indices = np.arange(x.shape[0])
        np.random.shuffle(indices)
        x = x[indices]
        y = y[indices]

        model = self._build_intent_model(len(set(labels)), word_index)
        model.compile(optimizer=RMSprop(lr=1e-4), loss=categorical_crossentropy, metrics=['acc'])

        print('Training Khwarizmi Intent Classification Model')
        his = model.fit(x, y, epochs=320, batch_size=32)
        self.display_hisotry(his)
        model.save(str(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/khwarizmi.h5')))
        pickle.dump(tokenizer, open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/khwarizmi.tkn'), 'wb'))
        self.model = model
        self.tkn = tokenizer
        if os.path.isfile(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/reference/khwarizmi.db')):
            os.remove(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/reference/khwarizmi.db'))
        con = sqlite3.connect(str(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/reference/khwarizmi.db')))
        c = con.cursor()
        c.execute(
            'CREATE TABLE `intents` ( `ID` INTEGER NOT NULL UNIQUE, `Intent` TEXT NOT NULL UNIQUE, PRIMARY KEY(`ID`) )')
        con.commit()
        for _id in id_to_intent.keys():
            c.execute('INSERT INTO intents VALUES(?, ?)', (str(_id), id_to_intent.get(_id)))
            con.commit()

    def predict_intent(self, sent):

        seq = self.tkn.texts_to_sequences([sent])
        x = sequence.pad_sequences(seq, maxlen=self.maxlen, padding='post', truncating='post')
        try:
            with self.graph.as_default():
                intent_predict = self.model.predict(x)[0]

            intent_id = np.argmax(intent_predict)
            intent_con = sqlite3.connect(str(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/reference/khwarizmi.db')))
            intent_cursor = intent_con.cursor()
            intent_cursor.execute('SELECT Intent FROM intents WHERE ID = ' + str(intent_id))
            intent = intent_cursor.fetchone()[0]

            return intent, max(intent_predict)
        except AttributeError:
            pass

    @staticmethod
    def _word2features(sent, word_num):
        word = sent[word_num][0]
        postag = sent[word_num][1]

        features = {
            'bias': 1.0,
            'word.lower()': word.lower(),
            'word[-3:]': word[-3:],
            'word[-2:]': word[-2:],
            'word.isupper()': word.isupper(),
            'word.istitle()': word.istitle(),
            'word.isdigit()': word.isdigit(),
            'postag': postag,
            'postag[:2]': postag[:2],
        }
        if word_num > 0:
            word1 = sent[word_num - 1][0]
            postag1 = sent[word_num - 1][1]
            features.update({
                '-1:word.lower()': word1.lower(),
                '-1:word.istitle()': word1.istitle(),
                '-1:word.isupper()': word1.isupper(),
                '-1:postag': postag1,
                '-1:postag[:2]': postag1[:2],
            })
        else:
            features['BOS'] = True

        if word_num < len(sent) - 1:
            word1 = sent[word_num + 1][0]
            postag1 = sent[word_num + 1][1]
            features.update({
                '+1:word.lower()': word1.lower(),
                '+1:word.istitle()': word1.istitle(),
                '+1:word.isupper()': word1.isupper(),
                '+1:postag': postag1,
                '+1:postag[:2]': postag1[:2],
            })
        else:
            features['EOS'] = True

        return features

    @staticmethod
    def _letters2num(sent):
        final_sent = ''
        for i in sent:
            if i != ' ':
                final_sent += str(ord(i)) + ';'
            else:
                final_sent += ' '
        return final_sent

    @staticmethod
    def _num2letters(word):
        final_word = []
        for let in word.split(';'):
            if let:
                final_word += chr(int(let))
        return final_word

    def _setup_entities(self, chat):
        all_possible = False
        content = open(chat, 'r', encoding='utf8').read()
        convs = list(filter(bool, content.split('\n')))
        entities_names = self.intents['.'.join(os.path.split(chat)[1].split('.')[:-1])]

        entities = []

        for entity_name in entities_names:
            if self.entities_guide[entity_name] == 'num':
                ent_vals = []
            elif self.entities_guide[entity_name] == 'year':
                ent_vals = [str(i) for i in range(1900, 2050)]
            else:
                ent_values = [val.split(',')
                              for val in list(filter(bool,
                                                     open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/entities/' +
                                                          self.entities_guide[entity_name] +
                                                          '.ent'), 'r', encoding='utf8').read().split('\n')))]
                ent_vals = []
                if len(ent_values) > 1500:
                    all_possible = True
                    ent_values = sample(ent_values, 1500)
                for ent_val in ent_values:
                    for val in ent_val:
                        ent_vals.append(val)
            entities.append([ent_vals, entity_name])
        entities.sort(key=lambda x: len(x[0]), reverse=True)
        for i, entity in enumerate(entities):
            ent_convs = []
            convs_copy = convs.copy()
            for conv in tqdm(convs):
                if ('[' + entity[1] + ']') in conv:
                    ent_convs.append(conv)
                    convs_copy.remove(conv)
            if len(entity[0]) >= len(ent_convs):
                ent_convs = (ent_convs * ceil(len(entity[0]) / len(ent_convs)))[:len(entity[0])]
            else:
                if entity[0]:
                    entities[i][0] = (entity[0] * ceil(len(ent_convs) / len(entity[0])))[:len(ent_convs)]
                else:
                    entities[i][0] = list(map(str, list(range(len(ent_convs)))))
            convs = ent_convs + convs_copy

        for i, enti in enumerate(entities):
            count = len([s for s in convs if '[' + enti[1] + ']' in s])
            if count > len(enti[0]):
                entities[i][0] = (enti[0] * ceil(count / len(enti[0])))[:count]

        ents = {}
        for entity in entities:
            ents[entity[1]] = entity[0]

        sents = []
        y = []
        for num, conv in tqdm(enumerate(convs)):
            aval_entities = []
            for entity in ents.keys():
                if ('[' + entity + ']') in conv:
                    aval_entities.append(entity)
            aval_entities = dict.fromkeys(aval_entities, '')
            for aval_ent in aval_entities.keys():
                if aval_ent:
                    new_ent = choice(ents[aval_ent])
                    if isinstance(aval_ent, str):
                        conv = conv.replace('[' + aval_ent + ']', new_ent)
                    else:
                        return [ValueError, chat, aval_ent]
                    aval_entities[aval_ent] = new_ent
                    ents[aval_ent].remove(new_ent)
            tokens = word_tokenize(conv)
            y_sam = list(map(str, list(np.zeros(len(tokens), dtype=int))))
            for aval_entity in aval_entities.keys():
                entity = aval_entities[aval_entity]
                if entity:
                    try:
                        ent_tokens = word_tokenize(entity)
                        ent1_index = tokens.index(ent_tokens[0])
                        y_sam[ent1_index] = 'B-' + aval_entity
                    except ValueError:
                        print(entity)
                        print(tokens)
                        sys.exit()
                    for i, ent_token in enumerate(ent_tokens):
                        if i != 0:
                            y_sam[ent1_index + i] = 'I-' + aval_entity
            tags = []
            for i, t in enumerate(self.tagger.tag(tokens)):
                t = t[1].split('/')
                if len(t) == 1:
                    tags.append([tokens[i], t[0]])
                else:
                    tags.append(t)
            sents.append(tags)
            y.append(y_sam)

        sents_copy = sents.copy()
        sents = []
        for sent in sents_copy:
            sents.append(list(map(lambda z: (self._letters2num(z[0]), z[1]), sent)))
        data = [[self._word2features(sent, i) for i in range(len(sent))] for sent in sents]
        y_copy = y.copy()
        y = []
        for y_val in y_copy:
            y.append(list(map(lambda z: self._letters2num(z), y_val)))
        return [data, y, all_possible]

    def train_entities(self):
        for intent in self.entity_intents.keys():
            print('Processing', intent)
            chat = Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/intents/' + intent + '.chat')
            data = self._setup_entities(chat)
            if data[0] == ValueError:
                print(data[1], '\t', data[2], type(data[2]))
                ValueError('Unknown type of the entity name')
            x = data[0] * 2
            y = data[1] * 2

            print('Training ' + intent.title())
            crf = CRF(algorithm='lbfgs', c1=0.1, c2=0.1, all_possible_states=data[2])
            try:
                crf.fit(x, y)
            except Exception as e:
                print(intent.title())
                raise e
            pickle.dump(crf, open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/' + intent + '.sav'), 'wb'))
            print(intent.title(), 'Entity Extraction Training Finished')

    def predict_entities(self, sent: str, intent):
        tokens = word_tokenize(sent)
        tags = []
        for i, t in enumerate(self.tagger.tag(tokens)):
            t = t[1].split('/')
            if len(t) == 1:
                tags.append([tokens[i], t[0]])
            else:
                tags.append(t)
        tags = list(map(lambda z: (self._letters2num(z[0]), z[1]), tags))
        x = [self._word2features(tags, i) for i in range(len(tags))]
        crf = pickle.load(open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/' + intent + '.sav'), 'rb'))
        entities_list = crf.predict_single(x)
        entities_list = list(map(lambda z: ''.join(self._num2letters(z)), entities_list))
        entities = self.intents[intent]
        aval_entities = {}
        for entity in entities:
            tokens_count = len([i for i in entities_list if entity in i])
            if tokens_count == 0:
                aval_entities[entity] = None
                continue
            try:
                word1_index = entities_list.index('B-' + entity)
                all_entity = []
            except ValueError:
                pass
            for i in range(tokens_count):
                try:

                    all_entity.append(tokens[word1_index + i])
                except UnboundLocalError:
                    pass
            aval_entities[entity] = ' '.join(all_entity)
        return aval_entities

    def _resynonem(self, entity_name, entity_val, first=False):
        name = self.entities_guide[entity_name]

        if entity_val is None:
            return None
        if name == 'any':
            return entity_val
        elif name == 'num':
            if entity_val == first:
                try:
                    os.remove('incomplete')
                except FileNotFoundError:
                    pass
                return [None, False]

            try:
                return float(entity_val)
            except ValueError:
                val = self.number_system.get(entity_val)
                if val is None:
                    vals = entity_val.split(' ')
                    for v in vals:
                        if v.isdigit():
                            return float(v)
                        elif v in list(self.number_system.keys()):
                            return self.number_system.get(v)
                    return None
                else:
                    return val
        elif name == 'year':
            try:
                return int(entity_val)
            except ValueError:
                return None
        elif name == 'date-time':
            return entity_val
        else:
            entity_values = list(map(lambda x: x.split(','),
                                     open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/entities/' + name + '.ent'), 'r', encoding='utf8').read().split('\n')))
            values = [i for i in entity_values if entity_val.strip() in i]
            if values:
                if values[0][0].isdigit():
                    return int(values[0][0])
                else:
                    return values[0][0].title()
            else:
                return None

    def _solve_incomplete(self, details):
        try:
            os.remove('incomplete')
        except FileNotFoundError:
            pass
        if not details['intent'] in self.required_entities.keys():
            return details
        for ent in self.required_entities[details['intent']]:
            if ent not in details['entities']:
                open('incomplete', 'w').close()
                self.incomplete_data = details
                self.missing_ent = ent
                return {'intent': 'incomplete', 'res': self.required_entities_responses.get(ent)}
        else:
            return details

    def _find_incomplete(self, req):
        dont_complete = ['انقل على غيره',
                         'خلاص',
                         'خلص',
                         'اغلق',
                         'اطفي' ,
                         'الغاء']
        if req.strip() in dont_complete:
            try:
                os.remove('incomplete')
            except FileNotFoundError:
                pass
            return {'intent': 'None', 'res': 'هل يمكنني القيام بشيء آخر من أجلك؟'}
        final_ent = self._resynonem(self.missing_ent, req)
        if isinstance(final_ent, list):
            final_ent = final_ent[1]
        if final_ent is None:

            if self.count < 3:
                self.count += 1
                print(self.count)
                return {'intent': 'incomplete', 'res': self.required_entities_responses.get(self.missing_ent)}
            else:
                self.count = 1
                try:
                    os.remove('incomplete')
                except FileNotFoundError:
                    pass
                return self.response(req)

        else:

            self.incomplete_data['entities'][self.missing_ent] = final_ent
            return self._solve_incomplete(self.incomplete_data)

    def search1(self,words):
        subscription_key = "f9a3c46abe6d4b499a94f0fb9ac2e143"
        endpoint = search_url = "https://api.labs.cognitive.microsoft.com/answersearch/v7.0/search"

        # Entity you want to find
        query = words

        # Construct the request
        mkt = 'en-US'
        params = 'mkt=' + mkt + '&q=' + urllib.parse.quote(query) + '&count=1&offset=0&safesearch=Moderate'
        headers = {'Ocp-Apim-Subscription-Key': subscription_key}

        # Call the API
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()

            # print("\nHeaders:\n")
            # print(response.headers)

            print("\nAnswer:\n")
            json1 = response.json()
            # pprint(json1)
            return (json1['webPages']['value'][0]['snippet'])
        except Exception as ex:
            raise ex

    def search(self, words):
        try:
             return wikipedia.summary(words,1)
        except Exception as ex:
            return choice(list(filter(bool, open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/responses/default_fallback.res'),
                                           'r', encoding='utf8').read().split('\n'))))

    def process(self, data):
        choice_listage= ['يُمْكِنُنِي حِسَابُ كُتْلَةِ جِسْمُكَ الزَّائِدَةْ','يُمْكِنُنِي حِسَابُ مِسَاحَةِ الأشكال','يُمْكِنُنِي حِسَابُ كَمِّيَّةُ الْمَاءِ الَّتِي يَحْتَاجُهَا جِسمُكْ','اسْتُطِيعُ عَرْضَ تَعَابِيرِ الْوَجْهْ']
        choice_listbmi = ['يُمْكِنُنِي حِسَابُ عُمرَكْ','يُمْكِنُنِي حِسَابُ مِسَاحَةِ الأشكال','يُمْكِنُنِي حِسَابُ كَمِّيَّةُ الْمَاءِ الَّتِي يَحْتَاجُهَا جِسمُكْ','اسْتُطِيعُ عَرْضَ تَعَابِيرِ الْوَجْهْ']
        choice_listwater = ['يُمْكِنُنِي حِسَابُ عُمرَكْ', 'يُمْكِنُنِي حِسَابُ كُتْلَةِ جِسْمُكَ الزَّائِدَةْ','يُمْكِنُنِي حِسَابُ مِسَاحَةِ الأشكال','اسْتُطِيعُ عَرْضَ تَعَابِيرِ الْوَجْهْ']
        choice_listshape = ['يُمْكِنُنِي حِسَابُ عُمرَكْ', 'يُمْكِنُنِي حِسَابُ كُتْلَةِ جِسْمُكَ الزَّائِدَةْ','يُمْكِنُنِي حِسَابُ كَمِّيَّةُ الْمَاءِ الَّتِي يَحْتَاجُهَا جِسمُكْ','اسْتُطِيعُ عَرْضَ تَعَابِيرِ الْوَجْهْ']
        if data['intent'] == 'age':
            res = [self.get_age(data['entities']), choice(choice_listage)]
        elif data['intent'] == 'bmi':
            res = self.get_bmi(data['entities'])
        elif data['intent'] == 'water_intake':
            res = [self.water_intake(data['entities']), choice(choice_listwater)]
        elif 'shapes' in data['intent']:
            res = [self.shapes(data), choice(choice_listshape)]
        elif data['intent'] == 'area':
            return self._solve_incomplete({'intent': 'shapes.' + data['entities']['shapes'].lower(), 'entities': {}})
        else:
            return data

        return {'intent': data['intent'], 'res': res}

    @staticmethod
    def get_bmi(ents):

        u = UnitRegistry()
        l_u = getattr(u, ents['l_unit'].lower())
        m_u = getattr(u, ents['m_unit'].lower())

        le = ents['height'] * l_u
        length = le.to(u.m).m

        ma = ents['weight'] * m_u
        weight = ma.to(u.kg).m

        bmi = weight / (length ** 2)
        mes = 'كُتْلَةُ جِسْمِكَ هي {bmi} وَهَذَا يَعْنِي أَنَّ {des}'

        if bmi < 18.5:
            mes = mes.format(bmi=round(bmi, 2), des=' وَزْنُكَ أَقَلُ مِنْ الطَّبِيعِيِّ')
            advice = '"لِزِيَادَةِ وَزْنِكَ, عَلَيْكَ بِتَنَاوُلِ أَطْعِمَةٍ تَحْتَوِي عَلَى سِعراتٍ حَرَارِيَّةٍ أَكْثَر و تَنَاوُلُ كَمِيَّةٍ كَبِيرَةٍ فِي وَجْبَةِ الْعَشَاءِ .'
            return [mes, advice]
        elif 25 >= bmi >= 18.5:
            mes = mes.format(bmi=round(bmi, 2), des='وَزْنُكَ طَبِيعِيْ')
            return mes
        elif 30 >= bmi > 25:
            mes = mes.format(bmi=round(bmi, 2), des='وَزْنُكَ أَكْثَرْ مِنَ الطَّبِيعِيْ')
            advice = "لإنقاصِ وَزْنِكَ عَلَيْكَ بِتَبْكيرِ وَجْبَةِ الْعَشَاءِ و مُمَارَسَةِ الرِّيَاضَةِ صَباحاً أَو مَساءً."
            return [mes, advice]
        else:
            mes = mes.format(bmi=round(bmi, 2), des='لَدَيْكَ سُّمْنَة.')
            advice = "لإنقاصِ وَزْنِكَ عَلَيْكَ بِتَبْكيرِ وَجْبَةِ الْعَشَاءِ و مُمَارَسَةِ الرِّيَاضَةِ صَباحاً أَو مَساءً."
            return [mes, advice]

    def get_age(self, ents):
        if not 1800 < ents['year'] <= dt.now().year:
            open('incomplete', 'w').close()
            self.missing_ent = 'year'
            return 'آسِفْ لَكِنَّ السَنَةَ اللتي حَدَّدتَها غَيْر مَنْطِقِيَّة'

        elif not 1 <= ents['month'] <= 12:
            open('incomplete', 'w').close()
            self.missing_ent = 'month'
            return 'آسِفْ لَكِنَّ الشَهْرَ اللذي حَدَّدْتَهُ غَيْرَ مَنْطِقِي'
        elif not 1 <= ents['day'] <= 31:
            open('incomplete', 'w').close()
            self.missing_ent = 'day'
            return 'آسِفْ لَكِنَّ اليَومَ اللذي حَدَّدْتَهُ غَيْرَ مَنْطِقِي'
        try:
            birth = dt(ents['year'], ents['month'], ents['day'])
        except ValueError:
            return 'آسِفْ لَكِنَّ اليَومَ اللذي قُلْتَهُ لَيْسَ في الشَّهْرَ الَّذِي حَدَّدتَّهُ. قُمْ بِالسُّؤالِ مَرَّةً أُخْرى'

        today = dt(dt.now().year, dt.now().month, dt.now().day)
        age = today - birth
        if age.days < 0:
            return 'التَّارِيخُ الَّذِي حَدَّدْتَّهُ سَابِقٌ لِأَوَانِهِ'
        years = dt.now().year - ents['year']
        months = dt.now().month - ents['month']
        days = dt.now().day - ents['day']

        if months < 0:
            years -= 1
            months += 12
        if days < 0:
            days += 31
            if dt.now().month > ents['month']:
                if 2 in range(ents['month'], dt.now().month):
                    months -= 1
            elif dt.now().month < ents['month']:
                if 2 in list(range(dt.now().month, 13)) + list(range(1, ents['month'] + 1)):
                    months -= 1

        if years == 1:
            years = ''
            y_s = ' سَنَة'
        elif years == 2:
            years = ''
            y_s = 'سِنتين'
        elif years in range(3, 11):
            y_s = 'سَنوات'
        else:
            y_s = 'سَنَة'

        if months == 1:
            months = ''
            m_s = 'شَهرٍ'
        elif months == 2:
            months = ''
            m_s = 'شَهرينِ'
        elif months in range(3, 11):
            m_s = 'شُهورْ'
        else:
            m_s = 'شَهرٍ'

        if days == 1:
            days = ''
            d_s = 'يَومْ'
        elif days == 2:
            days = ''
            d_s = 'يَومينْ'
        elif days in range(3, 11):
            d_s = 'أَيامْ'
        else:
            d_s = 'يَومْ'

        if days == 0 and months == 0:
            return 'يَوْمَ مِيلَاَدٍ سَعِيدْ الْيَوْمَ أَصْبَحَ عُمْرُكَ {year} {y_s}'.format(year=years, y_s=y_s)

        return 'عُمْرُكَ هُوَ {year} {y_s}, و {month} {m_s}, و {day} {d_s}'.format(day=days, d_s=d_s,
                                                                         month=months, m_s=m_s,
                                                                         year=years, y_s=y_s)

    @staticmethod
    def water_intake(ents):
        u = UnitRegistry()
        m_u = getattr(u, ents['m_unit'].lower())

        ma = ents['weight'] * m_u
        weight = ma.to(u.kg).m

        minutes = ents['t_minutes']

        liters = (weight / 30) + (minutes / 30) * .35
        return 'اعْتِمَادًا عَلَى وَزنِك والمُدَّةَ التي تَسْتَغْرِقُها يَوْمِيًّا في التمرينْ, فإنك تحتاج إلى {}  لِترْ من الماءْ'.format(int(liters))

    @staticmethod
    def shapes(data):
        #  self.missing_ent = 'shapes'
        shape_type = data['intent'].split('.')[-1]
        ents = data['entities']
        if shape_type == 'triangle':
            area = .5 * ents['b_t'] * ents['h_t']
            return 'مساحة المثلث هي {area}'.format(area=area)
        elif shape_type == 'square':
            area = ents['s_s'] ** 2
            return 'مساحة الْمُرَبَّع هي {area}'.format(area=area)
        elif shape_type == 'rectangle':
            area = ents['s1'] * ents['s2']
            return 'مساحة المستطيل هي {area}'.format(area=area)
        elif shape_type == 'circle':
            area = np.pi * (ents['r'] ** 2)
            return 'مساحة الدائرة هي {area}'.format(area=area)
        elif shape_type == 'trapezoid':
            area = (ents['a'] + ents['b']) * ents['h'] * .5
            return 'مساحة شِبْهِ الْمُنْحَرِفْ هي {area}'.format(area=area)
        elif shape_type == 'parallelogram':
            area = ents['bb'] * ents['hh']
            return 'مساحة متوازي الأضلاع هي {area}'.format(area=area)

    def response(self, req):
        print(req)
        try:
            if os.path.isfile('incomplete'):
                res = self._find_incomplete(req)
                if os.path.isfile('incomplete'):
                    return res
                else:
                    return self.process(res)
            intent, proba = self.predict_intent(req)
            print(intent, proba)
            if proba <= 0.45:
                if os.path.isfile('unknown_convs.chat'):
                    with open('unknown_convs.chat', 'a+', encoding='utf8') as f:
                        f.write(req + '\n')
                else:
                    with open('unknown_convs.chat', 'w', encoding='utf8') as f:
                        f.write(req + '\n')
                #return {'intent': 'default fullback',
                       # 'res': choice(list(filter(bool, open(Path('responses/default_fallback.res'),
                                          # 'r', encoding='utf8').read().split('\n'))))}
                return {'intent': 'default fullback',
                        'res': self.search(req) }
            if intent not in self.entity_intents.keys():
                try:
                    return {'intent': intent,
                            'res': choice(list(filter(bool, open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/responses/' + intent + '.res'),
                                               'r', encoding='utf8').read().split('\n'))))}
                except FileNotFoundError:
                    return {'intent': intent}

            req_details = {'intent': intent}
            entities = self.predict_entities(req, intent)
            print(entities)
            final_entities = {}
            for entity in entities.keys():
                final_entity = self._resynonem(entity, entities[entity], first=req)
                if final_entity == [None, False]:
                    return {'intent': 'default fullback',
                            'res': choice(list(filter(bool, open(Path('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/responses/default_fallback.res'),
                                                                 'r', encoding='utf8').read().split('\n'))))}
                if final_entity is None:

                    continue
                elif isinstance(final_entity, list):

                    final_entities[entity] = final_entity[1]
                    req_details['intent'] = final_entity[0]
                else:
                    final_entities[entity] = final_entity

            for ent in self.default_value_entities.keys():
                if ent in entities.keys() and ent not in final_entities.keys():

                    final_entities[ent] = self.default_value_entities[ent]

            req_details.update({'entities': final_entities})
            res = self._solve_incomplete(req_details)
            if os.path.isfile('incomplete'):
                return res
            else:

                return self.process(res)
        except AttributeError:
            pass