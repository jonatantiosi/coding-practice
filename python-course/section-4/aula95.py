
# def divide(n, d):
#     try:
#         return n/d
#     except ZeroDivisionError:
#         print('log erro')
#         # quando quer fazer alguma coisa no meio do erro
#         raise

def teste_denominador_zero(d):
    if d == 0:
        raise ZeroDivisionError('vc esta tentando dividir por zero')
    return True

def int_ou_float(x):
    tipo_x = type(x)
    if not isinstance(x, (float,int)):
        raise TypeError(
            f'"{x}" deve ser int ou float. '
            f'"{x}" nao pode ser "{tipo_x.__name__}"'
        )

def divide(n, d):
    teste_denominador_zero(d)
    int_ou_float(n)
    int_ou_float(d)
    return (n / d)
    
print(divide(8, '0'))

# print(123)

# raise ValueError('deu erro')
# print(456)