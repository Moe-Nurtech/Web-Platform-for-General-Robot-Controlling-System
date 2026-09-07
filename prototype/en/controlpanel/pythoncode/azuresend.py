import azure.cognitiveservices.speech as speechsdk
import socket

def from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="3b64ac3f450c47079a6aeaa53c9ceff6", region="westeurope")
    speech_config.speech_recognition_language="ar-SA"
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    #result = speech_recognizer.recognize_once()
    print(result.text)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# Connect to the server
    clientSocket.connect(("127.0.0.1",12347));
# Send data to server
#data = "السلام عليكم";
    clientSocket.send(result.text.encode());

from_mic()