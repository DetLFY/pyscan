import GUIframe
import wx
from scanner import *

class ScanFrame(GUIframe.MyFrame1):
    def __init__(self, parent):
        GUIframe.MyFrame1.__init__(self, parent)

    def ipScan(self, event):
        self.m_textCtrl7.SetValue('')
        ip = self.m_textCtrl2.GetValue()
        liveIP = scanIP(ip)
        port = self.m_textCtrl5.GetValue()
        for i in liveIP:
            livePort = checkOpen(i, port)[0]
            self.m_textCtrl7.WriteText(livePort)
            self.m_textCtrl7.WriteText('\n')

    def passBurte(self, event):
        mode = self.m_choice1.GetSelection()
        ip = self.m_textCtrl21.GetValue()
        userPath = self.m_filePicker1.GetPath()
        passPath = self.m_filePicker2.GetPath()
        if mode == 0:
            finedic = ftpCrack(ip, userPath, passPath)
            output = "[+] 登录成功：" +  "\n[+] 登录成功：".join([f"{i}@{ip}:21，密码：{finedic[i]}" for i in finedic])
            if not finedic:
                output = f"\n[-] 登陆失败 {ip}:21"
            self.m_textCtrl7.SetValue(output)
        elif mode == 1:
            finedic = sshCrack(ip, userPath, passPath)
            output = "[+] 登录成功：" +  "\n[+] 登录成功：".join([f"{i}@{ip}:22，密码：{finedic[i]}" for i in finedic])
            if not finedic:
                output = f"\n[-] 登陆失败 {ip}:21"
            self.m_textCtrl7.SetValue(output)
        elif mode == 2:
            finedic = mysqlCrack(ip, userPath, passPath)
            output = "[+] 登录成功：" +  "\n[+] 登录成功：".join([f"{i}@{ip}:3306，密码：{finedic[i]}" for i in finedic])
            if not finedic:
                output = f"\n[-] 登陆失败 {ip}:21"
            self.m_textCtrl7.SetValue(output)
        elif mode == 3:
            finedic = mssqlCrack(ip, userPath, passPath)
            output = "[+] 登录成功：" +  "\n[+] 登录成功：".join([f"{i}@{ip}:1433，密码：{finedic[i]}" for i in finedic])
            if not finedic:
                output = f"\n[-] 登陆失败 {ip}:21"
            self.m_textCtrl7.SetValue(output)


app = wx.App(False)
frame = ScanFrame(None)
frame.Show(True)
app.MainLoop()