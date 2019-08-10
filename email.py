# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:38:17 2019

@author: rayde
"""

  
class email(articles):    
    def read_template(self):
        filename = self.name
        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
            return template_file_content
        
    def compose(self):
        message = self.read_template()
        msg = MIMEMultipart()
        msg['From'] = 'raydebra89@gmail.com'
        msg['To'] = 'debraray89@icloud.com'
        msg['Subject']= 'Your News Update is Ready'
        msg.attach(MIMEText(message, 'plain'))
        self.msg = msg
        return msg
    
    def send_email(self):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('raydebra89@gmail.com', 'qoerbzlkaocdttam')  
        s.send_message(self.compose())
        s.quit()