#!/usr/bin/env python
"""
	@file : process_string.py
	@description: Library to analyze the string result
    @author : IoT-HEC, VNPT-Technology
"""
import os
import random
import json
import re, os, time
import time
from datetime import datetime
import string
from random import *
import filecmp

def Valid_Add_Dev_With_Eui(subscribe_msgs, euiDev, deviceType):
	"""
	Description:  Check function Add for One Device. The added device has true the EUI and the Device Type
		[IN] subscribe_msgs: The message received after 60s subscribe
		[IN] euiDev: The Device EUI
		[IN] deviceType: The Device Type
	Return :
		[OUT] : TRUE if device founded, FALSE if not. Type Boolean
	"""
	msgIDList = []
	if len(subscribe_msgs)==0:
		# Check if no item exist in the message received after 60s subscribe
		raise Exception ("No Device Added")
	else:
		# Check the number of messages which have type is "commsion" and Properties command is "addDevice". Return a list position
		# There are three cases:
		# 1. No message with type is common and command Adddevice -> Return No Device Added
		# 2. There msg type is common and command addDevice, but the data is success or Error: -> Return No Deviced Added
		# 3. There is one device Added
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "commission") and (msg['dataMessage']['properties']['command'] == "addDevice"):
				msgIDList.append(pos)

		if 	len(msgIDList) != 0 :
			for msgID in msgIDList:
				msgExc = ''
				findDev = False
				msg = json.loads(subscribe_msgs[msgID])
				data = msg['dataMessage']['properties']['data']
				# Check data is list or not
				if type(data) is list:
					numDev = Get_Number_Device(data)
					if (numDev == 1):
						data_str = (data[0])
						if (data_str['deviceEUI'] == euiDev) and (data_str['deviceType'] == deviceType):
							findDev = True
							break
						elif (data_str['deviceEUI'] != euiDev):
							findDev = False
							msgExc = "Please check DeviceEUI. "  + euiDev + " != "+ data_str['deviceEUI']
						elif (data_str['deviceType'] != deviceType):
							findDev = False
							msgExc = "Please check deviceType. " + deviceType + " != " + data_str['deviceType']
				else:
					findDev = False
					msgExc = "No Device Added"
			if findDev == True:
				return True
			else:
				raise Exception(msgExc)
		else:
			raise Exception ("No Device Added")
	return	False

def Valid_Add_Device_No_EUI(subscribe_msgs, deviceType):
	"""
	Description:  Check function Add for One Device. The added device has true Device Type, no need check for EUI device
		[IN] subscribe_msgs: The message received after 60s subscribe
		[IN] deviceType: The Device Type
	Return :
		[OUT] : TRUE if device founded, FALSE if not. Type Boolean
	"""
	msgIDList = []
	if len(subscribe_msgs)==0:
		# Check if no item exist in the message received after 60s subscribe
		raise Exception ("No Device Added")
	else:
		# Check the number of messages which have type is "commsion" and Properties command is "addDevice". Return a list position
		# There are three cases:
		# 1. No message with type is common and command Adddevice -> Return No Device Added
		# 2. There msg type is common and command addDevice, but the data is success or Error: -> Return No Deviced Added
		# 3. There is one device Added
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "commission") and (msg['dataMessage']['properties']['command'] == "addDevice"):
				msgIDList.append(pos)

		if 	len(msgIDList) != 0 :
			for msgID in msgIDList:
				msgExc = ''
				findDev = False
				msg = json.loads(subscribe_msgs[msgID])
				data = msg['dataMessage']['properties']['data']
				# Check data is list or not
				if type(data) is list:
					numDev = Get_Number_Device(data)
					if (numDev == 1):
						data_str = (data[0])
						if (data_str['deviceType'] == deviceType):
							findDev = True
							break
						elif (data_str['deviceType'] != deviceType):
							findDev = False
							msgExc = "Please check deviceType. " + deviceType + " != " + data_str['deviceType']
				else:
					findDev = False
					msgExc = "No Device Added"
			if findDev == True:
				return True
			else:
				raise Exception(msgExc)
		else:
			raise Exception ("No Device Added")
	return	False

