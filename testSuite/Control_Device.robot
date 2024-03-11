*** Settings ***
Library           MQTTLibrary
Resource          ../lib/Mqtt.txt
Resource          ../lib/Validate.txt
Resource          ../variable/mqttVariable.txt
Library           ../libpy/process_string.py    WITH NAME    PS
Library           OperatingSystem
Library           String

*** Variables ***
${DEV_EUI_PLUG}    ${EUI_PLUG_5}
${DEV_EUI_SW}     ${EUI_SW_1_ThoaLT}
@{CHILD_ID_LIST}    1    2    3

*** Test Cases ***
TC Control Device On Plug
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Control Device    ${CONTROL_DEVICE_PATH}    ${DEV_EUI_PLUG}    ${CHILD_ID_LIST}[0]    On
    ${control_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Valid_Update_Strait    ${control_dev_msg}    ${DEV_EUI_PLUG}    ${CHILD_ID_LIST}[0]    1
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Control Device Off Plug
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Control Device    ${CONTROL_DEVICE_PATH}    ${DEV_EUI_PLUG}    ${CHILD_ID_LIST}[0]    Off
    ${control_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Valid_Update_Strait    ${control_dev_msg}    ${DEV_EUI_PLUG}    ${CHILD_ID_LIST}[0]    0
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Control Device On Switch Child 1
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Control Device    ${CONTROL_DEVICE_PATH}    ${DEV_EUI_SW}    ${CHILD_ID_LIST}[0]    On
    ${control_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Valid_Update_Strait    ${control_dev_msg}    ${DEV_EUI_SW}    ${CHILD_ID_LIST}[0]    1
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Control Device Off Switch Child 1
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Control Device    ${CONTROL_DEVICE_PATH}    ${DEV_EUI_SW}    ${CHILD_ID_LIST}[0]    Off
    ${control_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    ${result}    PS.Valid_Update_Strait    ${control_dev_msg}    ${DEV_EUI_SW}    ${CHILD_ID_LIST}[0]    0
    Should Be True    ${result}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Control Device On Three Child
    [Setup]    Connect MQTT Broker
    Close Network
    FOR    ${item}    IN    @{CHILD_ID_LIST}
        Public Message Control Device    ${CONTROL_DEVICE_PATH}    ${DEV_EUI_SW}    ${item}    On
        ${control_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
        ${result}    PS.Valid_Update_Strait    ${control_dev_msg}    ${DEV_EUI_SW}    ${item}    1
        Should Be True    ${result}
    END
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Control Device Off Three Child
    [Setup]    Connect MQTT Broker
    Close Network
    FOR    ${item}    IN    @{CHILD_ID_LIST}
        Public Message Control Device    ${CONTROL_DEVICE_PATH}    ${DEV_EUI_SW}    ${item}    Off
        ${control_dev_msg}    Subscribe List Message    ${MIN_TIMEOUT}
        ${result}    PS.Valid_Update_Strait    ${control_dev_msg}    ${DEV_EUI_SW}    ${item}    0
        Should Be True    ${result}
    END
    Close Network
    [Teardown]    Disconnect MQTT Broker
