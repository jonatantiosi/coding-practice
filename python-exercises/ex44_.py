'''
44 — Mapeamento com list/dict comprehensions

Tarefa: dado lista de produtos [{nome, preco}], gere novo dicionário onde as
chaves são nomes e valores são preços corrigidos por 10% se preço > 50. Use
comprehension (lista → dicionário).
Conceitos: list/dict comprehension, if inline.
'''

produtos = [
    {'nome': 'Caneta', 'preco': 10},
    {'nome': 'Camiseta', 'preco': 70},
    {'nome': 'Caderno', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.1}
    if produto['preco'] > 50 else {*produto}
    for produto in produtos
]

print(novos_produtos)
