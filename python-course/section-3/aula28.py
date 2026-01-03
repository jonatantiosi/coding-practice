# exercicio

str_nome = input('digite seu nome: ')
str_idade = input('digite sua idade: ')

str_nome_inv = str_nome[::-1]
nome_espaco = ' 'in str_nome
quantidade_letras = len(str_nome)
primeira_letra = str_nome[0]
ultima_letra = str_nome[-1]

if str_nome and str_idade :
    print(f'seu nome e {str_nome}\n'
          f'seu nome invertido e {str_nome_inv}')
    
    if nome_espaco :
        print('seu nome contem espaco(s)')
    else :
        print('seu nome nao contem espaco(s)')
    
    print(f'seu nome tem {quantidade_letras} letras')
    print(f'a primera letra do seu nome e: {primeira_letra} \n'
          f'a ultima letra do seu nome e: {ultima_letra}')
else:
    print('desculpe, voce deixou campos vazios')