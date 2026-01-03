"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[0]
# print(lista)
lista.append(50)

lista.pop() 
# remove o ultimo elemento da lista

lista.append(60)
lista.append(70)

ultimo_valor = lista.pop(3) 
# remove e retorna o elemento no indice dele
print(lista, 'removido', ultimo_valor)