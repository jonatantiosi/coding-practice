produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# print(produto.items())




dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    # checka se e str
    # daria pra verificar mais de um com tupla e.g. (float, int)
    for chave, valor
    in produto.items()
    if chave != 'categoria'
    # chave categoria nao entra

}

# gerando dict atraves de lista

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

print(dc)
print(dict(lista))

# set comprehension


set1 = {i * 2 for i in range(10)}
print(set1)