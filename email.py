import smtplib

domain_user = 'email@domain.com'
domain_password = input("input password: ")

sent_from = "email@domain.com"
to = "email@domain.com"
subject = "Sent with Python."
email_text = """\
From: %s
To: %s
Subject: %s
%s
""" %(sent_from, to, subject, body)
server = smtplib.SMTP_SSL('smtp.domain.com', 465)
server.ehlo_or_helo_if_needed()
server.login(domain_user, domain_password)
server.sendmail(sent_from, to, email_text)
server.close()

print("Email Sent!")
