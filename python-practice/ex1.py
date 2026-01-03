'''
List Comprehension (Baseado na aula85.py)

Crie uma lista de tuplas contendo todos os pares (x, y) possíveis para x e y variando de 0 a 4
mas exclua os casos em que x == y.
'''
def x_igual_a_y(x, y):
    return x == y

# meio desnecessaria


tuplas_sem_pares = [

    (x, y)
    for x in range(4) # precisava ser range(5)
    for y in range(4) # precisava ser range(5)  
    if not x_igual_a_y(x, y)
    
]

print('lista dos pares (x, y) até 4 excluindo x igual a y:')
for tupla in tuplas_sem_pares:
    print(tupla)