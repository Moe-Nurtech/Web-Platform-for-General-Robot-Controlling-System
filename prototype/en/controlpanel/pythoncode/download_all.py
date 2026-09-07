import os
from google.cloud import texttospeech
from google.oauth2 import service_account
from pydub import AudioSegment
from pathlib import Path
from glob import glob


credentials = service_account.Credentials.from_service_account_file(
    str(Path('models/i-melody-252617-c82c58c9d70c.json')))
client_t2s = texttospeech.TextToSpeechClient(credentials=credentials)


def down(texts, path):
    for i, text in enumerate(texts):
        synthesis_input = texttospeech.types.SynthesisInput(text=text)
        voice = texttospeech.types.VoiceSelectionParams(language_code='ar-AE',
                                                        ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

        audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16,
                                                      pitch=-5)

        response = client_t2s.synthesize_speech(synthesis_input, voice, audio_config)
        try:
            with open(os.path.join(os.path.dirname(__file__),
                                   path, str(i) + '.wav'), 'wb') as out:
                out.write(response.audio_content)

            voice = AudioSegment.from_wav(os.path.join(os.path.dirname(__file__),
                                                       path, str(i) + '.wav'))
            voice += 25
            voice.export(os.path.join(os.path.dirname(__file__),
                                      path, str(i) + '.wav'), "wav")
        except Exception as e:
            print(e)
            print('Couldn\'t save the text "', text, '"')


files = glob('responses/*.res')

for file in files:
    if file == 'responses':
        continue

    f = '.'.join(file.split('.')[:-1])
    print(file)
    if '\\' in f:
        fn = f.split('\\')[1]
    else:
        fn = f.split('/')[1]
    sents = list(filter(bool,
                        open(Path(file),
                             'r',
                             encoding='utf8').read().split('\n')))
    print(fn)
    os.mkdir(os.path.join(os.path.join(os.path.dirname(__file__)), 'mp3_responses', fn))
    down(sents, os.path.join('mp3_responses', fn))
