nome = input('nome: ')

len_nome = len(nome)
curto = 0 < len_nome <= 4
normal = 5 <= len_nome <= 6
grande = len_nome > 6

if curto:
    print('nome curto')
elif normal:
    print('nome normal')
elif grande:
    print('nome grande')
else:
    print('erro!')