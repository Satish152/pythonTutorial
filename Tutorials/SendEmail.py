#sending a mail using python is very simple, we need to import smtplib from pip and then we need to
# connect to the smtp server by proving required information and then we cna use login and send function

import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('This is my message')

msg['Subject'] = 'This is Python Mail Subject'
msg['From'] = "srongala1@gmail.com"
msg['To'] = "rongalasatish52@gmail.com"

server=smtplib.SMTP("smtp.gmail.com",587)

server.starttls()
server.login("srongala1@gmail.com","satish@143")
server.sendmail("srongala1@gmail.com","rongalasatish52@gmail.com","This is a test python mail")
#or
server.send_message(msg) #this is another way of sending message with all subjects and body
print("mail sent")