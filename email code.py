import smtplib

gmail_user = 'raydebra89@gmail.com'
gmail_password = input("input password: ")

sent_from = "raydebra89@gmail.com"
to = "raydebra89@gmail.com"
subject = "Sent with Python. Cool or what?"
email_text = """\
From: %s
To: %s
Subject: %s

%s

""" %(sent_from, to, subject, body)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo_or_helo_if_needed()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()

print("Email Sent!")