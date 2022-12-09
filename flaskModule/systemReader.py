import platform
from cpuinfo import get_cpu_info
import psutil
import utilities as utilities

"""_summary_
osType
osVerion?
osRawVersion
pcName
platform
osRelease
machine
"""


def os_data():
    osDict = {}
    osDict["osType"] = platform.uname().system

    if platform.system() == "Darwin":
        osDict["osVerion"] = platform.mac_ver()[0]
    elif platform.system() == "Java":
        osDict["osVerion"] = platform.java_ver()[0]
    elif platform.system() == "Windows":
        osDict["osVerion"] = platform.win32_ver()[0]
    elif platform.system() == "Linux":
        osDict["osVerion"] = platform.freedesktop_os_release()["PRETTY_NAME"]

    osDict["osRawVersion"] = platform.uname().version
    osDict["pcName"] = platform.node()
    osDict["platform"] = platform.platform()
    osDict["osRelease"] = platform.uname().release
    osDict["machine"] = platform.machine()

    return utilities.emptyNullDict(osDict)


"""_summary_
arch
physicalCore
logicalCore
l1Cache?
l2Cache?
l3Cache?
hardware?
vendor?
modelName
"""


def cpu_data():
    rawList = get_cpu_info()
    cpuDict = {}
    cpuDict["arch"] = rawList["arch"]
    cpuDict["physicalCore"] = psutil.cpu_count(logical=False)
    cpuDict["logicalCore"] = psutil.cpu_count(logical=True)

    if "l1_data_cache_size" in rawList.keys():
        cpuDict["l1Cache"] = utilities.get_size(rawList["l1_data_cache_size"])
    if "l2_cache_size" in rawList.keys():
        cpuDict["l2Cache"] = utilities.get_size(rawList["l2_cache_size"])
    if "l3_cache_size" in rawList.keys():
        cpuDict["l3Cache"] = utilities.get_size(rawList["l3_cache_size"])

    if "hardware_raw" in rawList.keys():
        cpuDict["hardware"] = rawList["hardware_raw"]
    if "vendor_id_raw" in rawList.keys():
        cpuDict["vendor"] = rawList["vendor_id_raw"]
    cpuDict["modelName"] = rawList["brand_raw"]

    return utilities.emptyNullDict(cpuDict)


def memory_data():
    memDict = {}
    virtual = psutil.virtual_memory()
    memDict["ramVirtual"] = utilities.get_size(virtual.total)

    swapMem = psutil.swap_memory()
    memDict["ramSwap"] = utilities.get_size(swapMem.total)

    disk = []
    for partition in psutil.disk_partitions():
        part = {}
        part["device"] = partition.device
        part["mount"] = partition.mountpoint
        part["fstype"] = partition.fstype
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            disk.append(part)
            continue
        part["diskTotal"] = utilities.get_size(usage.total)
        part["diskUsed"] = utilities.get_size(usage.used)
        part["diskFree"] = utilities.get_size(usage.free)
        part["diskPercent"] = usage.percent
        disk.append(part)
    memDict["disk"] = disk

    return utilities.emptyNullDict(memDict)
