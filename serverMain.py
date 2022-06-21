from datetime import datetime
import socket
import threading
import json
import psutilSensor as psTool

# server config
host = "127.0.0.1"
port = 9943

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.setblocking(True)
server.listen(10)

dataPack = {}
cpu = {}
mem = {}
net = {}
other = {}

def sendData(client):
    dataPack["cpu"] = cpu
    dataPack["mem"] = mem
    dataPack["net"] = net
    dataPack["other"] = other
    dataPack["info"] = psTool.getComputerInfo()
    lastCall = None
    running = True
    runFirst = True
    while running:
        try:
            if(runFirst):
                cpuUsage = 0
                runFirst = False
            else:
                cpuUsage = psTool.getCpuUsage()
            
            cpuTemp = psTool.getCpuTemp()
            cpuFreq = psTool.getCpuFreq(0)
            memUsage = psTool.getMemUsage()
            netDL  = psTool.getDLSpeed()
            netUL  = psTool.getULSpeed()
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
        
            client.sendall(json.dumps(dataPack).encode('utf-8'))

        except socket.error:
            running = False
    client.close()
    print("disconnected")

while True:
    print("wait...")
    client, addr = server.accept()
    print('Connected by ', addr[0])
    threading._start_new_thread(sendData, (client,))
