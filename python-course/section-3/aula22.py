#or 

entrada = input('[E]ntrar [S]air: ')

if (entrada == 'E' or entrada == 'e'):
    senha_digitada = input('senha: ')

senha_permitida = '1234'


# if True :
    #...
if ((entrada == 'E' or entrada == 'e')) and senha_digitada == senha_permitida:
    print('entrar')
elif ((entrada == 'S' or entrada == 's')) :
    print('sair')
else:
    print('erro!')

a = 0 or False or 0.0 or 'abc' or True
print(a)