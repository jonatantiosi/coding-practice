'''
95 — Template + SMTP
Tarefa: combine um template HTML com dados substituídos e envie via SMTP em
uma única execução.
Conceitos: leitura de arquivo, Template, MIMEMultipart, SMTP.
'''
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template

CAMINHO_HTML = Path(__file__).parent / 'ex95.html'

load_dotenv()

# leitura de arquivo HTML e substituição usando template
with open(CAMINHO_HTML, 'r', encoding='utf8') as arquivo:
    texto_html = arquivo.read()
    template = Template(texto_html)
    corpo_email = template.substitute(substituir='Dolor')

# informações necessáriarias para o smtplib.SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')  # vem do .env
smtp_password = os.getenv('EMAIL_PASSWORD', '')  # vem do .env
remetente = smtp_username
destinatario = remetente

# configuracao e preparação da mensagem do email usando MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['subject'] = 'Lorem Ipsum'
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart.attach(MIMEText(corpo_email, 'html', 'utf8'))

# envio
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Enviado')
