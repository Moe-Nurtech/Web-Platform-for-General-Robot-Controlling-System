
gen_reg={'ID': {'name': 'ID', 'add': 3, 'size': 1, 'type': 'ROM'}, 
'ModelNumber': {'name': 'ModelNumber', 'add': 0, 'size': 2, 'type': 'ROM'}, 
#'ModelInfo': {'name': 'ModelInfo', 'add': 2, 'size': 2, 'type': 'ROM'}, 
'FirmVer': {'name': 'FirmVer', 'add': 2, 'size': 1, 'type': 'ROM'}, 
'BaudRate': {'name': 'BaudRate', 'add': 4, 'size': 1, 'type': 'ROM'}, 
'ReturnDelayTime': {'name': 'ReturnDelayTime', 'add': 5, 'size': 1, 'type': 'ROM'}, 
#'DriveMode': {'name': 'DriveMode', 'add': 10, 'size': 1, 'type': 'ROM'}, 
#'OperatingMode': {'name': 'OperatingMode', 'add': 11, 'size': 1, 'type': 'ROM'}, 
#'ShadowId': {'name': 'ShadowId', 'add': 12, 'size': 1, 'type': 'ROM'}, 
#'ProtocolVersion': {'name': 'ProtocolVersion', 'add': 13, 'size': 1, 'type': 'ROM'}, 
#'HomingOffset': {'name': 'HomingOffset', 'add': 20, 'size': 4, 'type': 'ROM'}, 
#'MovingThreshold': {'name': 'MovingThreshold', 'add': 24, 'size': 4, 'type': 'ROM'}, 
'MaxVolt': {'name': 'MaxVolt', 'add': 13, 'size': 1, 'type': 'ROM'}, 
'MinVolt': {'name': 'MinVolt', 'add': 12, 'size': 1, 'type': 'ROM'}, 
#'CurrentLimit': {'name': 'CurrentLimit', 'add': 38, 'size': 2, 'type': 'ROM'}, 
#'AccelerationLimit': {'name': 'AccelerationLimit', 'add': 40, 'size': 4, 'type': 'ROM'}, 
#'VelocityLimit': {'name': 'VelocityLimit', 'add': 44, 'size': 4, 'type': 'ROM'}, 
#'MaxPosition': {'name': 'MaxPosition', 'add': 48, 'size': 4, 'type': 'ROM'}, 
#'MinPosition': {'name': 'MinPosition', 'add': 52, 'size': 4, 'type': 'ROM'}, 
'Shutdown': {'name': 'Shutdown', 'add': 18, 'size': 1, 'type': 'ROM'}, 
'TorqueEnable': {'name': 'TorqueEnable', 'add': 24, 'size': 1, 'type': 'RAM'}, 
'Led': {'name': 'Led', 'add': 25, 'size': 1, 'type': 'RAM'}, 
'StatusReturn': {'name': 'StatusReturn', 'add': 16, 'size': 1, 'type': 'RAM'}, 
#'RegInstruction': {'name': 'RegInstruction', 'add': 69, 'size': 1, 'type': 'RAM'}, 
#'ErrorStatus': {'name': 'ErrorStatus', 'add': 70, 'size': 1, 'type': 'RAM'}, 
#'VelocityIgain': {'name': 'VelocityIgain', 'add': 27, 'size': 2, 'type': 'RAM'}, 
#'VelocityPgain': {'name': 'VelocityPgain', 'add': 28, 'size': 2, 'type': 'RAM'}, 
#'PositionDgain': {'name': 'PositionDgain', 'add': 26, 'size': 2, 'type': 'RAM'}, 
#'PositionIgain': {'name': 'PositionIgain', 'add': 82, 'size': 2, 'type': 'RAM'}, 
#'PositionPgain': {'name': 'PositionPgain', 'add': 84, 'size': 2, 'type': 'RAM'}, 
#'BusWatchdog': {'name': 'BusWatchdog', 'add': 98, 'size': 1, 'type': 'RAM'}, 
#'GoalCurrent': {'name': 'GoalCurrent', 'add': 102, 'size': 2, 'type': 'RAM'}, 
#'GoalVelocity': {'name': 'GoalVelocity', 'add': 104, 'size': 4, 'type': 'RAM'}, 
#'ProfileAcceleration': {'name': 'ProfileAcceleration', 'add': 108, 'size': 4, 'type': 'RAM'}, 
#'ProfileVelocity': {'name': 'ProfileVelocity', 'add': 112, 'size': 4, 'type': 'RAM'}, 
'GoalPosition': {'name': 'GoalPosition', 'add': 30, 'size': 2, 'type': 'RAM'}, 
'RealtimeTick': {'name': 'RealtimeTick', 'add': 50, 'size': 2, 'type': 'RAM'}, 
'Moving': {'name': 'Moving', 'add': 46, 'size': 1, 'type': 'RAM'}, 
'MovingSpeed': {'name': 'MovingSpeed', 'add': 32, 'size': 2, 'type': 'RAM'},
#'MovingStatus': {'name': 'MovingStatus', 'add': 123, 'size': 1, 'type': 'RAM'}, 
#'PresentCurrent': {'name': 'PresentCurrent', 'add': 126, 'size': 2, 'type': 'RAM'}, 
'PresentVelocity': {'name': 'PresentVelocity', 'add': 38, 'size': 2, 'type': 'RAM'}, 
'PresentPosition': {'name': 'PresentPosition', 'add': 36, 'size': 2, 'type': 'RAM'}, 
#'VelTrajectory': {'name': 'VelTrajectory', 'add': 136, 'size': 4, 'type': 'RAM'}, 
#'PosTrajectory': {'name': 'PosTrajectory', 'add': 140, 'size': 4, 'type': 'RAM'}, 
'PresentVoltage': {'name': 'PresentVoltage', 'add': 42, 'size': 1, 'type': 'RAM'}, 
'PresentTemp': {'name': 'PresentTemp', 'add': 4, 'size': 1, 'type': 'RAM'}}


