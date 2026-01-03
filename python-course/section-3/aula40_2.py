""" calculadora com while """

while True:
    
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    # flag
    float_num1 = 0
    float_num2 = 0
    # para que as variáveis não sejam definidas dentro do bloco try


    try:
        float_num1 = float(numero1)
        float_num2 = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
        # garantia

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        res = float_num1 + float_num2
        print(f'{float_num1} + {float_num2} = {res}')
    elif operador == '-':
        res = float_num1 - float_num2
        print(f'{float_num1} - {float_num2} = {res}')
    elif operador == '/':
        res = float_num1 / float_num2
        print(f'{float_num1} / {float_num2} = {res:.2f}')
    elif operador == '*':
        res = float_num1 * float_num2
        print(f'{float_num1} * {float_num2} = {res}')
    else:
        print('Nunca deveria chegar aqui')


    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break