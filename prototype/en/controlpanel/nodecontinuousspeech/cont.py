import azure.cognitiveservices.speech as speechsdk
import time
import string
from websocket import create_connection
ws = create_connection("ws://localhost:6969")

ws.send("يرجى التحدث إلى الميكروفون")
#print("Sent")
#print("Receiving...")
#result =  ws.recv()
#print("Received '%s'" % result)
#ws.close()


done = False
def from_mic():
    done = False
    speech_config = speechsdk.SpeechConfig(subscription="3b64ac3f450c47079a6aeaa53c9ceff6", region="westeurope")
    speech_config.speech_recognition_language="ar-SA"
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt.result.text)))
    speech_recognizer.recognized.connect(lambda evt: ws.send(evt.result.text))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)
    
    speech_recognizer.stop_continuous_recognition()

from_mic()
ws.close()
    # </SpeechContinuousRecognitionWithFile>

    
 