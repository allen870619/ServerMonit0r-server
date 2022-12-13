import psutil
import datetime
import time
import math
import MacTmp
import platform

preDL = 0
preUL = 0

# cpu
def getCpuUsage():
    # cpu usage(single)
    cpuUsage = psutil.cpu_percent(interval=1, percpu=False)
    # cpu usage free
    # cpuUsageFree = psutil.cpu_times_percent().idle
    return cpuUsage

# Only on Linux, MacOS
def getCpuTemp():
    # cpu temp
    try:
        if platform.system() == "Darwin":
            cpuTemp = MacTmp.CPU_Temp()
        else:
            cpuTemp = eval(psutil.sensors_temperatures()['coretemp'][0].current)
        return float(cpuTemp)
    except AttributeError:
        return None


def getCpuFreq(mode):
    if (mode == 0):
        return psutil.cpu_freq(percpu=False).current
    elif (mode == 1):
        return psutil.cpu_freq(percpu=False).min
    elif (mode == 2):
        return psutil.cpu_freq(percpu=False).max

# mem


def getMemUsage():
    return psutil.virtual_memory().percent

# network, Mbits


def getDLSpeed():
    global preDL
    curDL = psutil.net_io_counters().bytes_recv
    netDL = curDL - preDL
    preDL = curDL
    return netDL


def getULSpeed():
    global preUL
    curUL = psutil.net_io_counters().bytes_sent
    netUL = curUL - preUL
    preUL = curUL
    return netUL

# uptime


def getUptime():
    now = time.time()
    rawUptime = math.floor(now - psutil.boot_time())
    return datetime.timedelta(seconds=rawUptime)
