'''
(84 — Escolhas aleatórias

Tarefa: embaralhe uma lista de 5 nomes e depois selecione 2 nomes sem
repetição.
Conceitos: random.shuffle, random.sample.)

85 — Random vs Secrets

Tarefa: recrie o mesmo exercício anterior, mas usando secrets.SystemRandom.
Conceitos: secrets, SystemRandom, segurança x pseudoaleatoriedade.
'''
from secrets import SystemRandom

random_ = SystemRandom()

lista = ['Jonatan', 'Paulo', 'Miriam', 'Marcio', 'Maple']

random_.shuffle(lista)
# print(lista)
print(random_.sample(lista, 2))
