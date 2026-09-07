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


class MyFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    def Run_Robot(self, event):
        global ff
        thread100 = threading.Thread(target=main_func, args=(ff,))
        thread100.setDaemon(True)
        thread100.start()
        ff = False
        event.Skip()

    def ManualAnswer(self, event):
        save('stop', [True])
        global stop
        global main_running
        stop = True
        main_running = False
        event.Skip()

    def VedioTracking(self, event):

        thread1 = threading.Thread(target=open_camera)
        thread1.setDaemon(True)
        thread1.start()

        event.Skip()

    def FacialExpression(self, event):
        face.main22smile()
        time.sleep(8)

        face.main22sad()
        time.sleep(8)

        face.main22angry()
        time.sleep(8)

        face.main22surprise()
        time.sleep(8)

        face.main22fear()
        time.sleep(8)

        face.main22disgust()
        time.sleep(8)

        event.Skip()

    def OnTextEnter(self, event):
        global stop
        global main_running
        global run_auto
        MotionList=[motionc.MotionThread1,motionc.MotionThread2,motionc.MotionThread3]
        stop = True
        save('stop', [True])

        text1 = self.m_textCtrl3.GetValue()
        print(text1)

        com.say(text1)
        choice(MotionList)()

        if main_running:
            thread190 = threading.Thread(target=lambda: main_func(False))
            thread190.setDaemon(True)
            thread190.start()
        else:
            pass

        event.Skip()

    def MoveRight(self, event):
        head_motion_l_r = self.m_slider2.GetValue()

        if head_motion_l_r == 2:
            face.leftSlid()
        if head_motion_l_r == 1:
            face.centerSlid()
        if head_motion_l_r == 0:
            face.rightSlid()
        event.Skip()

    def MoveLeft(self, event):
        face.leftSlid()
        event.Skip()

    def onChoice(self, event):
        global stop
        global main_running

        MotionList=[motionc.MotionThread1,motionc.MotionThread2,motionc.MotionThread3]

        stop = True
        save('stop', [True])
        text1 = self.m_choice1.GetSelection()
        text2 = self.m_choice1.GetString(text1)
        print(text2)

        com.say(text2)
        choice(MotionList)()
        if main_running:
            thread180 = threading.Thread(target=lambda: main_func(False))
            thread180.setDaemon(True)
            thread180.start()
        else:
            event.Skip()
            return

        event.Skip()

    def list_choice(self, event):
        global stop
        global main_running
        global run_auto
        MotionList=[motionc.MotionThread1,motionc.MotionThread2,motionc.MotionThread3]

        run_auto = False
        stop = True
        save('stop', [True])
        text1 = self.m_listBox2.GetSelection()
        text2 = self.m_listBox2.GetString(text1)
        print(text2)
        print(run_auto)

        com.say(text2)
        choice(MotionList)()
        run_auto = True

        if main_running:

            thread1 = threading.Thread(target=lambda: main_func(False))
            thread1.setDaemon(True)
            thread1.start()
        else:
            event.Skip()
            return
        event.Skip()

    def list_choice2(self, event):
        global stop
        global main_running
        global run_auto
        MotionList=[motionc.MotionThread1, motionc.MotionThread2, motionc.MotionThread3]

        run_auto = False
        stop = True
        save('stop', [True])
        text1 = self.m_listBox3.GetSelection()
        text2 = self.m_listBox3.GetString(text1)
        print(text2)
        print(run_auto)

        com.say(text2)
        choice(MotionList)()
        run_auto = True

        if main_running:

            thread1 = threading.Thread(target=lambda: main_func(False)).start()
            thread1.setDaemon(True)
            thread1.start()
        else:
            event.Skip()
            return
        event.Skip()
    def Train_button(self, event):
        ch.train_intents()
        ch.train_entities()
        event.Skip()

    def Dont_complete(self, event):
        try:
            remove('incomplete')
        except FileNotFoundError:
            pass
        event.Skip()


class MyApp(wx.App):
    frame = None

    def OnInit(self):
        self.frame = MyFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        print("wxApp created.")
        return True


