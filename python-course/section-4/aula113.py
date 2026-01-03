from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

def funcao_do_reduce(acumulador, produto):
    print(acumulador, produto)
    return acumulador + produto['preco']

total = reduce(
    # funcao_do_reduce,
    lambda acumulador, produto: acumulador + produto['preco'],
    # funcao
    produtos,
    # iteravel
    0
    # valor inicial
)

print(total)

# soma = sum(produto['preco'] for produto in produtos)
# print(soma)