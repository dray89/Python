import untangle
obj = untangle.parse('path/to/file.xml')
#https://docs.python-guide.org/scenarios/xml/
import smtplib, openpyxl, sys
from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

   # Open the spreadsheet and get the latest dues status.
template = input("Input Document Name and Extension: " )
username = input("Input Sender Email: ")
password = input("input password: ")
wb = openpyxl.load_workbook(input("Please enter file: "))
sheet = wb.get_sheet_by_name(input("Please enter Sheet Name: ")
FinalDispositionColumn = sheet.get_highest_column()
FinalDispositionStatus = sheet.cell(row=1, column=lastCol).value

   # TODO: Check each contact's best disposition. Check to ensure all Final Dispositions are correct.

   # TODO: Log in to email account.

   # TODO: Send out reminder emails.
okay = ["Email Sent", "voicemail left"] #All FinalDispositions Okay to Contact
contacts = {}
for r in range(2, sheet.get_highest_row() + 1):
    FinalDisposition = sheet.cell(row=r, column=lastCol).value
       if FinalDisposition in okay:
           name = sheet.cell(row=r, column=1).value
           email = sheet.cell(row=r, column=2).value
           contacts[name] = email
        else:
            pass

smtpObj = smtplib.SMTP('smtp.domain', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(username, sys.argv[1])

for name, email in contacts.items():
    from mailmerge import MailMerge
    document = MailMerge(template)
    mergefields = []
        mergefields.append(document.get_merge_fields())
    document.merge(mergefields)

sendmailStatus = smtpObj.sendmail(username, email, body)
if sendmailStatus != {}:
    document('There was a problem sending email to %s: %s' % (email, sendmailStatus))
    
smtpObj.quit()



range = input("How many contacts?: ")
contacts = []
contacts.append(input("Input Contact List: "))
address = []
address.append()


sent_from = "email@domain.com"
to = 
subject = input("Enter Email Subject:" )
body = document(mailmerge)
email_text = """\
From: %s
To: %s
Subject: %s

%s

""" %(sent_from, to, subject, body)
server = smtplib.SMTP_SSL('smtp.domain', 465)
server.ehlo_or_helo_if_needed()
server.login(domain_user, domain_password)
server.sendmail(sent_from, to, email_text)
server.close()

print("Email Sent!")

