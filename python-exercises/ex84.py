'''
84 — Escolhas aleatórias

Tarefa: embaralhe uma lista de 5 nomes e depois selecione 2 nomes sem
repetição.
Conceitos: random.shuffle, random.sample.

'''
import random

lista = ['Jonatan', 'Paulo', 'Miriam', 'Marcio', 'Maple']

random.shuffle(lista)
# print(lista)

print(random.sample(lista, 2))
