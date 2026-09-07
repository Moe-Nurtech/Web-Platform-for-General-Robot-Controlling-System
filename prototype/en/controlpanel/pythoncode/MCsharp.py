import dynamixel
from motion import *

id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
for ID in id_i:
    dynamixel.write_print(ID, "MovingSpeed", 100)



def no_action():  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    No_actiom = [325, 470, 788, 658, 955, 685, 740, 385, 840, 730]
    for ID, x in zip(id_i, No_actiom):
        dynamixel.write_print(ID, "GoalPosition", x)


def Hi_first():  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    hi = [324, 500, 740, 688, 956, 694, 765, 587, 832, 540]
    for ID, x in zip(id_i, hi):
        dynamixel.write_print(ID, "GoalPosition", x)
    time.sleep(2)
    no_action()

    return

def OnScreen():  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20,  1]
    on_screen = [194, 480, 740, 688, 956, 697, 780, 463,  540]
    for ID, x in zip(id_i, on_screen):
        dynamixel.write_print(ID, "GoalPosition", x)
    time.sleep(1)
    dynamixel.write_print(11, "GoalPosition", 700)
    time.sleep(2)
    no_action()
    return

def motion0():

    thread1678 = threading.Thread(target=main)
    thread1678.setDaemon(True)
    thread1678.start()
def motion1():
    thread1678 = threading.Thread(target=main)
    thread1678.setDaemon(True)
    thread1678.start()
def motion1():
    thread1678 = threading.Thread(target=main)
    thread1678.setDaemon(True)
    thread1678.start()