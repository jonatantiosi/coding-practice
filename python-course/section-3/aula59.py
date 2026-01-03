string = 'abcd'
lista = ['lorem','ipsum', 1, 2, 3, 'dolor']
tupla = 'python', 'é', 'legal'

salas = [
    ['Jonatan', 'Nathalia'],    #0

    ['Marcio', "Miriam"],       #1

    ['Maple', 'Flyp', 'Fifi'],  #2
   
]


# p, s, *_, u = lista
# print(p, u)

# for nome in lista:
#     print(nome, end=" ")

# print()
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')
