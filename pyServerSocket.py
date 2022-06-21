import socket
import threading
from time import sleep
import datetime
import time
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

# psutil variable
preUp = 0
preDw = 0

dataPack = {}
cpu = {}
mem = {}
net = {}
other = {}

def sendData(client):
    global preDw, preUp

    dataPack["cpu"] = cpu
    dataPack["mem"] = mem
    dataPack["net"] = net
    dataPack["other"] = other
    dataPack["info"] = psTool.getComputerInfo()

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
    
            # json packet
            cpu["cpuUsage"] = cpuUsage
            cpu["cpuTemp"] = cpuTemp
            cpu["cpuFreq"] = cpuFreq
            mem["memUsage"] = memUsage
            net["netDownload"] = netDL
            net["netUpload"] = netUL
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
