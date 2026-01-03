'''
44 — Mapeamento com list/dict comprehensions

Tarefa: dado lista de produtos [{nome, preco}], gere novo dicionário onde as
chaves são nomes e valores são preços corrigidos por 10% se preço > 50. Use
comprehension (lista → dicionário).
Conceitos: list/dict comprehension, if inline.
'''


produtos = [{'Tenis': 500}, {'Camisa': 40}, {'Calça': 60}]

dicionario = {
    produto: preco * 0.9 if preco > 50 else preco
    for item in produtos
    for produto, preco in item.items()
    }

print(dicionario)
