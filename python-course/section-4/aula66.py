'''
argumento nao nomeado = posicional
'''


def soma (x, y, z):
    print(f'{x=}, y={y}, {z=}','|','x + y + z= ', x + y)


# soma(1, 2)
# soma(2, 1)
# soma(y=2, z=3, 1) erro

soma(y=2, z=3, y= 1)
# nao recomendado, chamar sempre tudo nomeado ou nao nomeado
