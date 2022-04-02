import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

print('Login Details of your Email \n')
username = input('Enter Your Email Address: \n')
password = input('Enter Your Password: \n')

email_address = input("Enter Email Sender's Address: \n")
subject = input('Enter the Subject: \n')
from_name = input('Enter the From Name: \n')

email = EmailMessage()
email['from'] = f'{from_name}'
email['to'] = f'{email_address}'
email['subject'] = f'{subject}'

email.set_content('I am testing mail')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(f'{username}', f'{password}')
    smtp.send_message(email)
    print('Email Sent')