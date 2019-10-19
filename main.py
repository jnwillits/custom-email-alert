# !/usr/bin/env python
"""
Jeff's XPS Email Alert Utility

This is a custom and single-purpose utility that displays an alert
in response to receipt of an email with a title of 'Notification
message'. The alert will only display when the email has not been
categorized.

The messages are computer-generated from phone call data taken at
a call center. They are in a consistent HTML format. This proram
uses regular expressions to extract only the most relevant data 
and include them on the alert dialog. 

The program is to be periodically triggered using the Windows Task
Scheduler and is expected to be used in conjunction with an Outlook
rule that alerts to emails with a 'Notification message' title. If
such an alert is closed without categorizing the email, this alert
will be triggered at a later time to assure the email is categorized.

When no emails are found that trigger the alert dialog, this shuts
down automatically.

"""

import re
import sys

import win32com.client as win32
import wx

import alertgui

subj = 'Notification message'
alert_shown = False


class DialogAlert(alertgui.Dialog_alert):
    def __init__(self, parent):
        alertgui.Dialog_alert.__init__(self, parent)

        self.staticText_caller_name.SetLabel(caller_name)
        self.staticText_caller_phone.SetLabel(caller_phone)
        self.staticText_caller_email.SetLabel(caller_email)
        self.staticText_tenant_name.SetLabel(tenant_name)
        self.staticText_tenant_phone.SetLabel(tenant_phone)
        self.staticText_unit_number.SetLabel(unit_number)
        self.staticText_issue_type.SetLabel(issue_type)
        self.staticText_received.SetLabel(f'{receipt_time}')
        self.richText_comment.AppendText(comments)

    def on_button_alert_close(self, event):
        self.Close()
        sys.exit()


class Interface(alertgui.MainFrame):
    def __init__(self, parent):
        alertgui.MainFrame.__init__(self, parent)


if __name__ == '__main__':
    outlook = win32.Dispatch(
        "Outlook.Application").GetNamespace("MAPI")
    app = wx.App(False)
    frame = Interface(None)
    frame.Show(False)
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    for message in messages:
        if not alert_shown:
            if message.Subject == subj and message.Categories == '':
                receipt_time = message.ReceivedTime
                content = message.Body
                caller_name = re.findall(
                    r'\bCaller\r\n\r\n\t(.*)\r\n\r\nPhone\b', content)[0]
                caller_phone = re.findall(
                    r'\bNumber\r\n\r\n\t(.*)\r\n\r\nEmail\b', content)[0]
                caller_email = re.findall(
                    r'\bEmail\r\n\r\n\t(.*)\t\r\n\tCall Time\b', content)[0]
                tenant_name = re.findall(
                    r'\bName\r\n\r\n\t(.*)\r\n\r\nPhone Number\b', content)[0]
                tenant_phone = re.findall(
                    r'\bNumber\r\n\r\n\t(.*)\r\n\r\n\tSpace\b', content)[0]
                unit_number = re.findall(
                    r'\bSpace #\r\n\r\n\t(.*)\r\n\r\nIssue\b', content)[0]
                issue_type = re.findall(
                    r'\bType\r\n\r\n\t(.*)\r\n\r\n\t\r\nAdditional\b', content)[0]
                comments = re.findall(
                    r'\bComments\r\n\r\n. (.*) \r\n\r\n\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n <https\b', content)[0]
                dlg = DialogAlert(None)
                dlg.Show(True)
                alert_shown = True

    if not alert_shown:
        sys.exit()

    app.MainLoop()
