# def Print(a, b, c):
#     print('lorem')
#     print('lorem')
#     print('lorem')


def imprimir(a, b, c):
    # paramentros
    print(a+b+c)

imprimir(1, 2, 3)
# argumento (valor)

def saudacao(nome = 'vazio'):
    #se nao passar  nenhum valor usa esse
    print(f'ola {nome}')

nome = input("nome: ")
saudacao(nome)