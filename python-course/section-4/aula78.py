'''
set(iteravel)
'''

# s1 = set('lorem')
# s2 = {'ipsum', 10}
# s3 = set()

# print(s1, type(s1))
# print(s2)
# print(s3)

'''
eficientes para remover duplicatas de iteraveis
sets podem nao garantir a ordem
'''

# s1 = {1, 2, 3, 3, 3, 1} 

l1 = {1, 2, 2, 3, 3, 1}
s1 = set(l1)
l2 = list(s1)

print(l2)

print(3 in s1)

'''
nao aceitam valores mutaveis, e.g. listas, dicts etc.
nao tem indice
'''