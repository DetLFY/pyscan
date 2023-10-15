# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 633,766 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetTitle('PyScan扫描器')
		#self.SetIcon(wx.Icon('./miku.ico'))
		self.SetSize((633, 680))

		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"PyScan GUI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"ip探活与端口扫描" ), wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"目标ip（段）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText81 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"目标端口", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		fgSizer1.Add( self.m_staticText81, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 350,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"扫描", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"口令爆破" ), wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText31 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"攻击服务", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		m_choice1Choices = [ u"ftp", u"ssh", u"mysql", u"mssql" ]
		self.m_choice1 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		fgSizer2.Add( self.m_choice1, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"用户名字典", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 400,-1 ), wx.FLP_DEFAULT_STYLE )
		fgSizer2.Add( self.m_filePicker1, 0, wx.ALL, 5 )

		self.m_staticTexta = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"口令字典", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTexta.Wrap( -1 )
		fgSizer2.Add( self.m_staticTexta, 0, wx.ALL, 5 )
		
		self.m_filePicker2 = wx.FilePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 400,-1 ), wx.FLP_DEFAULT_STYLE )
		fgSizer2.Add( self.m_filePicker2, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"目标ip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl21, 0, wx.ALL, 5 )
		sbSizer2.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button3 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"爆破", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,200 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer6.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.ipScan )
		self.m_button3.Bind( wx.EVT_BUTTON, self.passBurte )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ipScan( self, event ):
		event.Skip()
	
	def passBurte( self, event ):
		event.Skip()
	