def Valid_Add_More_Devices(subscribe_msgs):
	"""
	Description: Check function add  two or more devices when open network (about 60s)
		[IN]: subscribe_msgs: The message received after 60s subscribe
		[IN]: numDevInput: number of input devices
	Return:
		[OUT]: TRUE if number devices founded, FALSE if not. Type Boolean
	"""
	msgIDList = []
	cntAddDev = 0
	if len(subscribe_msgs)==0:
		# Check if no item exist in the message received after 60s subscribe
		raise Exception ("No Device Added")
	else:
		# Check the number of messages which have type is "commsion" and Properties command is "addDevice". Return a list position
		# There are three cases:
		# 1. No message with type is common and command Adddevice -> Return No Device Added
		# 2. There msg type is common and command addDevice, but the data is success or Error: -> Return No Deviced Added
		# 3. There are more devices
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "commission") and (msg['dataMessage']['properties']['command'] == "addDevice"):
				msgIDList.append(pos)

		if 	len(msgIDList) != 0 :
			for msgID in msgIDList:
				msgExc = ''
				msg = json.loads(subscribe_msgs[msgID])
				data = msg['dataMessage']['properties']['data']
				# Check data is list or not
				if type(data) is list:
					numDev = Get_Number_Device(data)
					if (numDev == 1):
						cntAddDev = cntAddDev+1
			if cntAddDev == 0:
				raise Exception("No Device Added")
			elif cntAddDev == 1:
				return True
			else:
				raise Exception("Please check number device Added. " + str(cntAddDev) + " != " + str(1))
		else:
			raise Exception ("No Device Added")
	return	False

def Valid_List_Device_None(subscribe_msgs):
	"""
	Description: Validate function List Device, when the list device none.
		[IN]: subscribe_msgs: The message received subscribe
	Return:
		[OUT]: TRUE if list devices NONE, FALSE if not. Type Boolean
	"""
	mgsID = 0
	if len(subscribe_msgs)== 0:
		# Check if no item exist in the message received after subscribe
		raise Exception ("Please check connection network. No message received!")
	else:
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "listDevice"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']
		numDev	= Get_Number_Device(data)

		if numDev == 0:
			return True
		else:
		 	raise Exception("List device is not NONE")
    return	False

def Valid_List_Devices(subscribe_msgs):
	"""
	Description: Validate function List Device, when the list device none.
		[IN]: subscribe_msgs: The message received subscribe
	Return:
		[OUT]: TRUE if list devices NONE, FALSE if not. Type Boolean
	"""
	mgsID = 0
	if len(subscribe_msgs)== 0:
		# Check if no item exist in the message received after subscribe
		raise Exception ("Please check connection network. No message received!")
	else:
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "listDevice"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']
		numDev	= Get_Number_Device(data)

		if numDev != 0:
			return True
		else:
		 	raise Exception("List device is NONE")
	return	False

def Check_Device_With_EUI_And_DeviceName(subscribe_msgs, deviceEUI, deviceName=''):
	"""
	Description: Check Device with deviceName and deviceEUI after using change Device Name function
		[IN]: subscribe_msgs: The message received subscribe
		[IN]: deviceEUI: the EUI of device
		[IN]: deviceName: new name of device
	Return:
		[OUT]: TRUE if list devices NONE, FALSE if not. Type Boolean
	"""
	if len(subscribe_msgs) == 0:
		# Check if no item exist in the message received after subscribe
		raise Exception ("Please check connection network. No message received!")
	else:
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "listDevice"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']
		numDev	= Get_Number_Device(data)
		if numDev != 0:
			for idx in range(numDev):
				data_str = (data[idx])

				if (data_str['deviceEUI'] == deviceEUI):
					findDev = True
					break
				else:
					findDev = False

			if findDev == True:
				if (data_str['deviceName']== deviceName):
					return True
				else:
					raise Exception("Device Name did not change to new value! " + data_str['deviceName'] + "!=" + deviceName)
			else:
				raise Exception("Can not find device in list: " + deviceEUI )
	return False

