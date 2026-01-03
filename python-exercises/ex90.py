'''
90 — Variáveis de Ambiente
Tarefa: leia a variável de ambiente BD_PASSWORD usando os.getenv após carregar
.env.
Conceitos: load_dotenv, os.getenv, variáveis de ambiente.
'''
import os
from dotenv import load_dotenv

load_dotenv()

var_ambiente = os.getenv('BD_PASSWORD')
print(var_ambiente)