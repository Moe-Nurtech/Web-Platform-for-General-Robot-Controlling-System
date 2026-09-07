import os
import maestro
import time
import Dyn  # Uses Dynamixel SDK library
import dynamixel_sdk as dynamixel

servo = maestro.Controller()


if os.name == 'nt':
    import msvcrt
    
    def getch():
        return msvcrt.getch().decode()
else:
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
servo_list = []
# os.sys.path.append('../dynamixel_functions_py')  # Path setting

# Control table address
ADDR_PRO_TORQUE_ENABLE = 24  # Control table address is different in Dynamixel model
ADDR_PRO_GOAL_POSITION = 30
ADDR_PRO_PROFILE_VELOCITRY = 46
ADDR_PRO_GOAL_VELOCITRY = 32
ADDR_PRO_PRESENT_POSITION = 36
ADDR_PRO_PRESENT_VELOCITRY = 38

# Data Byte Length
LEN_PRO_GOAL_POSITION = 2
LEN_PRO_PRESENT_POSITION = 2

# Protocol version
PROTOCOL_VERSION = 1.0  # See which protocol version is used in the Dynamixel

# Default setting
DXL1_ID = 30
DXL2_ID = 31  # Dynamixel ID : 1
BAUDRATE = 57600  # Dynamixel default baudrate : 57600
DEVICENAME = "COM6"
# Check which port is being used on your controller
# ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

# Protocol version
# PROTOCOL_VERSION = 1  # See which protocol version is used in the Dynamixel

# Default setting
# DXL1_ID = 30 # Dynamixel ID: 1
# DXL2_ID = 31 # Dynamixel ID: 2
# BAUDRATE = 57600 #2000000 #57600 #1048576

# DEVICENAME = "/dev/ttyUSB0".encode('utf-8')  # Check which port is being used on your controller
# DEVICENAME = "COM4"  # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE = 0  # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE = 2048  # and this value # (note that the Dynamixel would not move
#                                    when the position value is out of movable range.
#                                    Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 20  # Dynamixel moving status threshold

ESC_ASCII_VALUE = 0x1b

COMM_SUCCESS = 1  # Communication Success result value
COMM_TX_FAIL = -1001  # Communication Tx Failed

# Initialize PortHandler Structs


index = 0
dxl_comm_result = COMM_TX_FAIL  # Communication result
dxl_addparam_result = 0  # AddParam result
dxl_getdata_result = 0  # GetParam result
dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]  # Goal position

dxl_error = 0  # Dynamixel error
dxl1_present_position = 0  # Present position
dxl2_present_position = 0

# sudo chmod a+rw /dev/ttyUSB0
portHandler = dynamixel.PortHandler(DEVICENAME)

portHandler.setPacketTimeoutMillis(0.1)  # # set time out 1 ms
packetHandler = dynamixel.PacketHandler(PROTOCOL_VERSION)


def start():
    global portHandler
    global packetHandler

    portHandler = dynamixel.PortHandler(DEVICENAME)
    portHandler.setPacketTimeoutMillis(0.1)  # # set time out 1 ms
    packetHandler = dynamixel.PacketHandler(PROTOCOL_VERSION)

    if portHandler.openPort():
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        print("Press any key to terminate...")
        getch()
        quit()

    # Set port baudrate
    if portHandler.setBaudRate( BAUDRATE):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        print("Press any key to terminate...")
        getch()
        quit()

    pass

# Open port


# Write 1 byte with error test code
def write4(dxl_id, add_reg, value_reg, msg):
    dxl_comm_result_, dxl_error_ = packetHandler.write4ByteTxRx(portHandler, dxl_id, add_reg, value_reg)
    if dxl_comm_result != COMM_SUCCESS:
        pass # print("%s" % packetHandler.getTxRxResult(dxl_comm_result_)))
    elif dxl_error != 0:
        pass # print("%s" % packetHandler.getRxPacketError(dxl_error_)))
    else:
        pass # print("ID", dxl_id, "write", msg, value_reg))
   

# Write 1 byte with error test code
def write1(dxl_id, add_reg, value_reg, msg):
    dxl_comm_result_, dxl_error_ = packetHandler.write1ByteTxRx(portHandler, dxl_id, add_reg, value_reg)
    if dxl_comm_result != COMM_SUCCESS:
        pass # print("%s" % packetHandler.getTxRxResult(dxl_comm_result_)))
    elif dxl_error != 0:
        pass # print("%s" % packetHandler.getRxPacketError(dxl_error_)))
    else:
        pass # print("ID", dxl_id, "write", msg, value_reg))
   

# Write 2 byte with error test code
def write2(dxl_id, add_reg, value_reg, msg):
    dxl_comm_result_, dxl_error_ = packetHandler.write2ByteTxRx(portHandler, dxl_id, add_reg, value_reg)
    if dxl_comm_result != COMM_SUCCESS:
        pass # print("%s" % packetHandler.getTxRxResult(dxl_comm_result_)))
    elif dxl_error != 0:
        pass # print("%s" % packetHandler.getRxPacketError(dxl_error_)))
    else:
        pass # print("ID", dxl_id, "write", msg, value_reg))