def Check_Device_With_EUI_And_Device_Locate(subscribe_msgs, deviceEUI, deviceLoc=''):
	"""
	Description: Check Device with device locate and deviceEUI after using change Device Name function
		[IN]: subscribe_msgs: The message received subscribe
		[IN]: deviceEUI: the EUI of device
		[IN]: deviceLoc: new locate of device
	Return:
		[OUT]: TRUE if list devices NONE, FALSE if not. Type Boolean
	"""
	if len(subscribe_msgs) == 0:
		# Check if no item exist in the message received after subscribe
		raise Exception ("Please check connection network. No message received!")
	else:
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "listDevice"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']
		numDev	= Get_Number_Device(data)
		if numDev != 0:
			for idx in range(numDev):
				data_str = (data[idx])

				if (data_str['deviceEUI'] == deviceEUI):
					findDev = True
					break
				else:
					findDev = False

			if findDev == True:
				if (data_str['deviceLocate']== deviceLoc):
					return True
				else:
					raise Exception("Device Locate did not change to new value! " + data_str['deviceLocate'] + "!=" + deviceLoc)
			else:
				raise Exception("Can not find device in list: " + deviceEUI )
	return False

def Check_Device_With_DeviceName_And_Device_Locate(subscribe_msgs, deviceEUI, deviceName='', deviceLoc=''):
	"""
	Description: Check Device with device locate and deviceEUI after using change Device Name function
		[IN]: subscribe_msgs: The message received subscribe
		[IN]: deviceEUI: the EUI of device
		[IN]: deviceName: new name of device
		[IN]: deviceLoc: new locate of device
	Return:
		[OUT]: TRUE if list devices NONE, FALSE if not. Type Boolean
	"""
	if len(subscribe_msgs) == 0:
		# Check if no item exist in the message received after subscribe
		raise Exception ("Please check connection network. No message received!")
	else:
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "listDevice"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']
		numDev	= Get_Number_Device(data)
		if numDev != 0:
			for idx in range(numDev):
				data_str = (data[idx])

				if (data_str['deviceEUI'] == deviceEUI):
					findDev = True
					break
				else:
					findDev = False

			if findDev == True:
				if (data_str['deviceLocate'] == deviceLoc) and (data_str['deviceName'] == deviceName):
					return True
				elif(data_str['deviceName'] != deviceName):
					raise Exception("Device Name did not change to new value! " + data_str['deviceName'] + "!=" + deviceName)
				elif(data_str['deviceLocate'] == deviceLoc):
					raise Exception("Device locate did not change to new value! " + data_str['deviceLocate'] + "!=" + deviceLoc)
				else:
					raise Exception("Device locate and device name did not change to new value! " + data_str['deviceLocate'] + "!=" + deviceLoc + ";" + data_str['deviceName'] + "!=" + deviceName)
			else:
				raise Exception("Can not find device in list: " + deviceEUI )
	return False

def Check_Device_With_EUI_And_ChildDeviceName(subscribe_msgs, deviceEUI, childID, deviceName=''):
	"""
	Description: Check Device with deviceName and deviceEUI after using change Device Name function
		[IN]: subscribe_msgs: The message received subscribe
		[IN]: deviceEUI: the EUI of device
		[IN]: deviceName: new name of device
	Return:
		[OUT]: TRUE if list devices NONE, FALSE if not. Type Boolean
	"""
	if len(subscribe_msgs) == 0:
		# Check if no item exist in the message received after subscribe
		raise Exception ("Please check connection network. No message received!")
	else:
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "listDevice"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']
		numDev	= Get_Number_Device(data)
		if numDev != 0:
			for idx in range(numDev):
				data_str = (data[idx])

				if (data_str['deviceEUI'] == deviceEUI):
					findDev = True
					break
				else:
					findDev = False

			if findDev == True:

				if (data_str['deviceName'] == deviceName) and (data_str['deviceName'] == deviceName):
					return True
				else:
					raise Exception("Device Name did not change to new value! " + data_str['deviceName'] + "!=" + deviceName)
			else:
				raise Exception("Can not find device in list: " + deviceEUI )
	return False

def Valid_List_Gateway_Data(subscribe_msgs):
	"""
	Description: Validate function request Gateway data.
		[IN]: subscribe_msgs: The message received subscribe
	Return:
		[OUT]: TRUE if list devices NONE, FALSE if not. Type Boolean
	"""
	mgsID = 0
	if len(subscribe_msgs)== 0:
		# Check if no item exist in the message received after subscribe
		raise Exception ("Please check connection network. No message received!")
	else:
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "gatewayData"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']
		numDev	= Get_Number_Device(data)

		if numDev != 0:
			return True
		else:
		 	raise Exception("List Gateway is NONE")
	return False

