# !/usr/bin/env python
"""
Jeff's XPS Email Alert Utility

This is a custom and single-purpose utility that displays an alert
in response to receipt of an email with a title of 'Notification
message'. The alert will only display when the email has not been
categorized.

The messages are computer-generated from phone call data taken at
a call center. They are in a consistent HTML format. This program
uses regular expressions to extract relevant data and include them
on the alert dialog. 

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

import PySimpleGUI as sg
import win32com.client as win32

subj = "Notification message"
alert_shown = False
sg.ChangeLookAndFeel("Dark")
sg.SetOptions(
    element_padding=(0, 0),
    font=("verdana", 9),
    text_color="#32CD32",
    background_color="#1E1E1E",
    text_element_background_color="#1E1E1E",
)


layout = [
    [sg.T("")],
    [sg.T("", size=(60, 1), key="_CALLER_")],
    [sg.T("")],
    [sg.T("", size=(60, 1), key="_CALLER_PHONE_")],
    [sg.T("")],
    [sg.T("", size=(60, 1), key="_CALLER_EMAIL_")],
    [sg.T("")],
    [sg.T("", size=(60, 1), key="_TENANT_")],
    [sg.T("")],
    [sg.T("", size=(60, 1), key="_TENANT_PHONE_")],
    [sg.T("")],
    [sg.T("", size=(60, 1), key="_UNIT_")],
    [sg.T("")],
    [sg.T("", size=(60, 1), key="_ISSUE_TYPE_")],
    [sg.T("")],
    [sg.T("", size=(60, 1), key="_RECEIPT_TIME_")],
    [sg.T("")],
    [sg.T("", size=(80, 1), key="_COMMENTS_1")],
    [sg.T("", size=(80, 1), key="_COMMENTS_2")],
    [sg.T("", size=(80, 1), key="_COMMENTS_3")],
    [sg.T("", size=(80, 1), key="_COMMENTS_4")],
    [sg.T("")],
    [sg.T("")],
    [sg.Button("Close", visible=True, key="_BUTTON_CLOSE_")],
]


if __name__ == "__main__":
    outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    for message in messages:
        if not alert_shown:
            if message.Subject == subj and message.Categories == "":
                receipt_time = message.ReceivedTime
                content = message.Body
                caller_name = re.findall(
                    r"\bCaller\r\n\r\n\t(.*)\r\n\r\nPhone\b", content
                )[0]
                caller_phone = re.findall(
                    r"\bNumber\r\n\r\n\t(.*)\r\n\r\nEmail\b", content
                )[0]
                caller_email = re.findall(
                    r"\bEmail\r\n\r\n\t(.*)\t\r\n\tCall Time\b", content
                )[0]
                tenant_name = re.findall(
                    r"\bName\r\n\r\n\t(.*)\r\n\r\nPhone Number\b", content
                )[0]
                tenant_phone = re.findall(
                    r"\bNumber\r\n\r\n\t(.*)\r\n\r\n\tSpace\b", content
                )[0]
                unit_number = re.findall(
                    r"\bSpace #\r\n\r\n\t(.*)\r\n\r\nIssue\b", content
                )[0]
                issue_type = re.findall(
                    r"\bType\r\n\r\n\t(.*)\r\n\r\n\t\r\nAdditional\b", content
                )[0]
                comments = re.findall(
                    r"\bComments\r\n\r\n. (.*) \r\n\r\n\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n <https\b",
                    content,
                )[0]

                window = (
                    sg.Window(
                        " XPS Alert - Categorize this in Outlook!",
                        size=(700, 450),
                        default_element_size=(30, 1),
                        grab_anywhere=False,
                        background_color="#1E1E1E",
                        auto_size_text=False,
                        auto_size_buttons=False,
                    )
                    .Layout(layout)
                    .Finalize()
                )
                window.Element("_CALLER_").Update(f"Caller name: {caller_name}")
                window.Element("_CALLER_PHONE_").Update(f"Caller phone: {caller_phone}")
                window.Element("_CALLER_EMAIL_").Update(f"Caller email: {caller_email}")
                window.Element("_TENANT_").Update(f"Tenant name: {tenant_name}")
                window.Element("_TENANT_PHONE_").Update(f"Tenant phone: {tenant_phone}")
                window.Element("_UNIT_").Update(f"Unit number: {unit_number}")
                window.Element("_ISSUE_TYPE_").Update(f"Issue type: {issue_type}")
                window.Element("_RECEIPT_TIME_").Update(f"Receipt time: {receipt_time}")

                max_line_elements = 12
                lines = 5
                comment_elements = comments.split(" ")
                comment_lines = ["", "", "", ""]
                for line in range(0, lines):
                    line_txt = []
                    while True:
                        if len(comment_elements) > 0:
                            line_txt.append(comment_elements.pop(0))
                        else:
                            break
                        if len(line_txt) > max_line_elements:
                            comment_lines[line] = " ".join(line_txt)
                            break

                window.Element("_COMMENTS_1").Update(f"Comments: {comment_lines[0]}")
                window.Element("_COMMENTS_2").Update(
                    f"                   {comment_lines[1]}"
                )
                window.Element("_COMMENTS_3").Update(
                    f"                   {comment_lines[2]}"
                )
                window.Element("_COMMENTS_4").Update(
                    f"                   {comment_lines[3]}"
                )

                alert_shown = True
                while True:
                    event, values = window.Read(timeout=10)
                    if event == "_BUTTON_CLOSE_":
                        window.Close()
                        sys.exit()

    if not alert_shown:
        window.Close()
        sys.exit()
