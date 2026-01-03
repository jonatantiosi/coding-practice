tupla = (1, 2, 3)
print(id(tupla))  # ID da tupla original

tupla = tupla + (4,)
print(id(tupla))  # Novo ID, porque gerou uma nova tupla

lista = [1, 2, 3]
print(id(lista))  # ID da lista original

lista.append(4)
print(id(lista))  # Mesmo ID, porque a lista foi modificada