vip_reg={'ID': {'name': 'ID', 'add': 3, 'size': 1, 'type': 'ROM'}, 
'ModelNumber': {'name': 'ModelNumber', 'add': 0, 'size': 2, 'type': 'ROM'}, 
#'ModelInfo': {'name': 'ModelInfo', 'add': 2, 'size': 2, 'type': 'ROM'}, 
'FirmVer': {'name': 'FirmVer', 'add': 2, 'size': 2, 'type': 'ROM'}, 
'BaudRate': {'name': 'BaudRate', 'add': 4, 'size': 1, 'type': 'ROM'}, 
'ReturnDelayTime': {'name': 'ReturnDelayTime', 'add': 5, 'size': 1, 'type': 'ROM'}, 
#'DriveMode': {'name': 'DriveMode', 'add': 10, 'size': 1, 'type': 'ROM'}, 
#'OperatingMode': {'name': 'OperatingMode', 'add': 11, 'size': 1, 'type': 'ROM'}, 
#'ShadowId': {'name': 'ShadowId', 'add': 12, 'size': 1, 'type': 'ROM'}, 
#'ProtocolVersion': {'name': 'ProtocolVersion', 'add': 13, 'size': 1, 'type': 'ROM'}, 
#'HomingOffset': {'name': 'HomingOffset', 'add': 20, 'size': 4, 'type': 'ROM'}, 
#'MovingThreshold': {'name': 'MovingThreshold', 'add': 24, 'size': 4, 'type': 'ROM'}, 
#'TempLimit': {'name': 'TempLimit', 'add': 31, 'size': 1, 'type': 'ROM'}, 
'MaxVolt': {'name': 'MaxVolt', 'add': 13, 'size': 1, 'type': 'ROM'}, 
'MinVolt': {'name': 'MinVolt', 'add': 12, 'size': 1, 'type': 'ROM'}}
para={}
para["ID"] 				  =3	         # - 1 Byte	RW 	initial Value(1) 0 ~ 252
para["ModelNumber"]			=0	         # - 2 Byte	R 	initial Value(311)
para["ModelInfo"]	 		  =2	     # - 2 Byte	R 	initial Value(-)
#para["FirmVer"]	 		  =6	     # - 2 Byte	R 	initial Value(-)
#para["BaudRate"] 			  =8	     # - 1 Byte	RW 	initial Value(1 "57600")
#para["ReturnDelayTime"] 	  =9	     # * 1 Byte	RW 	initial Value(250) 0 ~ 254, 1 Unit = 2uSec
#para["DriveMode"] 			  =10    	 # * 1 Byte	RW 	initial Value(0) CCW: Positive, CW: Nigative
#para["OperatingMode"]		  =11     	 # - 1 Byte	RW 	initial Value(3) 0:Current Control, 1:Velocity Control, 3:Position Control, 4:Extended Position Control, 5:Current-based Position Control
#para["ShadowId"] 			  =12     	 # - 1 Byte	RW 	initial Value(255) 0 ~ 252
#para["ProtocolVersion"]	  =13        # - 1 Byte	RW 	initial Value(2) 1 or 2
#para["HomingOffset"] 		  =20     	 # - 4 Byte	RW 	initial Value(0) 1 Unit = 0.088 deg
#para["MovingThreshold"] 	  =24     	 # - 4 Byte	RW 	initial Value(10) 0 ~ 1023, 1 Unit = 0.229[RPM]
#para["TempLimit"]			  =31     	 # - 1 Byte	RW 	initial Value(80) 0 ~ 100
#para["MaxVolt"]			  =32        # - 2 Byte	RW 	initial Value(160)  160 = 16.0 VDC
#para["MinVolt"]			  =34        # - 2 Byte	RW 	initial Value(95)   95  = 9.5  VDC
#para["CurrentLimit"] 		  =38        # - 2 Byte	RW 	initial Value(1941) 0 ~ 1941, 1 Unit = 3.36mA
para["AccelerationLimit"]    =40     	 # * 4 Byte	RW 	initial Value(32767) 1 Unit = 214.577[Rev/min2]
para["VelocityLimit"]        =44     	 # * 4 Byte	RW 	initial Value(435) 0 ~ 1023, 1 Unit = 0.229[RPM]
para["MaxPosition"] 		  =48        # * 4 Byte	RW 	initial Value(4095) 0 ~ 4095, 1 Unit = 0.088 deg
para["MinPosition"] 		  =52        # * 4 Byte	RW 	initial Value(0) 0 ~ 4095, 1 Unit = 0.088 deg
para["Shutdown"] 		  	  =63        # - 1 Byte	RW  Check Datasheet for more info