def Check_Config_Gateway_Changed(subscribe_msgs, configType , value=''):
	"""
	Description: Check Device with deviceName and deviceEUI after using change Device Name function
		[IN]: subscribe_msgs: The message received subscribe
		[IN]: configType: the EUI of device
		[IN]: timeZone: new name of device
	Return:
		[OUT]: TRUE if list devices NONE, FALSE if not. Type Boolean
	"""
	mgsID = 0
	if len(subscribe_msgs) == 0:
		# Check if no item exist in the message received after subscribe
		raise Exception("Please check connection network. No message received!")
	else:
		for pos, each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "gatewayData"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']

		if configType == 'timeZone':
			if data['timeZone'] == value:
				return  True
			else:
				raise Exception("Timezone didn't change! " + data['timeZone'] + "!=" + str(value))
		elif configType == 'buzzerStatus':
			if data['buzzerData']['status'] == value:
				return True
			else:
				raise Exception("Buzzer Status didn't change! " + data['buzzerData']['status'] + "!=" + str(value))
		elif  configType == 'buzzerVolume':
			if data['buzzerData']['volume'] == value:
				return True
			else:
				raise Exception("Buzzer Volume didn't change! " + data['buzzerData']['volume'] + "!=" + str(value))
	return False

def Check_Config_Gateway_Not_Change(subscribe_msgs, configType , value=''):
	"""
	Description: Check Device with deviceName and deviceEUI after using change Device Name function
		[IN]: subscribe_msgs: The message received subscribe
		[IN]: configType: the EUI of device
		[IN]: timeZone: new name of device
	Return:
		[OUT]: TRUE if list devices NONE, FALSE if not. Type Boolean
	"""
	mgsID = 0
	if len(subscribe_msgs) == 0:
		# Check if no item exist in the message received after subscribe
		raise Exception("Please check connection network. No message received!")
	else:
		for pos, each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "gatewayData"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']

		if configType == 'timeZone':
			if data['timeZone'] != value:
				return  True
			else:
				raise Exception("Timezone is updated to " + str(value))
		elif configType == 'buzzerStatus':
			if data['buzzerData']['status'] != value:
				return True
			else:
				raise Exception("Buzzer Status is updated to " + str(value))
		elif  configType == 'buzzerVolume':
			if data['buzzerData']['volume'] != value:
				return TrueValid_Update_Strait
			else:
				raise Exception("Buzzer Volume is update to " + str(value))
	return False

def Valid_Update_Strait(subscribe_msgs, deviceEUI, childID, value=''):
	msgIDList = []
	if len(subscribe_msgs) == 0:
		# Check if no item exist in the message received after subscribe
		raise Exception ("Please check connection network. No message received!")
	else:
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "updateData")\
				and (msg['dataMessage']['connectivityType'] == "zigbee")\
				and (msg['dataMessage']['properties']['command'] == "updateStrait"):
				msgIDList.append(pos)

		if len(msgIDList) != 0:
			for msgID in msgIDList:
				msg = json.loads(subscribe_msgs[msgID])
				data = msg['dataMessage']['properties']['data']

				if (data['deviceEUI'] == deviceEUI) \
					and (int(data['child']) == int(childID)) \
					and (data['strait'] == 'traitOnOff'):
					findDev = True
					break
				else:
					findDev = False

			if findDev == True:
				if int(data['value']) == int(value):
					return True
				else:
					raise Exception("Cannot update TrainState of device." + data['value'] + " != " + value )
			else:
				raise Exception("Cannot Find Update Message for: " + str(deviceEUI) + ", " +  str(childID) + ", traitOnOff.\
								\n The mesage received with : " + str(data['deviceEUI']) + ", " + str(data['child']) + ', ' + str(data['strait']) )
		else:
			raise Exception("No Device Update Data")
	return False


