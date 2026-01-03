"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = "ABCDE"
# print(bool(lista)) # falsy,  se vaiza
# print(lista, type(lista))

#        0    1     2                3    4
#       -5   -4    -3               -2   -1
lista = [123, True, 'Jonatan', 1.5, []] 
lista[2] = 'Paulo'
print(lista[-3].upper(),type(lista[2]))