reg_len={}
reg_len["ID"] 				  =1              # - 1 Byte	RW 	initial Value(1) 0 ~ 252
reg_len["ModelNumber"]		  =2              # - 2 Byte	R 	initial Value(311)
reg_len["ModelInfo"]	 	  =2          	  # - 2 Byte	R 	initial Value(-)
reg_len["FirmVer"]	 		  =2              # - 2 Byte	R 	initial Value(-)
reg_len["BaudRate"] 		  =1              # - 1 Byte	RW 	initial Value(1 "57600")
reg_len["ReturnDelayTime"] 	  =1              # * 1 Byte	RW 	initial Value(250) 0 ~ 254, 1 Unit = 2uSec
reg_len["DriveMode"] 		  =1          	  # * 1 Byte	RW 	initial Value(0) CCW: Positive, CW: Nigative
reg_len["OperatingMode"]	  =1          	  # - 1 Byte	RW 	initial Value(3) 0:Current Control, 1:Velocity Control, 3:Position Control, 4:Extended Position Control, 5:Current-based Position Control
reg_len["ShadowId"] 		  =1          	  # - 1 Byte	RW 	initial Value(255) 0 ~ 252
reg_len["ProtocolVersion"]	  =1              # - 1 Byte	RW 	initial Value(2) 1 or 2
reg_len["HomingOffset"] 	  =4          	  # - 4 Byte	RW 	initial Value(0) 1 Unit = 0.088 deg
reg_len["MovingThreshold"] 	  =4          	  # - 4 Byte	RW 	initial Value(10) 0 ~ 1023, 1 Unit = 0.229[RPM]
reg_len["TempLimit"]		  =1          	  # - 1 Byte	RW 	initial Value(80) 0 ~ 100
reg_len["MaxVolt"]			  =2          	  # - 2 Byte	RW 	initial Value(160)  160 = 16.0 VDC
reg_len["MinVolt"]			  =2          	  # - 2 Byte	RW 	initial Value(95)   95  = 9.5  VDC
reg_len["CurrentLimit"] 	  =2              # - 2 Byte	RW 	initial Value(1941) 0 ~ 1941, 1 Unit = 3.36mA
reg_len["AccelerationLimit"]  =4          	  # * 4 Byte	RW 	initial Value(32767) 1 Unit = 214.577[Rev/min2]
reg_len["VelocityLimit"]      =4          	  # * 4 Byte	RW 	initial Value(435) 0 ~ 1023, 1 Unit = 0.229[RPM]
reg_len["MaxPosition"] 		  =4              # * 4 Byte	RW 	initial Value(4095) 0 ~ 4095, 1 Unit = 0.088 deg
reg_len["MinPosition"] 		  =4              # * 4 Byte	RW 	initial Value(0) 0 ~ 4095, 1 Unit = 0.088 deg
reg_len["Shutdown"] 		  =1              # - 1 Byte	RW  Check Datasheet for more info



