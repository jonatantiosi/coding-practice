# identidade (valor na memoria)

# v1 = 'a'
# v2 = 'a'

# print(id(v1)) # mesmo valor na memoria
# print(id(v2))

condicao = True
passou_if = None

if condicao :
    passou_if = True
    print('faca algo')

else:
    print('nao faca algo')

# print(passou_if)
# print(passou_if is None)

if passou_if is not None :    
    print('passou no if')
else:
    print('nao passou no if')