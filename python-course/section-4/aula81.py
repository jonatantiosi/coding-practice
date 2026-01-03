# lista = [4, 332, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# ordenando items usando funcao 
# como e uma funcao de apenas uma linha
# da pra simplesmente usar lambda

# def ordena(item):
#     # print(item)
#     return item['nome']

def exibir(lista):
    for item in lista:
        print(item)
        

# lista.sort(key=ordena)
# lista.sort(key=lambda item: item['nome'])

# copias rasas
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
print()
exibir(l2)