##(p)aramiters (RAM)
ram={}
ram["TorqueEnable"] 		  =64  #// * 1 Byte	RW 	initial Value(0) 0 or 1, Enable Torque will lock EEPROM data from changes
ram["Led"] 				      =65  #// * 1 Byte	RW 	initial Value(0) 0 or 1, Enable or Disable LED
ram["StatusReturn"] 		  =68  #// - 1 Byte	RW 	initial Value(2) 0:No Status return, 1:Status return on Read instructions, 2:Status Return for ALL
ram["RegInstruction"] 	      =69  #// - 1 Byte	R 	Check Datasheet for more info
ram["ErrorStatus"] 		      =70  #// - 1 Byte	R   Check Datasheet for more info
ram["VelocityIgain"]		  =76
ram["VelocityPgain"]		  =78
ram["PositionDgain"]		  =80
ram["PositionIgain"]		  =82
ram["PositionPgain"]		  =84
ram["BusWatchdog"]		      =98  	#// - 1 Byte	RW 	initial Value(0) 0:Deactivate Bus Watchdog Function & Clear Bus Watchdog Error, 1~127:Activate Bus Watchdog, 1 Unit = 20ms, -1 Error Status
ram["GoalCurrent"]		      =102 	#// - 2 Byte	RW 	initial Value(-) Range : -Current Limit(38) ~ Current Limit(38)
ram["GoalVelocity"]		      =104 	#// - 4 Byte	RW 	initial Value(-) Range : -Velocity Limit(44)  ~ Velocity Limit(44)
ram["ProfileAcceleration"]    =108	# // - 4 Byte	RW 	initial Value(-) Range : 0 ~ Acceleration Limit(40), 1 Unit = 214.577[Rev/min2]
ram["ProfileVelocity"]	      =112 	#// - 4 Byte	RW 	initial Value(-) Range : 0 ~ Velocity Limit(44), 1 Unit = 0.229[RPM]
ram["GoalPosition"]		      =116 	#// - 4 Byte	RW 	initial Value(-) Range : 0 ~ 4095, 1 Unit = 0.088 deg, Min Position Limit(52) ~ Max Position Limit(48)
ram["RealtimeTick"]		      =120 	#// - 2 Byte	R 	initial Value(-) Range : 0 ~ 32,767, 1 Unit = 1ms, The value resets to '0' when it exceeds 32,767
ram["Moving"] 			      =122 	#// - 2 Byte	R 	initial Value(-) Range : 0 ~ or 1 , 0: Not Moving , Movement is detected, or Profile is in progress(Goal Position(116) instruction is being processed)
ram["MovingStatus"] 		  =123 	#// - 1 Byte	R 	initial Value(0) Detailed Information of Movement Status, Check Datasheet for more info
ram["PresentCurrent"] 	      =126 	#// - 2 Byte	R 	initial Value(-) This value indicates current Current. For more details, please refer to the Goal Current(102)
ram["PresentVelocity"] 	      =128 	#// - 4 Byte	R 	initial Value(-) This value indicates current Velocity. For more details, please refer to the Goal Velocity(104)
ram["PresentPosition"] 	      =132 	#// - 4 Byte	R 	initial Value(-) This value indicates present Position. For more details, please refer to the Goal Position(116)
ram["VelTrajectory"]		  =136 	#// - 4 Byte	R 	initial Value(-),Target Velocity Trajectory Generated by Profile
ram["PosTrajectory"]		  =140 	#// - 4 Byte	R 	initial Value(-),Target Position Trajectory Generated by Profile
ram["PresentVoltage"]	      =144 #// - 2 Byte	R 	initial Value(-), Current Input Voltage
ram["PresentTemp"]		      =146 #// - 1 Byte	R 	initial Value(-), Current Internal Temperature

