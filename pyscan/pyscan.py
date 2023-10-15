from config import *
from flag import *
from scanner import *

if __name__ == "__main__":
    Banner()
    while True:
        buf = flagInput("[>] ")
        result, status = scanner(buf)
        if status == 1:
            if result == 'help':
                flagHelp(0)
            elif result == 'scanip':
                flagHelp(1)
            elif result == 'scanport':
                flagHelp(2)
            elif result == 'sshcrack':
                flagHelp(3)
            elif result == 'ftpcrack':
                flagHelp(4)
            elif result == 'mysqlcrack':
                flagHelp(5)
            elif result == 'mssqlcrack':
                flagHelp(6)
            else:
                flagSuccess()
                #print(result)
        elif status == -1:
            flagExit()
            break
        else:
            flagError(result)
        