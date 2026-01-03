from itertools import zip_longest

l1 = ['BA', 'SP', 'MG', 'RJ']
l2 = ['Salvador', 'Ubatuba', 'Belo Horizonte']  

lista_zip = list(zip(l1, l2))
lista_ziplongest = list(zip_longest(l1, l2, fillvalue='sem cidade'))

print(lista_zip)
print(lista_ziplongest)