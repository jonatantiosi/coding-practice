'''
86 — Gerador de Senhas

Tarefa: gere uma senha com 12 caracteres misturando letras, dígitos e
pontuação.
Conceitos: string.ascii_letters, string.digits, string.punctuation,
secrets.choice / SystemRandom.choices.
'''
from secrets import SystemRandom
import string

# concatenacao de todas as letras numeros e simbolos
alphabet = ''.join([string.ascii_letters, string.digits, string.punctuation])
# print(alphabet)

random_ = SystemRandom()

password_char_list = random_.choices(alphabet, k=12)
password = ''.join(password_char_list)
print('Senha:', password)