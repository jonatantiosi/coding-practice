'''
91 — Configurar variável no ambiente
Tarefa: defina uma variável de ambiente usando os.environ['CHAVE'] = valor e
depois leia com getenv.
Conceitos: os.environ, leitura e modificação de ambiente.
'''
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['BD_NOME'] = 'Maple'
print(os.getenv('BD_NOME'))