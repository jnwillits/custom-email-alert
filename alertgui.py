# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"XPS Alert", pos = wx.DefaultPosition, size = wx.Size( 1250,625 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer36 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.Bind( wx.EVT_UPDATE_UI, self.on_update_ui )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()

	def on_update_ui( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_alert
###########################################################################

class Dialog_alert ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"XPS ECHO-Alert Notification", pos = wx.DefaultPosition, size = wx.Size( 630,694 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		bSizer301 = wx.BoxSizer( wx.VERTICAL )

		bSizer301.SetMinSize( wx.Size( -1,20 ) )
		self.staticText_alert_header = wx.StaticText( self.m_panel2, wx.ID_ANY, u"ECHO-Alert Received", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_alert_header.Wrap( -1 )

		self.staticText_alert_header.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_alert_header.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer301.Add( self.staticText_alert_header, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 50 )

		self.staticText_respond_notice = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Respond to this alert and mark it complete in Outlook.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_respond_notice.Wrap( -1 )

		bSizer301.Add( self.staticText_respond_notice, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText36 = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		bSizer301.Add( self.m_staticText36, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_caller_name_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Caller Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_caller_name_label.Wrap( -1 )

		self.staticText_caller_name_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer3.Add( self.staticText_caller_name_label, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.staticText_caller_name = wx.StaticText( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_caller_name.Wrap( -1 )

		gSizer3.Add( self.staticText_caller_name, 0, wx.ALL, 5 )


		bSizer301.Add( gSizer3, 0, wx.EXPAND, 5 )

		gSizer31 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_caller_phone_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Caller Phone:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_caller_phone_label.Wrap( -1 )

		self.staticText_caller_phone_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer31.Add( self.staticText_caller_phone_label, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.staticText_caller_phone = wx.StaticText( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_caller_phone.Wrap( -1 )

		gSizer31.Add( self.staticText_caller_phone, 0, wx.ALL, 5 )


		bSizer301.Add( gSizer31, 0, wx.EXPAND, 5 )

		gSizer32 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_caller_email_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Caller Email:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_caller_email_label.Wrap( -1 )

		self.staticText_caller_email_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer32.Add( self.staticText_caller_email_label, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.staticText_caller_email = wx.StaticText( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_caller_email.Wrap( -1 )

		gSizer32.Add( self.staticText_caller_email, 0, wx.ALL, 5 )


		bSizer301.Add( gSizer32, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline3 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer301.Add( bSizer12, 1, wx.EXPAND, 5 )

		gSizer33 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_tenant_name_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Tenant Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_tenant_name_label.Wrap( -1 )

		self.staticText_tenant_name_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer33.Add( self.staticText_tenant_name_label, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.staticText_tenant_name = wx.StaticText( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_tenant_name.Wrap( -1 )

		gSizer33.Add( self.staticText_tenant_name, 0, wx.ALL, 5 )


		bSizer301.Add( gSizer33, 0, wx.EXPAND, 5 )

		gSizer34 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_tenant_phone_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Tenant Phone:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_tenant_phone_label.Wrap( -1 )

		self.staticText_tenant_phone_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer34.Add( self.staticText_tenant_phone_label, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.staticText_tenant_phone = wx.StaticText( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_tenant_phone.Wrap( -1 )

		gSizer34.Add( self.staticText_tenant_phone, 0, wx.ALL, 5 )


		bSizer301.Add( gSizer34, 0, wx.EXPAND, 5 )

		gSizer35 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_unit_number_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Unit Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_unit_number_label.Wrap( -1 )

		self.staticText_unit_number_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer35.Add( self.staticText_unit_number_label, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.staticText_unit_number = wx.StaticText( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_unit_number.Wrap( -1 )

		gSizer35.Add( self.staticText_unit_number, 0, wx.ALL, 5 )


		bSizer301.Add( gSizer35, 0, wx.EXPAND, 5 )

		bSizer121 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline31 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer121.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer301.Add( bSizer121, 1, wx.EXPAND, 5 )

		gSizer36 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_issue_type_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Issue Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_issue_type_label.Wrap( -1 )

		self.staticText_issue_type_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer36.Add( self.staticText_issue_type_label, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.staticText_issue_type = wx.StaticText( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_issue_type.Wrap( -1 )

		gSizer36.Add( self.staticText_issue_type, 0, wx.ALL, 5 )


		bSizer301.Add( gSizer36, 0, wx.EXPAND, 5 )

		gSizer28 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_received_label = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Received:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_received_label.Wrap( -1 )

		self.staticText_received_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer28.Add( self.staticText_received_label, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.staticText_received = wx.StaticText( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_received.Wrap( -1 )

		gSizer28.Add( self.staticText_received, 0, wx.ALL, 5 )


		bSizer301.Add( gSizer28, 1, wx.EXPAND, 5 )

		gSizer281 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText25 = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		gSizer281.Add( self.m_staticText25, 0, wx.ALL, 5 )


		bSizer301.Add( gSizer281, 1, wx.EXPAND, 20 )


		bSizer27.Add( bSizer301, 0, wx.EXPAND, 5 )

		bSizer3011 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( bSizer3011, 0, wx.ALIGN_CENTER_HORIZONTAL, 15 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.richText_comment = wx.richtext.RichTextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.richText_comment.SetFont( wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer40.Add( self.richText_comment, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer27.Add( bSizer40, 1, wx.EXPAND, 5 )


		bSizer5.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.button_alert_close = wx.Button( self.m_panel2, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.button_alert_close, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_alert_close.Bind( wx.EVT_BUTTON, self.on_button_alert_close )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_alert_close( self, event ):
		event.Skip()


