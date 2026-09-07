import dynamixel
import time
import threading
from random import choice
def no_action():  # speaking mode move hands and speak (fram 3)
    id_i = [1, 11, 15, 27, 28, 31, 18, 19]
    No_actiom = [900, 540, 225, 440, 400, 455, 360, 720]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 70)
    for ID, x in zip(id_i, No_actiom):
        dynamixel.write_print(ID, "GoalPosition", x)

def LeftArm1():  # speaking mode move hands and speak (fram 3)
    id_i = [1, 11, 15, 27, 28, 31, 18, 19]
    hi = [900, 540, 420, 450, 315, 455, 310, 720]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 100)
    for ID, x in zip(id_i, hi):
        dynamixel.write_print(ID, "GoalPosition", x)
    # print(1)
    time.sleep(2)
    thread2000310 = threading.Thread(target=no_action())
    thread2000310.setDaemon(True)
    thread2000310.start()


def RightArm1():  # speaking mode move hands and speak (fram 3)
    id_i = [1, 11, 15, 27, 28, 31, 18, 19]
    hi = [900, 540, 225, 395, 400, 455, 180, 720]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 100)
    for ID, x in zip(id_i, hi):
        dynamixel.write_print(ID, "GoalPosition", x)
    # print(2)
    time.sleep(2)
    thread2000310 = threading.Thread(target=no_action())
    thread2000310.setDaemon(True)
    thread2000310.start()


def LeftArm2():  # speaking mode move hands and speak (fram 3)
    id_i = [1, 11, 15, 27, 28, 31, 18, 19]
    on_screen = [900, 540, 450, 440, 400, 455, 360, 720]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 100)
    for ID, x in zip(id_i, on_screen):
        dynamixel.write_print(ID, "GoalPosition", x)
    # print(2)
    time.sleep(2)
    thread2000310 = threading.Thread(target=no_action())
    thread2000310.setDaemon(True)
    thread2000310.start()


def RightArm2():  # speaking mode move hands and speak (fram 3)
    id_i =      [31  , 27 , 3,   2,   6 , 23,   19, 15,   11, 1]
    on_screen = [206, 445, 440, 605, 960, 640, 700, 450, 430, 900]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 100)
    for ID, x in zip(id_i, on_screen):
        dynamixel.write_print(ID, "GoalPosition", x)
    # print(2)
    time.sleep(2)
    thread2000310 = threading.Thread(target=no_action())
    thread2000310.setDaemon(True)
    thread2000310.start()


def RightArm3():  # speaking mode move hands and speak (fram 3)
    id_i =      [31  , 27 , 3,   2,   6 , 23,   19, 15,   11, 1]
    on_screen = [206, 445, 440, 605, 960, 640, 700, 320, 430, 900]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", 100)
    for ID, x in zip(id_i, on_screen):
        dynamixel.write_print(ID, "GoalPosition", x)
    # print(2)
    time.sleep(2)
    thread2000310 = threading.Thread(target=no_action(), args=(None,))
    thread2000310.setDaemon(True)
    thread2000310.start()





def MotionThread1():
    thread200031 = threading.Thread(target=no_action(), args=(1,))
    thread200031.setDaemon(True)
    thread200031.start()
def MotionThread2():
    thread200032 = threading.Thread(target=LeftArm1(), args=(1,))
    thread200032.setDaemon(True)
    thread200032.start()
def MotionThread3():
    thread200033 = threading.Thread(target=RightArm1(), args=(1,))
    thread200033.setDaemon(True)
    thread200033.start()
# def MotionThread4():
#     thread200034= threading.Thread(target=no_action(), args=(1,))
#     thread200034.setDaemon(True)
#     thread200034.start()
# def MotionThread5():
#     thread200035 = threading.Thread(target=no_action(), args=(1,))
#     thread200035.setDaemon(True)
#     thread200035.start()