# Write 1 byte with error test code

# Read 1 byte with error test code
def read1(dxl_id, add_reg, msg):
    read_value, dxl_comm_result_, dxl_error_ = packetHandler.read1ByteTxRx(portHandler, dxl_id, add_reg)
    if dxl_comm_result != COMM_SUCCESS:
        pass # print("%s" % packetHandler.getTxRxResult(dxl_comm_result_)))
    elif dxl_error != 0:
        pass # print("%s" % packetHandler.getRxPacketError(dxl_error_)))
    elif dxl_comm_result == COMM_SUCCESS:    
        pass # print("ID:", dxl_id, msg, read_value))
    return read_value


# Read 2 byte with error test code
def read2(dxl_id, add_reg, msg):
    read_value, dxl_comm_result_, dxl_error_ = packetHandler.read2ByteTxRx(portHandler, dxl_id, add_reg)
    if dxl_comm_result != COMM_SUCCESS:
        pass # print("%s" % packetHandler.getTxRxResult(dxl_comm_result_)))
    elif dxl_error != 0:
        pass # print("%s" % packetHandler.getRxPacketError(dxl_error_)))
    elif dxl_comm_result == COMM_SUCCESS:
        pass # print("ID:", dxl_id, msg, read_value))
    return read_value


# Read 4 byte with error test code
def read4(dxl_id, add_reg, msg):
    read_value, dxl_comm_result_, dxl_error_ = packetHandler.read4ByteTxRx(portHandler, dxl_id, add_reg)
    if dxl_comm_result != COMM_SUCCESS:
        pass # print("%s" % packetHandler.getTxRxResult(dxl_comm_result_)))
    elif dxl_error != 0:
        pass # print("%s" % packetHandler.getRxPacketError(dxl_error_)))
    elif dxl_comm_result == COMM_SUCCESS:
        pass # print("ID:", dxl_id, msg, read_value))
    return read_value


def init_group_write(add_name):
    add = int(Dyn.gen_reg[add_name]["add"])
    len_add = int(Dyn.gen_reg[add_name]["size"])
    groupread_x = dynamixel.GroupSyncWrite(portHandler, packetHandler, add, len_add)
    return groupread_x


def Add_id_sync_group_write(groupwrite,ID,ADD_Name,Value):
    LEN_ADD=int(Dyn.gen_reg[ADD_Name]["size"])
    ADD=int(Dyn.gen_reg[ADD_Name]["add"])
    dxl_addparam_result = groupwrite.addParam(ID, Value)
    if dxl_addparam_result != True:
        pass # print("[ID:%03d] groupSyncWrite addparam failed" % DXL1_ID ))
    pass


def Write_Sync(groupwrite):
    # Syncwrite goal position
    dxl_comm_result = groupwrite.txPacket()
    if dxl_comm_result != COMM_SUCCESS:
        pass # print("%s" % packetHandler.getTxRxResult(dxl_comm_result)))

# function to Initialize Groupsyncread Structs for Address
def init_group_read(ADD_Name):
    ADD=int(Dyn.gen_reg[ADD_Name]["add"])
    LEN_ADD=int(Dyn.gen_reg[ADD_Name]["size"])
    groupSyncRead = dynamixel.GroupSyncRead(portHandler, packetHandler, ADD, LEN_ADD)
    return groupSyncRead


# Add parameter storage for packetHandler#1 present position value
def Add_id_sync_group_read(groupread,ID):
    dxl_addparam_result = groupread.addParam(ID)
    if dxl_addparam_result != True:
        pass # print("[ID:%03d] groupSyncRead addparam failed" % DXL2_ID ))
        quit()


def reboot(ID):
    dxl_comm_result, dxl_error = packetHandler.reboot(portHandler, ID)
    if dxl_comm_result != COMM_SUCCESS:
        pass # print("%s" % packetHandler.getTxRxResult(dxl_comm_result)))
    elif dxl_error != 0:
        pass # print("%s" % packetHandler.getRxPacketError(dxl_error)))

    pass # print("[ID:%03d] reboot Succeeded\n" % ID))
    pass

# Syncread present position
def Read_sync(groupread):
    groupread.txRxPacket()
    if dxl_comm_result != COMM_SUCCESS:
        pass # print("%s" % packetHandler.getTxRxResult(dxl_comm_result)))

def scan_ping(id_a,id_z):
    id_status=[]
    for X_ID in range(id_a,id_z):
        value=read1(X_ID,3,"id")
        if value>0:
            print(value)
            id_status.append(value)
            pass
        pass
    id_status.sort()
    
    return id_status


def Get_para_Value(groupread, ID, ADD_Name):
    ADD=int(Dyn.gen_reg[ADD_Name]["add"])
    LEN_ADD=int(Dyn.gen_reg[ADD_Name]["size"])

    # Check if groupsyncread data of packetHandler#1 is available
    dxl_getdata_result = groupread.isAvailable(ID, ADD, LEN_ADD)

    if dxl_getdata_result != 1:
        pass # print("[ID:%03d] groupSyncRead getdata failed" % (ID)))
        return None  
    # Get data of groupread is available
    if dxl_getdata_result == 1:
        ADD_Value = groupread.getData( ID, ADD, LEN_ADD )
        return ADD_Value
    pass

