*** Settings ***
Library           MQTTLibrary
Resource          ../lib/Mqtt.txt
Resource          ../lib/Validate.txt
Resource          ../variable/mqttVariable.txt

*** Test Cases ***
TC Add Device Success 1
    [Setup]    Connect MQTT Broker
    # Publish a msg one time
    Close Network
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Device Success 2
    [Setup]    Connect MQTT Broker
    #Publish 1 - 65s - publish 2
    Close Network
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    Sleep    ${TIMEOUT_65}
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Device Success 3
    [Setup]    Connect MQTT Broker
    #Publish 1 - 90s - publish 2
    Close Network
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    Sleep    ${TIMEOUT_90}
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Device Success 4
    [Setup]    Connect MQTT Broker
    #Publish 1 - 30s - publish 2 - 45s - Publish 3
    Close Network
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    Sleep    ${AGR_TIMEOUT}
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Error    ${add_dev_msg}
    Sleep    ${TIMEOUT_45}
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Device Error 1
    [Setup]    Connect MQTT Broker
    # Publish a message when the network open: imediately
    Close Network
    # The first times publish
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    # The second times publish
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Error    ${add_dev_msg}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Device Error 2
    [Setup]    Connect MQTT Broker
    # Publish 1 - 30s - publish 2
    Close Network
    # The first times publish
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    Sleep    ${TIMEOUT_30}
    # The second times publish
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Error    ${add_dev_msg}
    Close Network
    [Teardown]    Disconnect MQTT Broker

TC Add Device Error 3
    [Setup]    Connect MQTT Broker
    # Publish 1 - 59s - publish 2
    Close Network
    # The first times publish
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Success    ${add_dev_msg}
    Sleep    ${TIMEOUT_59}
    # The second times publish
    Publish Message    ${ADD_DEV_PATH}
    ${add_dev_msg}    Subscribe Message
    Validate Msg Add Dev Error    ${add_dev_msg}
    Close Network
    [Teardown]    Disconnect MQTT Broker
