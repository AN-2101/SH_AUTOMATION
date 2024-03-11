*** Settings ***
Library           MQTTLibrary
Resource          ../lib/Mqtt.txt
Resource          ../lib/Validate.txt
Resource          ../variable/mqttVariable.txt
Library           ../libpy/process_string.py    WITH NAME    PS

*** Variables ***
${DEV_EUI}        ${EUI_SW_1}
${DEV_ID}         ${ID_SW_1}
@{DEV_EUI_LIST}    ${EUI_PLUG_1}    ${EUI_PLUG_2}    ${EUI_PLUG_3}    ${EUI_PLUG_4}

*** Test Cases ***
TC Remove Device Success with EUI
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With EUI    ${REMOVE_DEV_PATH}    ${DEV_EUI}
    ${remove_dev_msg}    Subscribe Message
    Validate Remove Device Success    ${remove_dev_msg}    ${DEV_EUI}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Remove Device Success with EUI and ID
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message With EUI and ID    ${REMOVE_DEV_PATH}    ${DEV_EUI}    ${DEV_ID}
    ${remove_dev_msg}    Subscribe Message
    Validate Remove Device Success with EUI and ID    ${remove_dev_msg}    ${DEV_EUI}    ${DEV_ID}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Remove All Devices
    [Setup]    Connect MQTT Broker
    Close Network
    @{dev_eui_list}    Get List Device EUI
    FOR    ${item}    IN    @{dev_eui_list}
        Log to console    ${item}
        Publish Message With EUI    ${REMOVE_DEV_PATH}    ${item}
    END
    Check List Device Empty
    Close Network
    [Teardown]    Disconnect MQTT Broker
