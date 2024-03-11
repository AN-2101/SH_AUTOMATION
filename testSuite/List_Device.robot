*** Settings ***
Library           MQTTLibrary
Resource          ../lib/Mqtt.txt
Resource          ../variable/mqttVariable.txt
Library           OperatingSystem
Library           String

*** Test Cases ***
TC List Device None
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Valid_List_Device_None    ${list_dev_msg}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC List Device Not None
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message    ${LIST_DEV_PATH}
    ${list_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Valid_List_Devices    ${list_dev_msg}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Max Devices
    # Updating

TC Get List Device
    [Setup]    Connect MQTT Broker
    Close Network
    @{dev_eui_list}    Get List Device EUI
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC List Scence
    # Updating

TC List Automation
    # Updating

TC List Gateway Data
    [Setup]    Connect MQTT Broker
    Get List Device
    Close Network
    [Teardown]    Disconnect MQTT Broker
