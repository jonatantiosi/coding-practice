"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
import random

def random_num():
    return round(random.uniform(0,10), 2)

def soma_listas(lista1, lista2):
    # soma duas listas usando como referencia a menor
    indice_max = min(len(lista1), len(lista2))
    return [
        (round(lista1[i] + lista2[i], 2)) for i in range(indice_max)
    ]

lista_a     = [random_num() for _ in range(6)]
lista_b     = [random_num() for _ in range(4)]

print(lista_a)
print(lista_b)

print(soma_listas(lista_a, lista_b))