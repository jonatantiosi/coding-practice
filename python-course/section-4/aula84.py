'''
list comprehension
'''

import pprint

def pretty_print(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# print(list(range(10)))

lista = []

for numero in range(10):
    lista.append(numero)


lista = [
    numero * 2 
    for numero in range(10)
]

# print(lista)

# mapeamento de dados

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    # aumento de 5% nos precos de produtos > 20
    # so exibe preco original > 10
    {**produto, 'preco':produto['preco']*1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

# print(*novos_produtos, sep='\n')\

pretty_print(novos_produtos)

# filtro, depois do for
# lista = [
#     n for n in range(10)
#     if n < 5
# ]

# pretty_print(lista)
