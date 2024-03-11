*** Settings ***
Library           MQTTLibrary
Resource          ../lib/Mqtt.txt
Resource          ../lib/Validate.txt
Resource          ../variable/mqttVariable.txt
Library           ../libpy/process_string.py    WITH NAME    PS
Library           OperatingSystem
Library           String

*** Test Cases ***
TC Config TimeZone Success 1
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Config Gateway    ${CONFIG_GATEWAY_PATH}    ${GW_CF_TYPE_Timezone}    ${TIME_ZONE_4}
    Publish Message    ${GATEWAY_DATA_PATH}
    ${gateway_data_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    PS.Check_Config_Gateway_Changed    ${gateway_data_msg}    ${GW_CF_TYPE_Timezone}    ${TIME_ZONE_4}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Config TimeZone Unsucces 1
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Config Gateway    ${CONFIG_GATEWAY_PATH}    ${GW_CF_TYPE_Timezone}    ${TIME_ZONE_1}
    Publish Message    ${GATEWAY_DATA_PATH}
    ${gateway_data_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    PS.Check_Config_Gateway_Changed    ${gateway_data_msg}    ${GW_CF_TYPE_Timezone}    ${TIME_ZONE_1}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Config Buzzer Status Success 1
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Config Gateway    ${CONFIG_GATEWAY_PATH}    ${GW_CF_TYPE_Buzz_Status}    ${BUZZ_STATUS_1}
    Publish Message    ${GATEWAY_DATA_PATH}
    ${gateway_data_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    PS.Check_Config_Gateway_Changed    ${gateway_data_msg}    ${GW_CF_TYPE_Buzz_Status}    ${BUZZ_STATUS_1}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Config Buzzer Status Unsucces 1
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Config Gateway    ${CONFIG_GATEWAY_PATH}    ${GW_CF_TYPE_Buzz_Status}    ${BUZZ_STATUS_3}
    Publish Message    ${GATEWAY_DATA_PATH}
    ${gateway_data_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    PS.Check_Config_Gateway_Changed    ${gateway_data_msg}    ${GW_CF_TYPE_Buzz_Status}    ${BUZZ_STATUS_3}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Config Buzzer Volume Success 1
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Config Gateway    ${CONFIG_GATEWAY_PATH}    ${GW_CF_TYPE_Buzz_Volume}    ${BUZZ_VOLUME_0}
    Publish Message    ${GATEWAY_DATA_PATH}
    ${gateway_data_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    PS.Check_Config_Gateway_Changed    ${gateway_data_msg}    ${GW_CF_TYPE_Buzz_Volume}    ${BUZZ_VOLUME_0}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Config Buzzer Volume Unsucces 1
    [Setup]    Connect MQTT Broker
    Close Network
    Public Message Config Gateway    ${CONFIG_GATEWAY_PATH}    ${GW_CF_TYPE_Buzz_Volume}    ${BUZZ_VOLUME_Negative}
    Publish Message    ${GATEWAY_DATA_PATH}
    ${gateway_data_msg}    Subscribe List Message    ${MIN_TIMEOUT}
    PS.Check_Config_Gateway_Not_Change    ${gateway_data_msg}    ${GW_CF_TYPE_Buzz_Volume}    ${BUZZ_VOLUME_Negative}
    Close Network
    [Teardown]    Disconnect MQTT Broker
