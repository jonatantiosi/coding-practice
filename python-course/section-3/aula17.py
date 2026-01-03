

condicao1 = False
condicao2 = True
condicao3 = True


if condicao1:
    print('condicao 1')
elif condicao2:
    pass
    ...
elif condicao3:
    print(condicao3) # executa apenas uma quando True
else:
    print('nenhuma')

if 10 == 10:
    print('outro if')

print('fora do if')