'''
106 — Requisição HTTP com Requests
Tarefa: crie um script que faça uma requisição GET para http://localhost:3333/
e imprima o código de status da resposta (status_code).
Conceitos: requests, HTTP, status codes.
'''
import requests

url = 'http://localhost:3333/'
response = requests.get(url)

print('Código de status:', response.status_code)
