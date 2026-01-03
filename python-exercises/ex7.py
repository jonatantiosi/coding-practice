import os

dicionario = {
    'dobro': lambda x: x * 2,
    'triplo': lambda x: x * 3,
    'quadrado': lambda x: x ** 2,    
}

def executa_operacao(chave, numero):
    # busca funcao (lambda) especifica no dicionario e executa de forma dinamica
    # com base na operacao(chave) selecionada e retorna o resultado da operacao
    resultado = dicionario[chave](numero)
    os.system('cls')
    # print(f'o {chave} de {numero} é {resultado}.') # retirado
    return resultado



while True:
    tipo_operacao = input('escolha uma operação:\n'
                    'dobro\n'
                    'triplo\n' 
                    'quadrado\n'
                    ''
    ).lower()
    # evita erro do tipo se o usuario digitar "Dobro" etc

    if tipo_operacao not in dicionario.keys():
        # verifica se o user digitou uma operacao valida, se nao pede novamente
        os.system('cls')
        print('digite uma operação correta')
        continue


    str_numero = input('agora digite um número:\n'
                   ''
    )

    try: 
        # conversao numero digitado para float
        numero = float(str_numero)
    except ValueError:
        os.system('cls')
        print('digite apenas números')
        continue

    resultado = executa_operacao(tipo_operacao, numero)    
    print(f'o {tipo_operacao} de {numero} é {resultado}.')
    # eu tirei o print de dentro da função porque ouvi falar que nao é boa prática

    break 





