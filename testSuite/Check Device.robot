*** Settings ***
Library           MQTTLibrary
Resource          ../lib/Mqtt.txt
Resource          ../lib/Validate.txt
Resource          ../variable/mqttVariable.txt
Library           ../libpy/process_string.py    WITH NAME    PS
Library           OperatingSystem
Library           String

*** Variables ***
${NUM_DEV}        2
${DEV_EUI_PLUG}    ${EUI_PLUG_5}
${DEV_EUI_SW}     ${EUI_SW_2}
${DEV_EUI_SEN}    ${EUI_SEN_1}
${DEV_EUI_FIRE}    ${EUI_FIRE_1}
${DEV_EUI_CONTACT}    ${EUI_CONTACT_1}
${DEV_EUI_MOTION}    ${EUI_MOTION_1}

*** Test Cases ***
TC Add Plug Device Success
    [Setup]    Connect MQTT Broker
    Close Network
    Add Device
    ${payload_msg}    Subscribe List Message    ${MAX_TIMEOUT}
    ${result}    PS.Valid_Add_Dev_With_Eui    ${payload_msg}    ${DEV_EUI_PLUG}    ${DEV_TYPE_Plug}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Switch Device Success
    [Setup]    Connect MQTT Broker
    Close Network
    Add Device
    ${payload_msg}    Subscribe List Message    ${MAX_TIMEOUT}
    ${result}    PS.Valid_Add_Dev_With_Eui    ${payload_msg}    ${DEV_EUI_SW}    ${DEV_TYPE_Light}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Sensor Device Success
    [Setup]    Connect MQTT Broker
    Close Network
    Add Device
    ${payload_msg}    Subscribe List Message    ${MAX_TIMEOUT}
    ${result}    PS.Valid_Add_Dev_With_Eui    ${payload_msg}    ${DEV_EUI_SEN}    ${DEV_TYPE_Sensor}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Motion Device Success
    [Setup]    Connect MQTT Broker
    Close Network
    Add Device
    ${payload_msg}    Subscribe List Message    ${MAX_TIMEOUT}
    ${result}    PS.Valid_Add_Dev_With_Eui    ${payload_msg}    ${DEV_EUI_MOTION}    ${DEV_TYPE_Motion}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Contact Device Success
    [Setup]    Connect MQTT Broker
    Close Network
    Add Device
    ${payload_msg}    Subscribe List Message    ${MAX_TIMEOUT}
    ${result}    PS.Valid_Add_Dev_With_Eui    ${payload_msg}    ${DEV_EUI_CONTACT}    ${DEV_TYPE_Contact}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Fire Device Success
    [Setup]    Connect MQTT Broker
    Close Network
    Add Device
    ${payload_msg}    Subscribe List Message    ${MAX_TIMEOUT}
    ${result}    PS.Valid_Add_Dev_With_Eui    ${payload_msg}    ${DEV_EUI_FIRE}    ${DEV_TYPE_Fire}
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add More Devices In One Times
    [Setup]    Connect MQTT Broker
    Close Network
    Add Device
    ${add_msg}    Subscribe List Message    ${MAX_TIMEOUT}
    PS.Valid_Add_More_Devices    ${add_msg}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add More Devices
    [Setup]    Connect MQTT Broker
    Close Network
    Check List Device Not Empty
    Add Device
    ${add_msg}    Subscribe List Message    ${MAX_TIMEOUT}
    PS.Valid_Add_More_Devices    ${add_msg}
    Close Network
    [Teardown]    Disconnect MQTT Broker
