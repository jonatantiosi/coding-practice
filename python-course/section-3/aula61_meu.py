"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = "555.556.028-94"


lista_cpf_div_digito = cpf.split('-')
cpf_so_numeros = lista_cpf_div_digito[0]
lista_cpf_sem_digito = cpf_so_numeros.split('.')
cpf_nove_numeros = "".join(lista_cpf_sem_digito)
# dava pra fazer tudo isso so usando replace ou re.sub

# print(cpf_so_numeros)


multiplicador1 = 10
soma1 = 0

for digito in cpf_nove_numeros: # tinha usado enumerate mas acredito que nao precisa
    try:
        int_digito = int(digito)
    except:
        ...
    digito_mult = int_digito*multiplicador1
    soma1 = soma1 + digito_mult
    # print(digito_mult)
    multiplicador1 -= 1

num_validacao1 = (soma1 * 10) % 11
primeiro_digito = 0 if num_validacao1 > 9 else num_validacao1


cpf_dez_numeros = cpf_nove_numeros + str(primeiro_digito)

multiplicador2 = 11
soma2 = 0 

for digito in cpf_dez_numeros:
    try:
        int_digito = int(digito)
    except:
        ...
    digito_mult = int_digito*multiplicador2
    soma2 = soma2 + digito_mult
    # print(f'{int_digito}*{multiplicador2}={digito_mult}: (soma = {soma2})')
    multiplicador2 -= 1


num_validacao2 = (soma2 * 10) % 11
segundo_digito = 0 if num_validacao2 > 9 else num_validacao2

print(primeiro_digito)
print(segundo_digito)

digito1_valido = primeiro_digito == int(cpf[-2]) 
digito2_valido = segundo_digito == int(cpf[-1]) 

if digito1_valido and digito2_valido:
    print('cpf válido')
else:
    print('cpf inválido')
