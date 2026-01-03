"""
enumerate - enumera iteráveis (índices)"
"""

# se tiver duvida ver no debugger

lista = ['jonatan', 'paulo', 'tiosi']
lista.append('santana')

lista_enumerada = enumerate(lista)

# print(next(lista_enumerada))

# for item in lista_enumerada:
#     indice, nome = item
#     print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('for da tupla:')
#     for valor in tupla_enumerada:
#         print(f"\t{valor}")

# print(list(lista_enumerada))