import dynamixel

import time


START_TIME = time.time()


def speed_control(speed):
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    for ID in id_i:
        dynamixel.write_print(ID, "MovingSpeed", speed)
    return


# the reference point
def no_action1():
    no_action = [200, 700, 630, 700, 1000, 590, 760, 512, 920, 650]
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    speed_control(30)

    for ID, x in zip(id_i, no_action):
        dynamixel.write_print(ID, "GoalPosition", x)

    return


def no_action2():
    no_action_1 = [200, 700, 630, 700, 920, 620, 760, 512, 830, 650]
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    speed_control(30)

    for ID, x in zip(id_i, no_action_1):
        time.sleep(1.5)
        dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(0.2)

    return  


def no_action3():

    no_action_2 = [200, 700, 630, 700, 980, 560, 760, 512, 830, 650]

    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    speed_control(30)

    for ID, x in zip(id_i, no_action_2):
        # time.sleep(1)
        dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(0.2)

    return


def no_action4():

    no_action_2 = [200, 700, 630, 700, 980, 560, 760, 440, 660, 650]

    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    speed_control(30)

    for ID, x in zip(id_i, no_action_2):
        # time.sleep(1)
        dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(0.2)

    return


def handshake(count_):  # Hand shake when some tell him the greeting
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    handshak_1 = [200, 700, 630, 700, 950, 700, 750, 512, 700, 650]
    handshak_3 = [200, 700, 630, 700, 950, 700, 750, 512, 780, 630]

    count = 0
    while count < count_:

        for ID, x in zip(id_i, handshak_1):
            dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(1)

        for ID, x in zip(id_i, handshak_3):
            dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(1)
        count += 1   
    no_action1()
    return



    
def good_bye(count_):  # Say goodbye speak & move hand
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    goodbye = [200, 700, 630, 700, 800, 750, 512, 620, 400]
    goodbye_1 = [200, 700, 630, 700, 950, 800, 750, 612, 620, 400]

    count = 0
    while count < count_:

        for ID, x in zip(id_i, goodbye):
            dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(1)
        for ID, x in zip(id_i, goodbye_1):
            dynamixel.write_print(ID, "GoalPosition", x)
            
        time.sleep(1)
        count += 1   
    no_action1()
    return




def speaking(count_):  # speaking mode move hands and speak (fram 1)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    speak = [200, 700, 630, 700, 850, 650, 750, 512, 750, 650]
    speak_1 = [200, 700, 630, 700, 850, 650, 750, 550, 800, 650]
    count = 0
    while count < count_:
        for ID, x in zip(id_i, speak):
            dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(2)
        for ID, x in zip(id_i, speak_1):
            dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(1)
        count += 1   
    no_action1()
    return


def speaking_fram2(timer):  # speaking mode move hands and speak (fram 2)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    move_i = [200, 700, 630, 700, 900, 650, 800, 450, 830, 650]
    move_i2 = [200, 700, 630, 700, 900, 650, 800, 550, 830, 650]
    for ID, x in zip(id_i, move_i):
        dynamixel.write_print(ID, "GoalPosition", x)
    time.sleep(3)
    for ID, x in zip(id_i, move_i2):
        dynamixel.write_print(ID, "GoalPosition", x)
        
    time.sleep(timer)
    no_action1()
    return


def speaking_fram1(time_s):  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    speak_farm1 = [200, 700, 630, 700, 950, 650, 800, 450, 700, 850]

    for ID, x in zip(id_i, speak_farm1):
        dynamixel.write_print(ID, "GoalPosition", x)
    time.sleep(time_s)
    no_action1()
    return


def speaking_fram1_2(time_s):  # speaking mode move hands and speak (fram 3)
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    speak_farm1 = [200, 700, 630, 700, 950, 800, 750, 512, 650, 850]


    for ID, x in zip(id_i, speak_farm1):
        dynamixel.write_print(ID, "GoalPosition", x)

    time.sleep(time_s)
    no_action1()
    return

def introduce_himself(time_i):  # when the robot introduce him self move his hand and speak
    id_i = [31, 27, 3, 2, 6, 23, 19, 20, 11, 1]
    introduce_himself_ = [200, 700, 630, 700, 950, 640, 700, 400, 600, 888]

    for ID, x in zip(id_i, introduce_himself_):
        dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(time_i)
        no_action1()
    return


def body_fear(time_i):  # Fear facial expression & hand moving as a fear one
    id_i = [31, 1, 11, 27, 2, 3, 6, 23, 20, 19]
    fear = [530, 398, 595, 700, 744, 630, 827, 669, 565, 792]
    dynamixel.servo.runScriptSub(8)
    for ID, x in zip(id_i, fear):
        dynamixel.write_print(ID, "GoalPosition", x)
        time.sleep(0.2)
        time.sleep(time_i)
      
        no_action1()
    return


def left_move(time_i):  # Fear facial expression & hand moving as a fear one
    id_i = [16]
    left = [780]

    for ID, x in zip(id_i, left):
        speed_control(45)
        dynamixel.write_print(ID, "GoalPosition", x)

    time.sleep(time_i)
    return


def center_move(time_i):  # Fear facial expression & hand moving as a fear one
    id_i = [16]
    left = [730]

    for ID, x in zip(id_i, left):
        speed_control(45)
        dynamixel.write_print(ID, "GoalPosition", x)

    time.sleep(time_i)
    return


def right_move(time_i):  # Fear facial expression & hand moving as a fear one
    id_i = [16]
    right = [660]

    for ID, x in zip(id_i, right):
        speed_control(45)
        dynamixel.write_print(ID, "GoalPosition", x)

    time.sleep(time_i)
    return


def pololu_noAction():
    dynamixel.servo.runScriptSub(0)



def pololuSubLoop(time_i, sub):
    # facial expression sub => [0'no_action',  1'blinking', 2'speak_mode,  3'smile',  4'surprised',  5'sad',  6'angry']
    time.sleep(0.5)
    
    dynamixel.servo.runScriptSub(sub)
    time.sleep(time_i)
    
    dynamixel.servo.runScriptSub(0)
    return


def pololustartSub(sub):
    # facial expression sub => [0'no_action',  1'blinking', 2'speak_mode,  3'smile',  4'surprised',  5'sad',  6'angry']
    #time.sleep(0.5)
    dynamixel.servo.runScriptSub(sub)
    time.sleep(0.7)
    return

def pololuSubLoop_emotion(time_i, sub):
    # facial expression sub => [0'no_action',  1'blinking', 2'speak_mode,  3'smile',  4'surprised',  5'sad',  6'angry']
      
    dynamixel.servo.runScriptSub(sub)
    time.sleep(time_i)
    
    dynamixel.servo.runScriptSub(0)
    return
# pololuSubLoop(11)


def turn_off():  # exit
    
    # NOW_TIME = time.time()- START_TIME
    # if NOW_TIME >= 15.0:
    dynamixel.servo.close()
    dynamixel.portHandler.closePort()
    exit()
    return

# pololuSubLoop(10, 6)
