primeiro_valor = input('digite um valor: ')
segundo_valor = input('digite outro: ')

int_prim_val = int(primeiro_valor)
int_seg_val = int(segundo_valor)

if int_prim_val > int_seg_val:
    print(f'{primeiro_valor=} e maior que o {segundo_valor=}')
elif int_seg_val > int_prim_val:
    print(f'{segundo_valor=} e maior que o {primeiro_valor=}')
else:
    print('erro! confira se os valores sao iguais')    