lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

'''solucao pythonica'''

lista_soma = [ 
    x + y for x, y in zip(lista_a, lista_b)
    # especie de desempacotamento
    # daria pra implementar com ziplongest tbm
]

print(lista_soma)

'''solucao generica'''

# lista_soma = []

# for i in range(len(lista_b )):
#     lista_soma.append(lista_a[i] + lista_b[i])

# print(lista_soma)

'''solucao II'''

# lista_soma = []

# for i, _ in enumerate(lista_b ):
#     lista_soma.append(lista_a[i] + lista_b[i])

# print(lista_soma)




