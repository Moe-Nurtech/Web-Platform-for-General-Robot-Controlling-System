# -*- coding: utf-8 -*-
import wx
import time
import face
import threading
from gui import Frame
from communication import Communicator
from eye import Eye, open_camera
from tracking import Track
from cv2.dnn import readNetFromCaffe
from chatter import Chatter
from os import remove
from random import choice
from numpy import save
import motionc
import sys

save('stop', [False])
stop = False
main_running = False

ff = True

run_auto = True
com = Communicator()
ch = Chatter()

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

intro_list = ['مَرْحَبًا, أَنَا الرَّجُلُ الْآلِيُّ بُوُ سَيْفْ, كَيْفَ حَالُك ',
                  'حَيّاكُم الله,'
                  ' أَنَا الرَّجُلُ الْآلِيُّ بُوُ سَيْفْ,'
                  ' كَيْفَ حَالُك',
                  'أهلاً وَسَهلاً بِكُمْ, أَنَا الرَّجُلُ الْآلِيُّ بُوُ سَيْفْ, كَيْفَ حَالُك']
firstarg=sys.argv[1]
com.say(choice(firstarg))



firstarg=sys.argv[1]
print(firstarg)