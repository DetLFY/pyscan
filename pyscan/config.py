import threading

version = "1.0.0"
Userdict = {
    "ftp":        {"anonymous", "ftp", "admin", "www", "web", "root", "db", "wwwroot", "data"},
	"mysql":      {"root", "mysql"},
	"mssql":      {"sa", "sql"},
	"ssh":        {"root", "admin", "user"},
}
Passwords = [ "123456", "admin", "admin123", "root", "", "pass123", "pass@123", "password", "123123", "654321", "111111", "123", "1", "admin@123", "Admin@123", "admin123!@#", "{user}", "{user}1", "{user}111", "{user}123", "{user}@123", "{user}_123", "{user}#123", "{user}@111", "{user}@2019", "{user}@123#4", "P@ssw0rd!", "P@ssw0rd", "Passw0rd", "qwe123", "12345678", "test", "test123", "123qwe", "123qwe!@#", "123456789", "123321", "666666", "a123456.", "123456~a", "123456!a", "000000", "1234567890", "8888888", "!QAZ2wsx", "1qaz2wsx", "abc123", "abc123456", "1qaz@WSX", "a11111", "a12345", "Aa1234", "Aa1234.", "Aa12345", "a123456", "a123123", "Aa123123", "Aa123456", "Aa12345.", "sysadmin", "system", "1qaz!QAZ", "2wsx@WSX", "qwe123!@#", "Aa123456!", "A123456s!", "sa123456", "1q2w3e", "Charge123", "Aa123456789", "123@123.com" ]
PORTList = {
    20: "ftp (data)",
    21: "ftp (control)",       
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    67: "bootstrap protocol server",
    68: "bootstrap protocol client",
    69: "tftp",
    79: "finger",
    80: "http",     
    109: "pop2",
    110: "pop3", 
    111: "rpc",
    119: "nntp",
	135: "findnet",    
	139: "netbios", 
    143: "imap",  
    161: "snmp",
    443: "https",  
	445: "smb",    
    554: "rtsp", 
    1080: "socks",
	1433: "mssql",       
	1521: "oracle",      
	3306: "mysql",      
	3389: "rdp",       
	5432: "psql",        
	6379: "redis",       
	9000: "fcgi",       
	11211: "mem",         
	27017: "mgo",         
}
Outputfile = "result.txt"
IsSave = True

class Mythread(threading.Thread):  # 封装threading.Thread
    def __init__(self, func, args=()):
        super(Mythread, self).__init__()
        self.func=func
        self.args=args
    def run(self):  # 重写run方法，使之获取函数返回值
        self.result = self.func(*self.args)
    def getResult(self):
        try:
            return self.result
        except Exception:
            return None