def Get_List_Device_EUI(subscribe_msgs):
	"""
	Description: Get List Device EUI which return after publish Listdevice command
		[IN]: subscribe_msgs: The message received subscribe
	Return:
		[OUT]: List EUI of devices. Type List
	"""
	listDevEUI = []
	if len(subscribe_msgs) == 0:
		# Check if no item exist in the message received after subscribe
		raise Exception ("Please check connection network. No message received!")
	else:
		for pos,each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "listDevice"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']
		numDev	= Get_Number_Device(data)
		if numDev != 0:
			for idx in range(numDev):
				data_str = (data[idx])
				listDevEUI.append(data_str['deviceEUI'])
	if len(listDevEUI) == 0:
		raise Exception("There is no device in list")
	return listDevEUI


def Get_List_Device_EUI_ID(subscribe_msgs):
	listDevEUI = []
	listDevID = []
	if len(subscribe_msgs) == 0:
		# Check if no item exist in the message received after subscribe
 		raise Exception("Please check connection network. No message received!")
	else:
		for pos, each_msg in enumerate(subscribe_msgs):
			msg = json.loads(each_msg)
			if (msg['typeMessage'] == "requestData") and (msg['dataMessage']['properties']['command'] == "listDevice"):
				msgID = pos
				break
		msg = json.loads(subscribe_msgs[msgID])
		data = msg['dataMessage']['properties']['data']
		numDev = Get_Number_Device(data)
		if numDev != 0:
			for idx in range(numDev):
				data_str = (data[idx])
				listDevEUI.append({data_str['deviceEUI']:data_str['deviceID']})
				print (data_str['deviceEUI'])
				print(data_str['deviceID'])
	if len(listDevEUI) == 0:
		raise Exception("There is no device in list")
		respResult = ResponseResult(listDevEUI, listDevID)
		return respResult
	class ResponseResult:
	def __init__(self, name, lstID):
		self.lstEUI = lstEUI
		self.lstID = lstID

def Get_Number_Device(devList):
	"""
	Description:  Check Number of Device in Device List
		[IN] devList: list data in subscribe string
	Return :
		[OUT] : Number of devices
	"""
	if devList == None:
		return 0
	numDev	= len(devList)
	return	numDev

def Valid_DRAM_Mem(inputStr):
	strList = inputStr.split(':')
	memDRAM = strList[1].replace(' ','').replace('kB','')
	if (int(memDRAM) >= int(504660)):
		return True
	return False

def Valid_NAND_Flash(inputStr):
	mtd_list = ['mtd0', 'mtd1', 'mtd2', 'mtd3']
	mtd_dict = {
		'mtd0': '"boot"',
		'mtd1': '"kernel"',
		'mtd2': '"dtb"',
		'mtd3': '"rootfs"',
	}
	if isNotEmptyStr(inputStr):
		lines = inputStr.splitlines()[1:]
		if len(lines) == 4:
			for line in lines:
				checkMtp = False
				strList = line.split(' ')
				mtdID = strList[0].replace(':', '')
				mtdName = strList[3]
				if (mtdID in mtd_list) and (mtd_dict[mtdID] == mtdName):
					checkMtp = True
				else:
					checkMtp = False
					break

			if checkMtp == True:
				return  True
	return False

def Valid_CPU_Volume(inputStr):
	cpu_list = ['mtdblock0', 'mtdblock1', 'mtdblock2', 'mtdblock3']
	cpu_dict ={
		'mtdblock0': '64M',
		'mtdblock1': '16M',
		'mtdblock2': '16M',
		'mtdblock3': '928M'
	}
	if isNotEmptyStr(inputStr):
		lines = inputStr.splitlines()[1:]
		if len(lines) == 4:
			for line in lines:
				checkCPU = False
				strList = line.split()
				cpuID = strList[0]
				cpuName = strList[3]
				if (cpuID in cpu_list) and (cpu_dict[cpuID] == cpuName):
					checkCPU = True
				else:
					checkCPU = False

			if checkCPU == True:
				return True
	return False
def Compare_Two_Files(file1, file2):
	return  filecmp.cmp(file1,file2)

def Write_Msg_From_Str(inputStr, fileName):
	with open(fileName, 'w') as fileHandle:
		lines = inputStr.splitlines()
		for line in lines:
			fileHandle.write('%s\n' % line)

def Write_Msg_From_List(subscribe_msg, fileName):
	with open(fileName, 'w') as fileHandle:
		for item in subscribe_msg:
			fileHandle.write('%s\n' % item)

