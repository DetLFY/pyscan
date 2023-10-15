import socket
import re
import time
from concurrent.futures import ThreadPoolExecutor
from config import *

temp_PORTList = PORTList.copy()

def getPortslist(reg:str):
    pattern0 = r"\b([0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])\b"
    pattern1 = r"^([0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$"
    pattern2 = r"^([0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])\s*-\s*([0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$"
    postslist = []
    if re.match(pattern1, reg):  # 单port
        postslist.append(int(reg))
    elif re.match(pattern2, reg): # port1 - port2
        start, end = re.compile(pattern0).findall(reg)
        start_port = int(start)
        end_port = int(end)
        if start_port <= end_port:
            for port in range(start_port, end_port+1):
                postslist.append(port)
    elif ',' in reg:  # 递归处理
        templist = reg.split(',')
        for temp in templist:
            temp = temp.strip()
            postslist += getPortslist(temp)
            postslist = sorted(list(set(postslist)))  # 去重排序
    return postslist

def checkPort(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))

    try:
        sock.send(b'GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n')
        r = sock.recv(256)
    except Exception:   # 异常捕获，主要针对端口未开放的发包超时和防火墙拦截
        return False

    if port not in temp_PORTList.keys():
        if b'HTTP' in r:
            temp_PORTList[port] = 'http'
        elif b'SSH' in r:
            temp_PORTList[port] = 'ssh'
        elif b'mysql' in r:
            temp_PORTList[port] = 'mysql'
        elif b'MSSQL Serve' in r:
            temp_PORTList[port] = 'mssql'
        elif b'220' or b'331' in r:
            temp_PORTList[port] = 'ftp'

    if result == 0:
        return True
    else:
        return False


def doScanPort(ip:str, mode:bool=False, portslist:list[int]=[]):
    openportslist = []
    li = []
    #semaphore = threading.BoundedSemaphore(128)
    if not mode:  # 扫全部
        for port in range(65536):
            t = Mythread(checkPort, args=(ip, port))
            li.append(t)
        for i in range(0, 65536, 2048):
            for t in li[i:i+2048]:
                t.start()
            for t in li[i:i+2048]:
                t.join()
                if t.getResult():
                    openportslist.append(t.args[1])
            #if checkPort(ip, port):
            #    openportslist.append(port)
    else:  # 扫特定
        for port in portslist:
            t = Mythread(checkPort, args=(ip, port))
            li.append(t)
        for i in range(0, len(portslist), 2048):
            for t in li[i:i+2048]:
                t.start()
            for t in li[i:i+2048]:
                t.join()
                if t.getResult():
                    openportslist.append(t.args[1])
    return openportslist

def checkOpen(ip:str, args:str):
    if args == '':
        openportslist = doScanPort(ip)
    else:
        openportslist = doScanPort(ip, True, getPortslist(args))
    for port in range(65536):
        if port not in temp_PORTList.keys():
            temp_PORTList[port] = "unknown service"
    portdata = "[+] " +  "\n[+] ".join([f"{port}" + f" {temp_PORTList[port]}" for port in openportslist])
    if len(openportslist) > 0:
        output = f'''[*] {ip} 扫描结束，开放的端口数量为 {len(openportslist)}
[*] 开放的端口及相应服务如下
{portdata}'''
    else:
        output = f'''[*] {ip} 未探测到开放的端口'''
    return output, openportslist

def scanPort(ip:str, reg:str):
    output, openportslist = checkOpen(ip, reg)
    print(output)
    return openportslist


#print(scanPort("127.0.0.1", "1-10000"))