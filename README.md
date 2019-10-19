Jeff's XPS Email Alert Utility

This is a custom and single-purpose utility that displays an alert
in response to receipt of an email with a title of 'Notification
message'. The alert will only display when the email has not been
categorized.

The messages are computer-generated from phone call data taken at
a call center. They are in a consistent HTML format. This program
uses regular expressions to extract only the most relevant data 
and include them on the alert dialog. 

The program is to be periodically triggered using the Windows Task
Scheduler and is expected to be used in conjunction with an Outlook
rule that alerts to emails with a 'Notification message' title. If
such an alert is closed without categorizing the email, this alert
will be triggered at a later time to assure the email is categorized.

When no emails are found that trigger the alert dialog, this shuts
down automatically.

There are two versions of the code - one written with PySimpleGUI
and the other using wxPython.
