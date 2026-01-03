'''
94 — Envio SMTP autenticado
Tarefa: conecte ao Gmail com smtplib.SMTP(...), chame starttls(), faça login e
envie um e-mail simples.
Conceitos: smtplib.SMTP, starttls, login, send_message.
'''
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

mime_multipart = MIMEMultipart()
mime_multipart['subject'] = 'Lorem Ipsum'
mime_multipart['from'] = 'jonatanosu@gmail.com'
mime_multipart['to'] = 'jonatanosu@gmail.com'
mime_multipart.attach(MIMEText('Mensagem simples', 'plain', 'utf8'))

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo() 
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Enviado')