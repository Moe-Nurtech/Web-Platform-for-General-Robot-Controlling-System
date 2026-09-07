import threading
from motion import *
from random import choice
import wave
import contextlib
import os
One_Go = False

stop = False
m_start=True
m_go=True
duration=0
old_duration=0
sub_motion=8
def stop_or_not():
    global stop
    while True:
        try:
            stop = os.path.isfile('speech.wav')
            if not stop:
                stop = os.path.isfile('stop_blink')
        except ValueError:
            pass


def no_action_thread():
    
    while True:
        time.sleep(5)
        try:
            # print('start')
            
            choice([no_action1,
                    no_action2,
                    no_action3,
                    no_action3,
                    no_action4,
                    right_move(3),
                    left_move(3),
                    center_move(2)])()
            time.sleep(2)
            # print('end')
        except Exception as e:
            print(e)


stop_blink = False




def no_action():  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 100)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    No_actiom = [325, 470, 788, 658, 955, 685, 740, 385, 840, 730]
    for ID, x in zip(id_i, No_actiom):
        dynamixel.write_print(ID, "GoalPosition", x)

def no_action_thread1():
    threading.Thread(target=stop_or_not).start()
    global stop_blink
    global stop
    while True:
        time.sleep(1)
        # while not stop_blink:
        while not stop:
            time.sleep(2)
            for _ in range(int(3 / .1)):
                time.sleep(.05)
                if stop or stop_blink:
                    break
            if not stop:
                choice([dynamixel.servo.runScriptSub(1)])
            for _ in range(int(5 / .1)):
                time.sleep(.05)
                # if stop_blink:
                if stop or stop_blink:
                    break
            # if not stop_blink:
            if not stop:
                choice([dynamixel.servo.runScriptSub(1), pololuSubLoop(1, 9), dynamixel.servo.runScriptSub(1), pololuSubLoop(1, 10)])
            for _ in range(int(6 / .1)):
                time.sleep(.05)
                if stop or stop_blink:
                    break
            if not stop:
                choice([dynamixel.servo.runScriptSub(1)])


def smile():
    global Two_Go, stop_blink
    Two_Go = False
    stop_blink = True
    # print("Thread thread_one started..!")
    global One_Go
    
    pololuSubLoop_emotion(10, 2)
    One_Go = False
    stop_blink = False


def sad():
    global Two_Go, stop_blink
    stop_blink = True
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    pololuSubLoop_emotion(10, 4)
    One_Go = False
    stop_blink = False


def angry():
    global Two_Go, stop_blink
    stop_blink = True
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    
    pololuSubLoop_emotion(10, 5)
    One_Go = False
    stop_blink= False


def disgust():
    global Two_Go
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    
    pololuSubLoop_emotion(10, 6)
    One_Go = False


def fear():
    global Two_Go
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    
    pololuSubLoop_emotion(10, 7)
    One_Go = False
    
    
def fear1():
    global Two_Go
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    body_fear(7)
    
    One_Go = False


def surprise():
    global Two_Go
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    
    pololuSubLoop_emotion(10, 3)
    One_Go = False
    
    
def thread_1114():
    global Two_Go
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    time.sleep(2)
    pololuSubLoop(3, 11)
    One_Go = False


def hi_speak():
    global Two_Go
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go

    speed_control(45)
    speaking_fram1_2(5)
    time.sleep(3)


def hand_shake_speak():
    global Two_Go
    Two_Go = False
    global One_Go
    speed_control(60)
    handshake(1.5)


def fram1_speak():
    global Two_Go
    Two_Go = False
    global One_Go
    speed_control(45)

    speaking_fram1(5)
    One_Go = False


def fram1_speak1():
    global Two_Go
    Two_Go = False
    global One_Go
    speed_control(45)

    speaking_fram2(5)
    One_Go = False


def Hi_first():  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 70)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    hi = [324, 500, 740, 688, 956, 694, 765, 587, 832, 540]
    for ID, x in zip(id_i, hi):
        dynamixel.write_print(ID, "GoalPosition", x)
    time.sleep(5)
    x15122 = threading.Thread(target=no_action())
    x15122.daemon = True
    x15122.start()



def OnScreen():  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 100)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20,  1]
    on_screen = [194, 480, 740, 688, 956, 697, 780, 463,  540]
    for ID, x in zip(id_i, on_screen):
        dynamixel.write_print(ID, "GoalPosition", x)
    time.sleep(1)
    dynamixel.write_print(11, "GoalPosition", 700)
    time.sleep(5)


def Hi_first1():  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 70)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    hi = [324, 350, 740, 688, 956, 694, 765, 587, 832, 540]
    for ID, x in zip(id_i, hi):
        dynamixel.write_print(ID, "GoalPosition", x)
    time.sleep(5)
    x1511 = threading.Thread(target=no_action())
    x1511.daemon = True
    x1511.start()
    # no_action()


def Hi_first2():  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 70)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    hi = [324, 350, 650, 688, 956, 694, 765, 587, 832, 540]
    for ID, x in zip(id_i, hi):
        dynamixel.write_print(ID, "GoalPosition", x)
    time.sleep(5)
    x15133 = threading.Thread(target=no_action())
    x15133.daemon = True
    x15133.start()