def isNotEmptyStr(strMsg):
	if strMsg and strMsg.strip():
		return  True
	return False
#subscribe_msgs = [u'{"typeMessage":"commission","dataMessage":{"properties":{"command":"addDevice","data":"success"}}}',u'{"typeMessage":"commission","dataMessage":{"properties":{"command":"addDevice","data":[{"deviceType":"typeOutlet","deviceName":"Plug","deviceLocate":"Living Room","gatewayID":"588E81FFFE5A3ED4","connectivityType":"zigbee","deviceID":"0x3FED","deviceEUI":"0x588E81FFFE5A4300","deviceInfo":{"manufacturer":"VNPT","model":"model1","hwVersion":"1.0","swVersion":"1.0"},"deviceTrait":{"deviceChild":[{"child":1,"childName":"null","traitOnOff":{"value":1,"bindDirect":"Out"},"traitEnergy":{"value":0,"bindDirect":"In"},"traitVoltage":{"value":227,"bindDirect":"In"},"traitCurrent":{"value":0,"bindDirect":"In"},"traitPower":{"value":0,"bindDirect":"In"}}],"numChild":"1"},"customData":{"data1":"null","data2":"null","data3":"null"},"_id":"sdbHv2hixGigFxFF"}]}}}']
euiDev='0x588E81FFFE5A4300'

msg_str1=[u'{"typeMessage":"commission","dataMessage":{"properties":{"command":"addDevice","data":"success"}}}']


