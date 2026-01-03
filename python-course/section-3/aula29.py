# try/except

numero_str = input('a: ')

# apenas numeros (exceto 2.2, 4,5 etc)

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} e {numero_float * 2:.2f}')
# else:
#     print('nao e numero')

try:
    print('SRT:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_str} e {numero_float * 2:.2f}')
except:
    print('nao e numero')