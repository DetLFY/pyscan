import os
import sys
import re
import time
from config import *

def getHostslist(reg:str):
    pattern0 = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b" # (any)ip(any)
    pattern1 = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$" # ip
    pattern2 = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s*-\s*(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$" # ip(any space)-(any space)ip
    pattern3 = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/(?:8|16|24)$" #ip/(8 or 16 or 24)
    hostslist = []
    if re.match(pattern1, reg): # 单ip
        hostslist.append(reg)
    elif re.match(pattern2, reg): # ip1 - ip2
        start, end = re.compile(pattern0).findall(reg)
        start_list = start.split('.')
        end_list = end.split('.')
        if  start_list[0:3] == end_list[0:3] and int(start_list[3]) <= int(end_list[3]): # ABC段必须相同，D段起始小于结束
            for d in range(int(start_list[3]), int(end_list[3])+1):
                hostslist.append('.'.join(start_list[0:3]) + '.' + str(d))
    elif re.match(pattern3, reg): # ip/n
        n, = re.compile(r"\b/(?:8|16|24)\b").findall(reg)
        ip, = re.compile(pattern0).findall(reg)
        ip_list = ip.split('.')
        if n == '/24':  # 扫C段
            for d in range(0, 256):
                hostslist.append('.'.join(ip_list[0:3]) + '.' + str(d))
        elif n == '/16':  # 扫B段
            for c in range(0, 256):
                for d in range(0, 256):
                    hostslist.append('.'.join(ip_list[0:2]) + '.' + str(c) + '.' + str(d))
        elif n == '/8':  # 扫A段
            for b in range(0, 256):
                for c in range(0, 256):
                    for d in range(0, 256):
                        hostslist.append('.'.join(ip_list[0:1]) + '.' + str(b) + '.' + str(c) + '.' + str(d))
    elif ',' in reg:  # 递归处理
        templist = reg.split(',')
        for temp in templist:
            temp = temp.strip()
            hostslist += getHostslist(temp)
            hostslist = sorted(list(set(hostslist)))  # 去重排序
    return hostslist

def execPing(ip:str):
    if sys.platform == 'win32' or sys.platform ==  'cygwin':
        return os.popen("ping -n 1 -w 1 " + ip + " && echo true || echo false").read()
    elif sys.platform == 'linux':
        return os.popen("ping -c 1 -w 1 " + ip + " >/dev/null && echo true || echo false").read()
    elif sys.platform == 'darwin':
        return os.popen("ping -c 1 -W 1 " + ip + " >/dev/null && echo true || echo false").read()

def runPing(hostslist:list[str]):
    livelist = []
    li = []
    for host in hostslist:
        t = Mythread(execPing, args=(host,))
        li.append(t)
        t.start()
    for t in li:
        t.join()
        if 'true' in t.getResult():
            livelist.append(t.args[0])
        #if 'true' in execPing(host):
        #    livelist.append(host)
    return livelist

def checkLive(hostslist:list[str]):
    livelist =  runPing(hostslist)
    hostdata = "[+] " +  "\n[+] ".join([f"{host}" for host in livelist])
    if len(livelist) > 0:
        output = f'''[*] 扫描结束，扫描段存活IP数量为 {len(livelist)}
[*] 存活的IP如下
{hostdata}'''
    else:
        output = f'''[*] 扫描段无存活IP'''
    return output, livelist

def scanIP(reg:str):
    time.sleep(1)
    hostlist = getHostslist(reg)
    output, livelist = checkLive(hostlist)
    print(output)
    return livelist


#print(scanIP("127.0.0.1"))