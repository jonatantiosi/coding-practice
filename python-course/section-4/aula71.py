'''
*args
'''

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma (x,y):
#     return x + y

def soma(*args):
    soma = 0
    for num in args:
        soma += num
        # print(num, soma)

    return soma

numeros = 1, 2, 3, 4, 5, 6

soma_numeros1 = soma(*numeros)
# desempacota 'numeros" para funcionar na funcao soma
print(soma_numeros1)

soma_numeros2 = soma(55, 102, 21, 343)
print(soma_numeros2)

print(sum((55, 102, 21, 343)))