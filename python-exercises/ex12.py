from itertools import groupby

lista_clientes = [
    {'nome': 'Ana', 'plano': 'premium'},
    {'nome': 'Bruno', 'plano': 'básico'},
    {'nome': 'Clara', 'plano': 'premium'},
    {'nome': 'Daniel', 'plano': 'básico'},
]

def key_ordenacao(param):
    return param['plano']

clientes_ordenados = sorted(lista_clientes, key=key_ordenacao)

clientes_agrupados = groupby(clientes_ordenados, key=key_ordenacao)

for chave, clientes in clientes_agrupados:
    print(chave)
    for cliente in clientes:
        print(cliente)