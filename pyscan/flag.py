from config import *

def Banner():
    banner = fr'''
                 _____                
    ____  __  __/ ___/_________ _____ 
   / __ \/ / / /\__ \/ ___/ __ `/ __ \
  / /_/ / /_/ /___/ / /__/ /_/ / / / /
 / .___/\__, //____/\___/\__,_/_/ /_/ 
/_/    /____/
                    pyscan version: {version}
'''
    print(banner)

def flagInput(tips):
    buf = input(tips)
    return buf

def flagHelp(cmd):
    if not cmd:
        output = '''[*] 使用说明
    scanip:
        Usage: scanip <ip1>[/<submask>|-<ip2>][, ...] [<options>]

        -h                             帮助
    scanport:
        Usage: scanport <ip1>[/<submask>|-<ip2>][, ...] [<options>]
        
        -p <port1>[-<port2>][, ...]    使用指定端口
        -h                             帮助
    sshcrack:
        Usage: sshcrack <ip> [<options>...]

        -u <filepath>                  指定用户名字典
        -p <filepath>                  指定用户口令字典
        -h                             帮助
    ftpcrack:
        Usage: ftpcrack <ip> [<options>...]

        -u <filepath>                  指定用户名字典
        -p <filepath>                  指定用户口令字典
        -h                             帮助
    mysqlcrack:
        Usage: mysqlcrack <ip> [<options>...]

        -u <filepath>                  指定用户名字典
        -p <filepath>                  指定用户口令字典
        -h                             帮助
    mssqlcrack:
        Usage: mssqlcrack <ip> [<options>...]

        -u <filepath>                  指定用户名字典
        -p <filepath>                  指定用户口令字典
        -h                             帮助
    help:
        Usage: help
    exit:
        Usage: exit'''
    elif cmd == 1:
        output = '''[*] Usage: scanip <ip1>[/<submask>|-<ip2>][, ...] [<options>]

    -h                             帮助'''
    elif cmd == 2:
        output = '''[*] Usage: scanport <ip1>[/<submask>|-<ip2>][, ...] [<options>]

    -p <port1>[-<port2>][, ...]    使用指定端口
    -h                             帮助'''
    elif cmd == 3:
        output = '''[*] Usage: sshcrack <ip> [<options>...]

    -u <filepath>                  指定用户名字典
    -p <filepath>                  指定用户口令字典
    -h                             帮助'''
    elif cmd == 4:
        output = '''[*] Usage: ftpcrack <ip> [<options>...]

    -u <filepath>                  指定用户名字典
    -p <filepath>                  指定用户口令字典
    -h                             帮助'''
    elif cmd == 5:
        output = '''[*] Usage: mysqlcrack <ip> [<options>...]

    -u <filepath>                  指定用户名字典
    -p <filepath>                  指定用户口令字典
    -h                             帮助'''
    elif cmd == 6:
        output = '''[*] Usage: mssqlcrack <ip> [<options>...]

    -u <filepath>                  指定用户名字典
    -p <filepath>                  指定用户口令字典
    -h                             帮助'''
    print(output)

def flagExit():
    print("[*] Bye.")

def flagSuccess():
    print("[*] Run successfully.")

def flagError(cmd):
    print(f"[!] Command '{cmd}' not found! Please input 'help' to get the usages.")