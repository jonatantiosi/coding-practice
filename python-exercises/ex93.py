'''
93 — Construindo e-mail MIME
Tarefa: crie um objeto MIMEMultipart, configure from, to, subject e anexe um
corpo MIMEText em HTML.
Conceitos: MIMEMultipart, MIMEText, campos do e-mail.
'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

remetente = 'Paulo'
destinatario = 'Jonatan'
assunto = 'Assunto qualquer'
texto_email = 'Lorem Ipsum Dolor Amet'

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = assunto

corpo_email = MIMEText(texto_email, 'html', 'utf8')
mime_multipart.attach(corpo_email)

# testes
print(mime_multipart.as_string())