import os
from pydub import AudioSegment
from google.cloud import speech
from google.cloud import texttospeech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.oauth2 import service_account
import pyaudio
from winsound import PlaySound, SND_FILENAME
from six.moves import queue
from pathlib import Path
import face
import time
from numpy import load
from random import choice
from threading import Thread

restart = False

choice_list2 = ['أنا الخوارزمي وأَسْتَطِيعُ أَنَّ أَحَسْبُ عُمْرِكَ, مِسَاحَةَ الْأَشْكَالِ, وَكُتْلَةَ الْجِسْمِ الزَّايِدَةَ,وَ كَمِّيَّةُ الْمَاءِ الَّتِي يَحْتَاجُهَا الْجِسْمْ,بالإضافة إلى ذَلِكَ اسْتُطِيعُ عَرْضَ تَعَابِيرِ الْوَجْهْ',
               'لَدَيَ عَدَدٌ غير قليل مِنَ الْمَهَارَاتِ,يُمْكِنُنِي حِسَابُ عُمرَكْ , و يُمْكِنُنِي حِسَابُ كُتْلَةِ جِسْمُكَ الزَّائِدَةْ,',
               'يُمْكِنُنِي حِسَابُ مِسَاحَةِ الأشكال, و يُمْكِنُنِي حِسَابُ كَمِّيَّةُ الْمَاءِ الَّتِي يَحْتَاجُهَا جِسمُكْ, بالإضافة إلى ذَلِكَ اسْتُطِيعُ عَرْضَ تَعَابِيرِ الْوَجْهْ',
               ]


class MicrophoneStream(object):
    def __init__(self, rate, chunk, track):
        self.track = track
        global restart
        restart = False
        self._rate = rate
        self._chunk = chunk

        self._buff = queue.Queue()
        self.closed = True
        Thread(target=self.stop_or_not, args=()).start()
        Thread(target=self.check_inactive, args=()).start()

    def check_inactive(self):
        global restart
        s = time.time()
        while time.time() - s <= 60 * 2:
            st = time.time()
            # while self.track.face_here:
            if time.time() - st >= 60 * 2:
            #         # try:
            #         #     os.remove('incomplete')
            #         # except FileNotFoundError:
            #         #     pass
                restart = [True]
                self.closed = True
        if not self.closed:
            restart = True
            self.closed = True

    def stop_or_not(self):
        global restart
        while True:
            try:
                if load('stop.npy')[0]:
                    restart = False
                    self.closed = True
            except ValueError:
                pass

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, the_type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        self._buff.put(in_data)
        del frame_count, time_info, status_flags
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)

                except queue.Empty:
                    break

            yield b''.join(data)


class Communicator:
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(str(Path('models/My Project 46621-cef0972fe98d.json')))
        self.client_speech = speech.SpeechClient(credentials=credentials)
        self.client_t2s = texttospeech.TextToSpeechClient(credentials=credentials)

    def listen(self, track):
        global restart
        rate = 16000
        chunk = int(rate / 10)

        lang = 'ar-AE'
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=rate,
            language_code=lang)
        streaming_config = types.StreamingRecognitionConfig(
            config=config,
            interim_results=True)
        while True:

            with MicrophoneStream(rate, chunk, track) as stream:
                audio_generator = stream.generator()
                requests = (types.StreamingRecognizeRequest(audio_content=content)
                            for content in audio_generator)

                responses = self.client_speech.streaming_recognize(streaming_config, requests)

                for response in responses:

                    if not response.results:
                        continue
                    result = response.results[0]

                    if result.alternatives and result.is_final:
                        transcript = result.alternatives[0].transcript
                        print('you: ', transcript)

                        return transcript
            if restart:
                # if isinstance(restart, list):
                #     pass
                #     # self.say(choice(choice_list2))
                # else:
                self.say(choice(list(filter(bool, open(Path('responses/fill_time.res'),
                                                           'r', encoding='utf8').read().split('\n')))))

            else:
                return PermissionError

    def say(self, text):

        print('Khwarizmi:', text)
        synthesis_input = texttospeech.types.SynthesisInput(text=text)
        voice = texttospeech.types.VoiceSelectionParams(language_code='ar-AE',
                                                        ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

        audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16,
                                                      pitch=-5)

        response = self.client_t2s.synthesize_speech(synthesis_input, voice, audio_config)
        try:
            with open('speech.wav', 'wb') as out:
                out.write(response.audio_content)

            voice = AudioSegment.from_wav("speech.wav")
            voice += 25
            voice.export("speech.wav", "wav")
        except:
            pass
        path = os.path.join(os.path.dirname(__file__), 'speech.wav')
        face.duration_wav1()
        PlaySound(path, SND_FILENAME)
        try:
            os.remove('speech.wav')
        except (FileNotFoundError, PermissionError):
            pass
