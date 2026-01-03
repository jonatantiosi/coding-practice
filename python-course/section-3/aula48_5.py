"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'paulo'
outra_var = nome
nome = 'jonatan'

print(nome, outra_var)


lista_a = ['joao', 'maria']
lista_c = lista_a.copy()
lista_b = lista_a
# as duas listas apontam para o mesmo valor na memoria

lista_a[0] = 'lorem'
print(lista_b)

print(lista_c)