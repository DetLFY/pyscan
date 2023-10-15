from scanIP import *
from scanPort import *
from ssh import *
from ftp import *
from mysql import *
from mssql import *




def scanner(buf:str):
    buf = buf.strip()
    if ' ' in buf:
        cmd, args = buf.split(' ', 1)
    else:
        cmd, args = buf, ''
    cmd = cmd.strip()
    args = args.strip()
    if cmd == 'scanip':
        if args == '-h':
            return 'scanip', 1
        livelist = scanIP(args)    
        return livelist, 1
    elif cmd == 'scanport':
        openportsdicts = dict()
        if args == '-h':
            return 'scanport', 1
        if '-p' in args:
          arg1, arg2 = args.split('-p', 1)
        else:
            arg1, arg2 = args, ''
        arg1 = arg1.strip()
        arg2 = arg2.strip()
        iplist = getHostslist(arg1)
        iplist = runPing(iplist)
        for ip in iplist:
            openportslist = scanPort(ip, arg2)
            openportsdicts[ip] = openportslist
        return openportsdicts, 1
    elif cmd == 'sshcrack':
        userdict = dict()
        if args == '-h':
            return 'sshcrack', 1
        if '-u' in args or '-p' in args:
            if '-u' in args and '-p' in args:
                arg1, temp = args.split('-u')
                arg2, arg3 = temp.split('-p')
            elif '-u' in args and '-p' not in args:
                arg1, arg2 = args.split('-u')
                arg3 = ''
            elif '-u' not in args and '-p' in args:
                arg1, arg3= args.split('-p')
                arg2 = ''
        else:
            arg1, arg2, arg3 = args, '', ''
        arg1 = arg1.strip()
        arg2 = arg2.strip()
        arg3 = arg3.strip()
        if checkPort(arg1, 22):    # 22端口开放测试
            userdict = sshCrack(arg1, arg2, arg3)
        return userdict, 1
    elif cmd == 'ftpcrack':
        userdict = dict()
        if args == '-h':
            return 'ftpcrack', 1
        if '-u' in args or '-p' in args:
            if '-u' in args and '-p' in args:
                arg1, temp = args.split('-u')
                arg2, arg3 = temp.split('-p')
            elif '-u' in args and '-p' not in args:
                arg1, arg2 = args.split('-u')
                arg3 = ''
            elif '-u' not in args and '-p' in args:
                arg1, arg3= args.split('-p')
                arg2 = ''
        else:
            arg1, arg2, arg3 = args, '', ''
        arg1 = arg1.strip()
        arg2 = arg2.strip()
        arg3 = arg3.strip()
        if checkPort(arg1, 21):    # 21端口开放测试
            userdict = ftpCrack(arg1, arg2, arg3)
        return userdict, 1
    elif cmd == 'mysqlcrack':
        userdict = dict()
        if args == '-h':
            return 'mysqlcrack', 1
        if '-u' in args or '-p' in args:
            if '-u' in args and '-p' in args:
                arg1, temp = args.split('-u')
                arg2, arg3 = temp.split('-p')
            elif '-u' in args and '-p' not in args:
                arg1, arg2 = args.split('-u')
                arg3 = ''
            elif '-u' not in args and '-p' in args:
                arg1, arg3= args.split('-p')
                arg2 = ''
        else:
            arg1, arg2, arg3 = args, '', ''
        arg1 = arg1.strip()
        arg2 = arg2.strip()
        arg3 = arg3.strip()
        if checkPort(arg1, 3306):    # 3306端口开放测试
            userdict = mysqlCrack(arg1, arg2, arg3)
        return userdict, 1
    elif cmd == 'mssqlcrack':
        userdict = dict()
        if args == '-h':
            return 'mssqlcrack', 1
        if '-u' in args or '-p' in args:
            if '-u' in args and '-p' in args:
                arg1, temp = args.split('-u')
                arg2, arg3 = temp.split('-p')
            elif '-u' in args and '-p' not in args:
                arg1, arg2 = args.split('-u')
                arg3 = ''
            elif '-u' not in args and '-p' in args:
                arg1, arg3= args.split('-p')
                arg2 = ''
        else:
            arg1, arg2, arg3 = args, '', ''
        arg1 = arg1.strip()
        arg2 = arg2.strip()
        arg3 = arg3.strip()
        if checkPort(arg1, 1433):    # 1433端口开放测试
            userdict = mssqlCrack(arg1, arg2, arg3)
        return userdict, 1
    elif cmd == 'exit':
        return 'exit', -1
    elif cmd == 'help':
        return 'help', 1
    else:
        return cmd, 0

#print(scanner("scanport 127.0.0.1, 192.168.64.1 -p 22"))
#print(scanner("exit"))
#print(scanner("sshcrack 192.168.64.3"))