#msg_str=[u'{"typeMessage":"commission","dataMessage":{"properties":{"command":"addDevice","data":"success"}}}', u'{"typeMessage":"commission","dataMessage":{"properties":{"command":"addDevice","data":"error"}}}']
msg_str=[u'{"typeMessage":"requestData","dataMessage":{"properties":{"command":"listDevice","data":[]}}}']
msg_str2 = [u'{"typeMessage":"requestData","dataMessage":{"properties":{"command":"listDevice","data":[{"deviceType":"typeOutlet","deviceName":"Plug","deviceLocate":"Living Room","gatewayID":"588E81FFFE5A3ED4","connectivityType":"zigbee","deviceID":"0x3FED","deviceEUI":"0x588E81FFFE5A4300","deviceInfo":{"manufacturer":"VNPT","model":"model1","hwVersion":"1.0","swVersion":"1.0"},"deviceTrait":{"deviceChild":[{"child":1,"childName":"null","traitOnOff":{"value":1,"bindDirect":"Out"},"traitEnergy":{"value":0,"bindDirect":"In"},"traitVoltage":{"value":227,"bindDirect":"In"},"traitCurrent":{"value":0,"bindDirect":"In"},"traitPower":{"value":0,"bindDirect":"In"}}],"numChild":"1"},"customData":{"data1":"null","data2":"null","data3":"null"},"_id":"sdbHv2hixGigFxFF"}]}}}']
msg_str3 = [u'{"typeMessage":"commission","dataMessage":{"properties":{"command":"addDevice","data":[{"deviceType":"typeOnOffLight","deviceName":"Plug","deviceLocate":"Living Room","gatewayID":"BC33ACFFFE3DA75E","connectivityType":"zigbee","deviceID":"0x5740","deviceEUI":"0x588E81FFFE5A3EE8","deviceInfo":{"manufacturer":"VNPT","model":"model1","hwVersion":"1.0","swVersion":"1.0"},"deviceTrait":{"deviceChild":[{"child":1,"childName":"null","traitOnOff":{"value":"null","bindDirect":"Out"}},{"child":2,"childName":"null","traitOnOff":{"value":"null","bindDirect":"Out"}},{"child":3,"childName":"null","traitOnOff":{"value":"null","bindDirect":"Out"}}],"numChild":"3"},"customData":{"data1":"null","data2":"null","data3":"null"},"_id":"BZhWovnTsfbAikBk"}]}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":1,"strait":"traitOnOff","value":0,"timeStamp":1604386351262}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":2,"strait":"traitOnOff","value":0,"timeStamp":1604386351328}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":3,"strait":"traitOnOff","value":0,"timeStamp":1604386351424}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":2,"strait":"traitOnOff","value":0,"timeStamp":1604386352249}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":1,"strait":"traitOnOff","value":0,"timeStamp":1604386352466}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":3,"strait":"traitOnOff","value":0,"timeStamp":1604386352989}}}}']
msg_str4 = [u'{"typeMessage":"commission","dataMessage":{"properties":{"command":"addDevice","data":[{"deviceType":"typeOnOffLight","deviceName":"Plug","deviceLocate":"Living Room","gatewayID":"BC33ACFFFE3DA75E","connectivityType":"zigbee","deviceID":"0x5740","deviceEUI":"0x588E81FFFE5A3EE8","deviceInfo":{"manufacturer":"VNPT","model":"model1","hwVersion":"1.0","swVersion":"1.0"},"deviceTrait":{"deviceChild":[{"child":1,"childName":"null","traitOnOff":{"value":"null","bindDirect":"Out"}},{"child":2,"childName":"null","traitOnOff":{"value":"null","bindDirect":"Out"}},{"child":3,"childName":"null","traitOnOff":{"value":"null","bindDirect":"Out"}}],"numChild":"3"},"customData":{"data1":"null","data2":"null","data3":"null"},"_id":"BZhWovnTsfbAikBk"}]}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":1,"strait":"traitOnOff","value":0,"timeStamp":1604386351262}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":2,"strait":"traitOnOff","value":0,"timeStamp":1604386351328}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":3,"strait":"traitOnOff","value":0,"timeStamp":1604386351424}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":2,"strait":"traitOnOff","value":0,"timeStamp":1604386352249}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":1,"strait":"traitOnOff","value":0,"timeStamp":1604386352466}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":3,"strait":"traitOnOff","value":0,"timeStamp":1604386352989}}}}',u'{"typeMessage":"commission","dataMessage":{"properties":{"command":"addDevice","data":[{"deviceType":"typeOnOffLight","deviceName":"Plug","deviceLocate":"Living Room","gatewayID":"BC33ACFFFE3DA75E","connectivityType":"zigbee","deviceID":"0x5740","deviceEUI":"0x588E81FFFE5A3EE8","deviceInfo":{"manufacturer":"VNPT","model":"model1","hwVersion":"1.0","swVersion":"1.0"},"deviceTrait":{"deviceChild":[{"child":1,"childName":"null","traitOnOff":{"value":"null","bindDirect":"Out"}},{"child":2,"childName":"null","traitOnOff":{"value":"null","bindDirect":"Out"}},{"child":3,"childName":"null","traitOnOff":{"value":"null","bindDirect":"Out"}}],"numChild":"3"},"customData":{"data1":"null","data2":"null","data3":"null"},"_id":"QWtdoRpAZA0XJTIF"}]}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":1,"strait":"traitOnOff","value":0,"timeStamp":1604387067833}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":1,"strait":"traitOnOff","value":0,"timeStamp":1604387068186}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":2,"strait":"traitOnOff","value":0,"timeStamp":1604387068240}}}}',u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3EE8","child":3,"strait":"traitOnOff","value":0,"timeStamp":1604387068324}}}}']
msg_str5 = [u'{"typeMessage":"updateData","dataMessage":{"connectivityType":"zigbee","properties":{"command":"updateStrait","data":{"deviceEUI":"0x588E81FFFE5A3ED1","child":1,"strait":"traitOnOff","value":1,"timeStamp":1604549771778}}}}']
#Valid_Add_Dev_With_Eui(msg_str, euiDev, 'test')
#Valid_List_Device_None(msg_str2)
#Get_List_Device_EUI(msg_str2)
#Valid_Add_More_Devices(msg_str4,3)
#Check_Device_With_DeviceName_And_EUI(msg_str2,'0x588E81FFFE5A4300','Plug')
#Valid_Update_Strait(msg_str5, '0x588E81FFFE5A3ED1', 1, 1)
str='MemTotal:         504668 kB'
str=('MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT \n \
mtdblock2  31:2    0   16M  0 disk \n \
mtdblock0  31:0    0   64M  0 disk \n \
mtdblock3  31:3    0  928M  0 disk \n \
mtdblock1  31:1    0   16M  0 disk ')
#Valid_CPU_Volume(str)
#Valid_DRAM_Mem(str)