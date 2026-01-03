
import os
# para usar o clear


palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:
    
    letra_digitada  = input('Letra: ')
    tentativas += 1

    if len(letra_digitada)>1:
        print('digite apenas uma letra')
        continue


    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        # mantem as letras que o usuario ja acertou

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            # print(letra_secreta)
            palavra_formada += letra_secreta
        else:
            # print("*")
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'A palavra era "{palavra_formada}"')
        print('Tentativas:', tentativas)

        letras_acertadas = ''
        tentativas = 0