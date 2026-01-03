#if entrada.isdigit():

str_numero = input('digite um numero inteiro: ')
nao_inteiro = None

try:
    numero = int(str_numero)
    par = numero % 2 == 0
    impar = not par
except:
    nao_inteiro = True


if nao_inteiro:
    print('digite um numero inteiro')
elif par:
    print('o numero e par')
elif impar:
    print('o numero e impar')
else:
    ...