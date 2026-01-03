string = 'lorem'
metodo = 'upper'
# dinamico


print(string)
# dir(string) no debugger pra verificar os métodos

if hasattr(string, metodo):
    # verifica a existencia de uma metodo e executa ele
    print('existe upper')
    print(string)
    print(getattr(string, metodo)())
else:
    print(f'nao existe o metodo: {metodo}')