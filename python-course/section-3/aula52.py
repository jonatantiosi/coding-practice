"""
Tipo tupla - Uma lista imutável
"""

# quando nao precisa alterar nada
tupla = 'jonatan', 'paulo', 'tiosi'
tupla2 = ('lorem', 'ipsum', 'santana')

print(tupla[-2], type(tupla))


lista = ['jonatan', 'paulo', 'tiosi']
lista.append(tupla2[-1])

meu_nome = tuple(lista)
print(meu_nome)

lista2 = list(tupla2)
print(lista2)


