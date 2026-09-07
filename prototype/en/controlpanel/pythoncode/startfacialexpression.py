# -*- coding: utf-8 -*-
import socket
from communication import Communicator
import time
import face
from cv2.dnn import readNetFromCaffe

#from random import choice
from numpy import save



save('stop', [False])
stop = False
main_running = False

ff = True

run_auto = True
com = Communicator()
#ch = Chatter()

proto_object = 'C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/objects.prototxt'
model_object = 'C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/objects.caffemodel'
object_net = readNetFromCaffe(proto_object, model_object)

proto_face = 'C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/face.prototxt'
model_face = 'C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/face.caffemodel'
face_net = readNetFromCaffe(proto_face, model_face)

proto_gender = 'C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/gender.prototxt'
model_gender = 'C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/gender.caffemodel'
gender_net = readNetFromCaffe(proto_gender, model_gender)

proto_age = 'C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/age.prototxt'
model_age = 'C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/age.caffemodel'
age_net = readNetFromCaffe(proto_age, model_age)




time.sleep(1)
smile = 'هَكَذَا يَبْدُو الْفَرَحْ '
#com.say(smile)
#time.sleep(2)
#face.main22smile()
#time.sleep(5)
sad = 'أَنَا هَكَذَا حَزِينْ'
#com.say(sad)
#time.sleep(2)
#face.main22sad()
#time.sleep(6)
angry = 'إنَّ الْغَضَبْ شُعُورٌ سَيّءّْ'
#com.say(angry)
#time.sleep(2)
#face.main22angry()
#time.sleep(6)


s = socket.socket()
host = "127.0.0.1"
port = 12346
s.bind((host, port))

s.listen(5)
while True:
   c, addr = s.accept()
   data = c.recv(1024)
   if data:
        if data.decode("utf-8")=="happy":
            com.say(smile)
            time.sleep(2)
            face.main22smile()
            time.sleep(5)           
        elif data.decode("utf-8")=="sad":
            com.say(sad)
            time.sleep(2)
            face.main22sad()
            time.sleep(6)            
        elif data.decode("utf-8")=="angry":
            com.say(angry)
            time.sleep(2)
            face.main22angry()
            time.sleep(6)
            
   c.close()