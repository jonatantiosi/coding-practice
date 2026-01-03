from funcoes_uteis.main import print_iter

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# maiores_que_20 = [
#     produto for produto in produtos
#     if produto['preco'] > 20
# ]

novos_produtos = filter(
    # primeiro parametro = funcao
    lambda produto: produto['preco'] > 20,
    # segundo parametro = iteravel
    produtos
)

print_iter(novos_produtos)