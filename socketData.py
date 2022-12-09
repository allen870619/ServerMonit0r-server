from datetime import datetime
import socket
import json
import psutilSensor as psTool

def socket_send_data(client):
    dataPack = {}
    cpu = {}
    mem = {}
    net = {}
    other = {}
    lastCall = None
    running = True
    runFirst = True
    
    while running:
        try:
            if (runFirst):
                cpuUsage = 0
                runFirst = False
            else:
                cpuUsage = psTool.getCpuUsage()

            cpuTemp = psTool.getCpuTemp()
            cpuFreq = psTool.getCpuFreq(0)
            memUsage = psTool.getMemUsage()
            netDL = psTool.getDLSpeed()
            netUL = psTool.getULSpeed()
            upTime = psTool.getUptime()
            if lastCall != None:
                timeDelta = (datetime.now() - lastCall).seconds
            else:
                timeDelta = 1
            lastCall = datetime.now()

            # json packet
            cpu["cpuUsage"] = cpuUsage
            cpu["cpuTemp"] = cpuTemp
            cpu["cpuFreq"] = cpuFreq
            mem["memUsage"] = memUsage
            net["netDownload"] = netDL/timeDelta
            net["netUpload"] = netUL/timeDelta
            other["upTime"] = str(upTime)
            dataPack["cpu"] = cpu
            dataPack["mem"] = mem
            dataPack["net"] = net
            dataPack["other"] = other
            dataPack["info"] = psTool.getComputerInfo()

            client.sendall(json.dumps(dataPack).encode('utf-8'))

        except socket.error:
            running = False
    client.close()
    print("disconnected", flush=True)
