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

    
def Convert_New(filePathIN, filePathOut ):
	with open(filePathIN) as json_file:
		datatoDict = json.load(json_file)  # Convert Data to Dict
	Write_Dict_To_Json_File(datatoDict, filePathOut)



def Convert_New_File():
	filePathIN = "../testOutput_http/01.TestListDev.txt"
	filePathOut = "../testOutput_mqtt" + "/" + "01.TestListDev" + ".json"
	with open(filePathIN) as json_file:
		datatoDict = json.load(json_file)
		responData = datatoDict['responseData']
		responDict = json.loads(responData)
		#print(responDict)
	with open(filePathOut, 'w') as fileHandle:
		json.dump(responDict, fileHandle, indent=4)


Convert_New_File()
#Convert_New(filePathIn, filePathOut)

#Convert_All_File_In_Folder()
#Get_Body_All_File_In_Folder()

#Get_Body_One_File_New(fileName)