*** Settings ***
Library           MQTTLibrary
Resource          ../lib/Mqtt.txt
Resource          ../lib/Validate.txt
Resource          ../variable/mqttVariable.txt
Library           ../libpy/process_string.py    WITH NAME    PS
Library           OperatingSystem
Library           String

*** Test Cases ***
TC Change Device Name English
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And DeviceName    ${CHANGE_DEV_NAME_PATH}    ${EUI_PLUG_1}    ${DEV_NAME_PUG_1}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_EUI_And_DeviceName    ${list_dev_msg}    ${EUI_PLUG_1}    ${DEV_NAME_PUG_1}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Device Name VietNamese
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And DeviceName    ${CHANGE_DEV_NAME_PATH}    ${EUI_PLUG_1}    ${DEV_NAME_PUG_1_VN}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_EUI_And_DeviceName    ${list_dev_msg}    ${EUI_PLUG_1}    ${DEV_NAME_PUG_1_VN}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Device Name Max Length
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And DeviceName    ${CHANGE_DEV_NAME_PATH}    ${EUI_PLUG_1}    ${DEV_NAME_PUG_MAX}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_EUI_And_DeviceName    ${list_dev_msg}    ${EUI_PLUG_1}    ${DEV_NAME_PUG_MAX}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Device Name Null
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And DeviceName    ${CHANGE_DEV_NAME_PATH}    ${EUI_PLUG_1}    ${EMPTY}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_EUI_And_DeviceName    ${list_dev_msg}    ${EUI_PLUG_1}    ${EMPTY}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Device Locate English
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And Device Locate    ${CHANGE_DEV_LOC_PATH}    ${EUI_PLUG_1}    ${DEV_LOC_PUG_1}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_EUI_And_Device_Locate    ${list_dev_msg}    ${EUI_PLUG_1}    ${DEV_LOC_PUG_1}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Device Locate VietNamese
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And Device Locate    ${CHANGE_DEV_LOC_PATH}    ${EUI_PLUG_1}    ${DEV_LOC_PUG_1_VN}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_EUI_And_Device_Locate    ${list_dev_msg}    ${EUI_PLUG_1}    ${DEV_LOC_PUG_1_VN}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Device Locate Max Length
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And Device Locate    ${CHANGE_DEV_LOC_PATH}    ${EUI_PLUG_1}    ${DEV_LOC_PUG_MAX}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_EUI_And_Device_Locate    ${list_dev_msg}    ${EUI_PLUG_1}    ${DEV_LOC_PUG_MAX}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Device Locate Null
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And Device Locate    ${CHANGE_DEV_LOC_PATH}    ${EUI_PLUG_1}    ${EMPTY}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_EUI_And_Device_Locate    ${list_dev_msg}    ${EUI_PLUG_1}    ${EMPTY}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Both Device Name And Device Locate
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And DeviceName    ${CHANGE_DEV_NAME_PATH}    ${EUI_PLUG_1}    ${DEV_NAME_PUG_1}
    Publish Message With DeviceEUI And Device Locate    ${CHANGE_DEV_LOC_PATH}    ${EUI_PLUG_1}    ${DEV_LOC_PUG_1}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_DeviceName_And_Device_Locate    ${list_dev_msg}    ${EUI_PLUG_1}    ${DEV_NAME_PUG_1}    ${DEV_LOC_PUG_1}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Both Device Name And Device Locate Null
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With DeviceEUI And DeviceName    ${CHANGE_DEV_NAME_PATH}    ${EUI_PLUG_1}    ${EMPTY}
    Publish Message With DeviceEUI And Device Locate    ${CHANGE_DEV_LOC_PATH}    ${EUI_PLUG_1}    ${EMPTY}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_DeviceName_And_Device_Locate    ${list_dev_msg}    ${EUI_PLUG_1}    ${EMPTY}    ${EMPTY}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Change Child Device Name English
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message With DeviceEUI And Child Device Name    ${CHANGE_CHILD_DEV_NAME_PATH}    ${EUI_SWITCH_1}    ${CHILD_ID_1}    ${CHILD_DEV_NAME_1}
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Check_Device_With_EUI_And_ChildDeviceName    ${list_dev_msg}    ${EUI_SWITCH_1}    ${CHILD_ID_1}    ${CHILD_DEV_NAME_1}
    Publish Message    ${LIST_DEV_PATH}
    Close Network
    # Updating
    [Teardown]    Disconnect MQTT Broker
