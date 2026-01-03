'''
escopo: o que e definido na funcao fica na funcao
'''

x = 0
y = 10

def las_vegas():
    # global x
    # altera o valor de x mesmo nos escopos maiores
    x = 11

    print(x)
    def cassino():
        print(x)
    cassino()
    y = 50
    print(y)

# da pra acessar varias dos escopos acima
# mas nao o contrario

# print(y)
# name 'y' is not defined



print(x)
las_vegas()
print(x)