def write_print(ID,name,value):
    
    if Dyn.gen_reg[name]["size"]==1:
        write1(ID, int(Dyn.gen_reg[name]["add"]), int(value),name)
        
    elif Dyn.gen_reg[name]["size"]==2:
        write2(ID, int(Dyn.gen_reg[name]["add"]), int(value),name)
    elif Dyn.gen_reg[name]["size"]==4:
        write4(ID, int(Dyn.gen_reg[name]["add"]), int(value),name)

def write_dump(ID,name,value):
        

    if Dyn.gen_reg[name]["size"]==1:
        dxl_comm_result = packetHandler.write1ByteTxOnly(portHandler, ID, int(Dyn.gen_reg[name]["add"]), int(value))

    elif Dyn.gen_reg[name]["size"]==2:
        dxl_comm_result= packetHandler.write2ByteTxOnly(portHandler, ID, int(Dyn.gen_reg[name]["add"]), int(value))

    elif Dyn.gen_reg[name]["size"]==4:
        dxl_comm_result = packetHandler.write4ByteTxOnly(portHandler, ID, int(Dyn.gen_reg[name]["add"]), int(value))



def read_print(ID,name):

    if Dyn.gen_reg[name]["size"]==1:
        value=read1(ID, int(Dyn.gen_reg[name]["add"]),name)
    elif Dyn.gen_reg[name]["size"]==2:
        value=read2(ID, int(Dyn.gen_reg[name]["add"]),name)
    elif Dyn.gen_reg[name]["size"]==4:
        value=read4(ID, int(Dyn.gen_reg[name]["add"]),name)
        pass
    return value

'''<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
print("scan_ping")


start()
#print(scan_ping(1,40))



ii=[2,3,4,6,16,23,22,20,31,19,11]

#print(introduce_himself())
#print(take_seat())

# values = []

# for i in ii:

#     x=read_print(i,'PresentPosition')
    
#     values.append(x)
#     print(x)
# print ('Position of servos :' , values)
# #z=read_print(2,'PresentPosition')

#time.sleep(5)
#print(handshake())
#time.sleep(5)
#print(take_seat())
#time.sleep(5)
#iiii=[1,2,3,4,5,6,7,8,9,10]
#for i in iiii:
   # print(good_bye())
    
#print(no_action())
#read_print(22,PresentPosition)
#write_print(6,"TorqueEnable",0) 
#write_print(6,"MovingSpeed",45)
#write_print(2,"MovingSpeed",45)
#write_print(3,"MovingSpeed",45)
#write_print(4,"MovingSpeed",45)
#write_print(31,"MovingSpeed",45)
# write_print(40,"GoalPosition",200)
#write_print(3,"GoalPosition",250)
#write_print(4,"GoalPosition",50)
#write_print(2,"GoalPosition",200)

#write_print(21,"MovingSpeed",45)
#write_print(22,"MovingSpeed",45)
#write_print(23,"MovingSpeed",45)
#write_print(2,"MovingSpeed",45)
#write_print(3,"MovingSpeed",45)
#write_print(4,"MovingSpeed",45)
#write_print(6,"MovingSpeed",45)
#write_print(19,"MovingSpeed",45)
#write_print(16,"MovingSpeed",45)
#write_print(19,"TorqueEnable",1)
#write_print(19,"GoalPosition",300)
#write_print(20,"TorqueEnable",1)
#write_print(20,"GoalPosition",500)
#time.sleep(3)
#write_print(20,"GoalPosition",350)
#write_print(21,"TorqueEnable",1)
#write_print(27,"GoalPosition",0)
#write_print(22,"TorqueEnable",1)
#write_print(22,"GoalPosition",20)
#write_print(23,"TorqueEnable",1)
#write_print(23,"GoalPosition",250)
#write_print(2,"TorqueEnable",1)
#write_print(2,"GoalPosition",250)
#write_print(3,"TorqueEnable",0)
#write_print(3,"GoalPosition",500)
#write_print(4,"TorqueEnable",0)
#write_print(4,"GoalPosition",600)
#write_print(6,"TorqueEnable",0)
#write_print(6,"GoalPosition",300)
#write_print(16,"TorqueEnable",0)
#write_print(16,"GoalPosition",300)



#groupread_num=init_group_read("GoalPosition")
#Add_id_sync_group_read(groupread_num,30)
#Add_id_sync_group_read(groupread_num,31)
#Add_id_sync_group_read(groupread_num,32)
#Read_sync(groupread_num)
#goal_value_30=Get_para_Value(groupread_num, 30,"GoalPosition")
#goal_value_31=Get_para_Value(groupread_num, 31,"GoalPosition")
#goal_value_32=Get_para_Value(groupread_num, 32,"GoalPosition")
#print("id",30,"GoalPosition",goal_value_30)
#print("id",31,"GoalPosition",goal_value_31)
#print("id",32,"GoalPosition",goal_value_32)
# Close port