ram_len={}
ram_len["TorqueEnable"] 		  =1  #// * 1 Byte	RW 	initial Value(0) 0 or 1, Enable Torque will lock EEPROM data from changes
ram_len["Led"] 				      =1  #// * 1 Byte	RW 	initial Value(0) 0 or 1, Enable or Disable LED
ram_len["StatusReturn"] 		  =1  #// - 1 Byte	RW 	initial Value(2) 0:No Status return, 1:Status return on Read instructions, 2:Status Return for ALL
ram_len["RegInstruction"] 	      =1  #// - 1 Byte	R 	Check Datasheet for more info
ram_len["ErrorStatus"] 		      =1  #// - 1 Byte	R   Check Datasheet for more info
ram_len["VelocityIgain"]		  =2
ram_len["VelocityPgain"]		  =2
ram_len["PositionDgain"]		  =2
ram_len["PositionIgain"]		  =2
ram_len["PositionPgain"]		  =2
ram_len["BusWatchdog"]		      =1  	#// - 1 Byte	RW 	initial Value(0) 0:Deactivate Bus Watchdog Function & Clear Bus Watchdog Error, 1~127:Activate Bus Watchdog, 1 Unit = 20ms, -1 Error Status
ram_len["GoalCurrent"]		      =2 	#// - 2 Byte	RW 	initial Value(-) Range : -Current Limit(38) ~ Current Limit(38)
ram_len["GoalVelocity"]		      =4 	#// - 4 Byte	RW 	initial Value(-) Range : -Velocity Limit(44)  ~ Velocity Limit(44)
ram_len["ProfileAcceleration"]    =4	    #// - 4 Byte	RW 	initial Value(-) Range : 0 ~ Acceleration Limit(40), 1 Unit = 214.577[Rev/min2]
ram_len["ProfileVelocity"]	      =4 	#// - 4 Byte	RW 	initial Value(-) Range : 0 ~ Velocity Limit(44), 1 Unit = 0.229[RPM]
ram_len["GoalPosition"]		      =2	#// - 4 Byte	RW 	initial Value(-) Range : 0 ~ 4095, 1 Unit = 0.088 deg, Min Position Limit(52) ~ Max Position Limit(48)
ram_len["RealtimeTick"]		      =2 	#// - 2 Byte	R 	initial Value(-) Range : 0 ~ 32,767, 1 Unit = 1ms, The value resets to '0' when it exceeds 32,767
ram_len["Moving"] 			      =2 	#// - 2 Byte	R 	initial Value(-) Range : 0 ~ or 1 , 0: Not Moving , Movement is detected, or Profile is in progress(Goal Position(116) instruction is being processed)
ram_len["MovingStatus"] 		  =1 	#// - 1 Byte	R 	initial Value(0) Detailed Information of Movement Status, Check Datasheet for more info
ram_len["PresentCurrent"] 	      =2 	#// - 2 Byte	R 	initial Value(-) This value indicates current Current. For more details, please refer to the Goal Current(102)
ram_len["PresentVelocity"] 	      =4 	#// - 4 Byte	R 	initial Value(-) This value indicates current Velocity. For more details, please refer to the Goal Velocity(104)
ram_len["PresentPosition"] 	      =4 	#// - 4 Byte	R 	initial Value(-) This value indicates present Position. For more details, please refer to the Goal Position(116)
ram_len["VelTrajectory"]		  =4 	#// - 4 Byte	R 	initial Value(-),Target Velocity Trajectory Generated by Profile
ram_len["PosTrajectory"]		  =4 	#// - 4 Byte	R 	initial Value(-),Target Position Trajectory Generated by Profile
ram_len["PresentVoltage"]	      =2     #// - 2 Byte	R 	initial Value(-), Current Input Voltage
ram_len["PresentTemp"]		      =1     #// - 1 Byte	R 	initial Value(-), Current Internal Temperature

