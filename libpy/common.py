#!/usr/bin/env python
"""
	@file : common.py
	@description: Library for common function
    @author : IoT-HEC, VNPT-Technology
"""
import filecmp
import json
import os

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

def isNotEmptyList(sub_list_msg):
	if len(sub_list_msg) == 0:
		return False
	return True

def Write_Dict_To_Json_File(msgDict, fileName):
	with open(fileName, 'w') as fileHandle:
		json.dump(msgDict, fileHandle, indent=4)

def Get_Body_Command_Msg(fileIN):
	resDict = {}
	with open(fileIN) as json_file:
		data = json.load(json_file)  # json.load : using for file : convert data dic file to Json
		conData = data['pc']['m2m:sgn']['nev']['rep']['m2m:cin']['con']
		conDict = json.loads(conData)  #json.loads: using for string: convert string dic to Json
		responData = conDict['responseData']
		responDict = json.loads(responData) #json.loads: using for string: convert string dic to Json
		if (conDict['recordId'] == responDict['requestID'] ):
			resDict = responDict
		else:
			raise Exception("Record ID is not equal Request ID")
	return resDict

def Get_Body_Telemetry_Msg(fileIN):
	with open(fileIN) as json_file:
		data = json.load(json_file)  # json.load : using for file : convert data file to Json
		conData = data['pc']['m2m:sgn']['nev']['rep']['m2m:cin']['con']
		conDict = json.loads(conData)  # json.loads: using for string: convert string to Json
	return conDict

def Convert_Output_To_API(filePathIN, filePathOut):
	fileName = False
	if filePathIN.find("update") > 0:
		msgDict = Get_Body_Telemetry_Msg(filePathIN)
		fileName = True
	elif filePathIN.find("res") > 0:
		msgDict = Get_Body_Command_Msg(filePathIN)
		fileName = True
	else:
		fileName = False

	if fileName == True:
		Write_Dict_To_Json_File(msgDict, filePathOut)

def Get_Body_All_File_In_Folder():
	dirFile = "../testOutput_http"
	dirFileOut = "../testOutput_mqtt"

	for file in os.listdir(dirFile):
		if file.endswith(".txt"):
			filePathIn = dirFile + "/" + file
			print(filePathIn)
			#filePathOut = dirFileOut + "/" + file.split(".json")[0] + ".txt"
			filePathOut = dirFileOut + "/" + file.split(".txt")[0] + ".json"
			Convert_Output_To_API(filePathIn, filePathOut)


def Get_Body_One_File(fileName):
	#fileName = "02. resRemoveDevice"
	filePathIn = "../testOutput_http" + "/" + fileName + ".txt"
	filePathOut = "../testOutput_mqtt" + "/" + fileName + ".json"
	Convert_Output_To_API(filePathIn, filePathOut)


def Convert_Json_Data_To_Json_Postman(filePathIN):
	headerDict = {
		"commandId": "update",
		"name": "update",
		"data": "",
		"commandType": "Control",
		"recordId": "1587356365924"
	}
	conStrDict = {
		"con": ""
	}

	postmanDict = {
		"m2m:cin": {
			"cnf": "text/plains:0",
			"con": ""
		}
	}

	with open(filePathIN) as json_file:
		datatoDict = json.load(json_file)  # Convert Data to Dict
		DictToStr = json.dumps(datatoDict)  # Convert Data Dict to String

	headerDict["data"] = DictToStr  # Gan data string cho keyword Data cua Header
	headerStr = json.dumps(headerDict)  # Convert Header dictionary to String
	postmanDict["m2m:cin"]["con"] = headerStr
	return postmanDict

def Convert_To_HTTP(filePathIN, filePathOut):
	msgDict = Convert_Json_Data_To_Json_Postman(filePathIN)
	Write_Dict_To_Json_File(msgDict, filePathOut)

def Convert_All_File_In_Folder():
	dirFile = "../testData_mqtt"
	dirFileOut = "../testData_http"

	for file in os.listdir(dirFile):
		if file.endswith(".json"):
			filePathIn = dirFile + "/" + file
			filePathOut = dirFileOut + "/" + file.split(".json")[0] + ".txt"
			Convert_To_HTTP(filePathIn, filePathOut)

def Get_Body_One_File_New(fileName):
	#fileName = "02. resRemoveDevice"
	filePathIn = "../testOutput_http" + "/" + fileName + ".txt"
	filePathOut = "../testOutput_mqtt" + "/" + fileName + ".json"
	with open(filePathIn) as json_file:
		data = json.load(json_file)  # json.load : using for file : convert data file to Json
		responData = data['responseData']
		responDict = json.loads(responData)
	with open(filePathOut, 'w') as fileHandle:
		json.dump(responDict, fileHandle, indent=4)
   


#Convert_All_File_In_Folder()
Get_Body_All_File_In_Folder()

#Get_Body_One_File_New(fileName)