def fram1_speak2():
    global Two_Go
    Two_Go = False
    global One_Go
    speed_control(45)

    no_action4()
    One_Go = False


def fram1_speak4():
    global Two_Go
    Two_Go = False
    global One_Go
    speed_control(45)

    speaking(5)
    One_Go = False


def good_bye__():
    global Two_Go
    Two_Go = False
    global One_Go
    speed_control(60)
    good_bye(3)
    One_Go = False


def right_slid():
    global Two_Go
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    right_move(3)
    One_Go = False


def center_slid():
    global Two_Go
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    center_move(3)
    One_Go = False


def left_slid():
    global Two_Go
    Two_Go = False
    # print("Thread thread_one started..!")
    global One_Go
    left_move(3)
    One_Go = False
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def speakFram_1():
    # x16 = threading.Thread(target=fram1_speak)
    # x16.daemon = True
    # x16.start()
    pass



def speakFram_2():
    x16 = threading.Thread(target=Hi_first)
    x16.daemon = True
    x16.start()
    pass


def speakFram_3():
    x15 = threading.Thread(target=OnScreen)
    x15.daemon = True
    x15.start()
    pass
def speakFram_21():
    x162 = threading.Thread(target=Hi_first1)
    x162.daemon = True
    x162.start()
    pass
def speakFram_22():
    x161 = threading.Thread(target=Hi_first2)
    x161.daemon = True
    x161.start()
    pass
def speakFram_222():
    choice([speakFram_22(),speakFram_2(),speakFram_21()])
    pass
def speakFram_5():
    # x14 = threading.Thread(target=fram1_speak4)
    # x14.daemon = True
    # x14.start()
    pass


def main22smile():
    x13 = threading.Thread(target=smile)
    x13.daemon = True
    x13.start()


def good_bye_():
    x12 = threading.Thread(target=good_bye__())
    x12.daemon = True
    x12.start()

    
def main22sad():
    x11 = threading.Thread(target=sad)
    x11.daemon = True
    x11.start()
    
    
def main22angry():
    x9 = threading.Thread(target=angry)
    x9.daemon = True
    x9.start()
    
    
def main22disgust():
    x8 = threading.Thread(target=disgust)
    x8.daemon = True
    x8.start()
    
    
def main22fear():
    x7 = threading.Thread(target=fear)
    x7.daemon = True
    x7.start()
    
    
def main22fear1():
    x6 = threading.Thread(target=fear1)
    x6.daemon = True
    x6.start()
    

def main22surprise():
    x5 = threading.Thread(target=surprise)
    x5.daemon = True
    x5.start()


def blinking_thread():
    # thread3 = threading.Thread(target=no_action_thread)
    # thread3.start()
    pass


def blinking_thread1():

    thread2 = threading.Thread(target=no_action_thread1)
    thread2.start()


def hi_thread():
    # x4 = threading.Thread(target=hi_speak)
    # x4.daemon = True
    # x4.start()
    pass


def hand_shake():
    # x3 = threading.Thread(target=hand_shake_speak)
    # x3.daemon = True
    # x3.start()
    pass


def rightSlid():
    x1 = threading.Thread(target=right_slid)
    x1.daemon = True
    x1.start()


def centerSlid():
    x2 = threading.Thread(target=center_slid)
    x2.daemon = True
    x2.start()


def leftSlid():
    x00 = threading.Thread(target=left_slid)
    x00.daemon = True
    x00.start()
# duration = 0.0


def duration_wav():
    global stop_blink
    global stop
    while True:
        try:

            with contextlib.closing(wave.open('speech.wav', 'r')) as f:
                stop_blink = True
                stop = True
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)

            pololuSubLoop(duration, 8)
            time.sleep(duration)
            # print('Duration: ', duration)
            stop_blink = False
            stop = False
            return
        except PermissionError:
            stop = False
            stop_blink = False
            continue


def duration_wav1():
    x = threading.Thread(target=duration_wav)
    x.daemon = True
    x.start()
def run_motion1():
     global duration
     tic = time.perf_counter()
     toc = time.perf_counter()
     while(toc-tic < (duration/1000)):
        pololustartSub(8)
        toc = time.perf_counter()
     pololu_noAction()

def stop_motion1():
    global m_start
    global m_go
    m_start=True
    m_go=False
    print("Stoped mmmmm")
    pololu_noAction()
def visime_wav(mduration):
    global stop_blink
    global stop
    pololuSubLoop(mduration, 8)
    print('Mdddd',"fdgfdgfdg")
    time.sleep(duration)
    stop_blink = False
    stop = False

def Visime_motion(time_i,sub):
    global duration
    global sub_motion
    duration=time_i
    sub_motion=sub
    #x = threading.Thread(target=visime_wav)
    #x.daemon = False
    #x.start()
def run_motion():
    global m_start
    global m_go
    global duration
    print('Durationlll: ', duration)
    m_go=True
    if m_start:
        x = threading.Thread(target=run_motion1)
        x.daemon = True
        x.start()
        m_start=False
        print("STart mmmmm")

def stop_motion():
    x = threading.Thread(target=stop_motion1)
    x.daemon = True
    x.start()