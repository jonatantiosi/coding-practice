nome = input('nome: ')
i = 0
ultima_letra = len(nome) - 1


while i < len(nome):
    letra = nome[i]
    if i == ultima_letra:
        print(f'{letra}', end ='')
    else:
        print(f'{letra}*', end ='')
    i += 1