def process(respones):
    global run_auto
    # MotionList = [ motionc.MotionThread1, motionc.MotionThread3]
    # MotionList1 = [motionc.MotionThread2]
    try:
        if respones['intent'] == 'feeling':
            open('stop_blink', 'w').close()

            okay = 'حَسّناً '



            com.say(okay)
            # choice(MotionList)()
            time.sleep(1)
            smile = 'هَكَذَا يَبْدُو الْفَرَحْ '


            com.say(smile)
            # choice(MotionList)()

            time.sleep(2)
            face.main22smile()
            time.sleep(5)
            sad = 'أَنَا هَكَذَا حَزِينْ'


            com.say(sad)
            # choice(MotionList)()

            time.sleep(2)
            face.main22sad()
            time.sleep(6)
            angry = 'إنَّ الْغَضَبْ شُعُورٌ سَيّءّْ'

            com.say(angry)
            # choice(MotionList)()

            time.sleep(2)
            face.main22angry()
            time.sleep(6)

            remove('stop_blink')

        elif respones['intent'] == 'agent.acquaintance':
            res = respones['res']
            com.say(res)
            # choice(MotionList)()

        elif respones['intent'] == 'greetings.bye':
            res = respones['res']
            com.say(res)
            # choice(MotionList1)()

            # raise KeyboardInterrupt
        elif respones['intent'] == 'salam':
            res = respones['res']
            com.say(res)
            # choice(MotionList)()
            # face.hand_shake()
            # time.sleep(1)
        elif respones['intent'] == 'greetings.hello':
            res = respones['res']

            com.say(res)
            # choice(MotionList)()
            # face.main22smile()

        # elif respones['intent'] == 'area':
        #     res = respones['res']
        #     choice(speak_motion)
        #     com.say(res)

        elif 'greeting' in respones['intent']:
            res = respones['res']

            com.say(res)
            # choice(MotionList)()

        else:
            print(respones)
            res = respones['res']
            intent = respones['intent']
            if not isinstance(res, list):

                if not intent == 'default fullback':

                    com.say(res)
                    # choice(MotionList)()

                    return

                print(intent)
                print('unknown')
                # time.sleep(5)
                run_auto = False
                if not run_auto:

                    com.say(res)
                    # choice(MotionList)()
                    run_auto = True

                else:
                    pass

            else:
                for r in res:
                    com.say(r)
                    # choice(MotionList)()
    except TypeError:
        pass

def tracker_():
    #pass
    eye = Eye().start()
    track = Track(eye, face_net).start()


def main():
    global track
    global stop
    stop = False
    save('stop', [False])

    while not stop:
        try:

            req = com.listen(track)
            # req = input('You: ')
            if req == '':
                continue
            # if req is PermissionError:
            #     print('Manually Ended')
            #     break
            # if req and not track.face_here:
            #     com.say('قِفْ أمَاميّ وَأَنْتَ تَتَحَدَّثْ, من فضلك!')
            #     continue
            res_data = ch.response(req)
            process(res_data)
        except KeyboardInterrupt:
            print('restart......')
            break


def main_func(first_run):
    global stop
    global main_running
    # MotionList = [motionc.MotionThread1, motionc.MotionThread2, motionc.MotionThread3]

    stop = True
    save('stop', [True])
    time.sleep(1)
    stop = False
    save('stop', [False])

    main_running = True
    # face.blinking_thread()
    face.blinking_thread1()

    intro_list = ['مَرْحَبًا, أَنَا الرَّجُلُ الْآلِيُّ بُوُ سَيْفْ, كَيْفَ حَالُك ',
                  'حَيّاكُم الله,'
                  ' أَنَا الرَّجُلُ الْآلِيُّ بُوُ سَيْفْ,'
                  ' كَيْفَ حَالُك',
                  'أهلاً وَسَهلاً بِكُمْ, أَنَا الرَّجُلُ الْآلِيُّ بُوُ سَيْفْ, كَيْفَ حَالُك']



    if first_run:

        com.say(choice(intro_list))
        # choice(MotionList)()
    thread1678 = threading.Thread(target=main)
    thread1678.setDaemon(True)
    thread1678.start()


# thread150 = threading.Thread(target=run_test)
# thread150.setDaemon(True)
# thread150.start()

eye = Eye().start()
track = Track(eye, face_net, gender_net, age_net, object_net).start()
# Track.gender_estimation()

app = MyApp(redirect=False)
app.MainLoop()


# datetime object containing current date and time
