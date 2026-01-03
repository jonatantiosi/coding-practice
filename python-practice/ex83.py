'''
83 — Uso básico de random

Tarefa: gere um número inteiro aleatório entre 100 e 200 usando randrange.
Depois, gere outro usando randint.
Conceitos: random.seed, random.randrange, random.randint.
'''
import random

random_even_number = random.randrange(100, 200, 2)
print(random_even_number)

random_number = random.randint(100, 200)
print(random_number)
