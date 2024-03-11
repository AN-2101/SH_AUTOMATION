*** Settings ***
Library           BuiltIn
Library           ../libpy/process_string.py    WITH NAME    PS
Resource          ../lib/SSH.txt
Resource          ../variable/mqttVariable.txt

*** Variables ***
${processor}      processor    : 0
${fileIN}         testData/cpuInfo.txt
${fileOUT}        testData/cpuInfoOut.txt
${fileZigbeeIN}    testData/zigbeeInfo.txt
${fileZigbeeOut}    testData/zigbeeInfoOut.txt

*** Test Cases ***
TC Console Interface 1
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    ${output}    Execute Command    cat /sys/devices/system/cpu/*/cpufreq/cpuinfo_cur_freq
    Should be equal    ${output}    528000
    #Log to console    ${output}
    Close Connection

TC Console Interface 2
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    ${output}    Execute Command    cat /proc/cpuinfo
    PS.Write_Msg_From_Str    ${output}    ${fileOUT}
    ${result}    PS.Compare_Two_Files    ${fileIN}    ${fileOUT}
    Should Be True    ${result}
    Close Connection

TC DRAM
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    ${output}    Execute Command    cat /proc/meminfo | grep 'MemTotal:'
    ${result}    PS.Valid_DRAM_Mem    ${output}
    Should Be True    ${result}
    #Log to console    ${output}
    Close Connection

TC NAND Flash 1
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    #Write    cat /proc/mtd | grep mtd0
    ${output}    Execute Command    cat /proc/mtd
    ${result}    PS.Valid_NAND_Flash    ${output}
    Should Be True    ${result}
    Log to console    ${output}
    Close Connection

TC NAND Flash 2
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    #Write    cat /proc/mtd | grep mtd0
    ${output}    Execute Command    lsblk
    ${result}    PS.Valid_CPU_Volume    ${output}
    Should Be True    ${result}
    Log to console    ${output}
    Close Connection

TC Wifi 1
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    Write    ifconfig wlan0 | grep 'wlan0'
    ${output}    Read    delay=2
    Log to console    ${output}
    Close Connection

TC Wifi 2
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    Write    wpa_cli scan_results
    ${output}    Read    delay=2
    Log to console    ${output}
    Close Connection

TC Ethernet 1
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    Write    ifconfig eth0 | grep 'eth0'
    ${output}    Read    delay=2
    Log to console    ${output}
    Close Connection

TC Ethernet 2
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    Write    ifconfig eth0 | grep 'inet addr'
    ${output}    Read    delay=2
    Log to console    ${output}
    Close Connection

TC Zigbee Chip
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    Write    killall node
    Write    cd /home/root/FirmwareGateway/gateway/adapter/zigbee-adapter/bin
    Write    chmod +x siliconlabsgateway
    Write    ./siliconlabsgateway -n 0 -p /dev/ttymxc1
    ${output}    Read    delay=2
    PS.Write_Msg_From_Str    ${output}    ${fileZigbeeOut}
    ${result}    PS.Compare_Two_Files    ${fileZigbeeOut}    ${fileZigbeeIN}
    Log to console    ${output}
    Close Connection

TC LED 1
    Create SSH Session    ${HOST}    ${USER}    ${PASS}
    ${output}    Execute Command    echo 1 > /sys/class/gpio/gpio5/value
    Sleep    2
    ${output}    Execute Command    echo 0 > /sys/class/gpio/gpio5/value
    Sleep    2
    ${output}    Execute Command    echo 1 > /sys/class/gpio/gpio6/value
    Sleep    2
    ${output}    Execute Command    echo 0 > /sys/class/gpio/gpio6/value
    Sleep    2
    ${output}    Execute Command    echo 1 > /sys/class/gpio/gpio7/value
    Sleep    2
    ${output}    Execute Command    echo 0 > /sys/class/gpio/gpio7/value
    Sleep    2
    Log to console    ${output}
    Close Connection
