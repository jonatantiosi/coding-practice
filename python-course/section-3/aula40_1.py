while True:

    numero1 = input('numero 1: ')
    numero2 = input('numero 2: ')
    operador = input('operador (+ - / *): ')

    # flag
    numeros_validos = None

    float_numero1 = 0
    float_numero2 = 0

    try:
        float_numero1 = float(numero1)
        float_numero2 = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None          # redundante

    if numeros_validos is None:
        print('um ou ambos os numeros sao invalidos')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('operador invalido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue
    

    if operador == '+':
        print(f'{float_numero1} + {float_numero2} = {float_numero1+float_numero2}')
    elif operador == '-':
        print(f'{float_numero1} - {float_numero2} = {float_numero1-float_numero2}')
    elif operador == '/':
        print(f'{float_numero1} / {float_numero2} = {float_numero1/float_numero2}')
    elif operador == '*':
        print(f'{float_numero1} * {float_numero2} = {float_numero1*float_numero2}')
    else:
        print('nunca deveria chegar aqui')
    
    sair = input('[s] sair: ').lower().startswith('s')
    
    if sair:
        break