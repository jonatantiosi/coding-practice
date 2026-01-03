from itertools import zip_longest

def soma_listas(lista1, lista2):
    return [
        (x + y) for x, y in zip_longest(lista1, lista2, fillvalue=0)
    ]


a = [10, 20, 30, 40]
b = [1, 2]

print(soma_listas(a,b))