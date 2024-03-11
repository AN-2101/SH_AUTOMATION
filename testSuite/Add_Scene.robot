*** Settings ***
Library           MQTTLibrary
Resource          ../lib/Mqtt.txt
Resource          ../lib/Validate.txt
# Resource          ../libpy/process_string.py with PS

*** Test Cases ***
TC FUNC_65
    [Setup]    Connect MQTT Broker
    Close Network
    Publish Message Add Scene
    ${add_scene_msg_res}    Subscribe Topic Recive Command
    Validate Msg Add Scene Success    ${add_scene_msg_res}
    [Teardown]    Disconnect MQTT Broker
