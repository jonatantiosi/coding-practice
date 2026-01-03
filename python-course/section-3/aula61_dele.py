import re 
import sys
# regular expression


input = input('CPF: ')

cpf_enviado = input.replace('.','').replace('-','')

cpf_enviado = re.sub(
    r'[^0-9]',
    # tudo que nao e numero
    '',
    input
)

cpf_sequencial =  cpf_enviado == cpf_enviado[0] * len(cpf_enviado)
if cpf_sequencial:
    print('dados sequenciais')
    sys.exit()


nove_digitos = cpf_enviado[:9]
contador_regressivo1 = 10

resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo1
    contador_regressivo1 -= 1


validacao_digito1 = (resultado * 10) % 11
# print(validacao_digito1)
digito1 = validacao_digito1 if validacao_digito1 <= 9 else 0

# print(digito1)

dez_digitos = nove_digitos + str(digito1)
contador_regressivo2 = 11

resultado2 = 0
for digito in dez_digitos:
    resultado2 += int(digito) * contador_regressivo2
    contador_regressivo2 -= 1

validacao_digito2 = (resultado2 * 10) % 11
digito2 = validacao_digito2 if validacao_digito2 <= 9 else 0

# print(digito1, digito2)

cpf_gerado = f'{nove_digitos}{digito1}{digito2}'
# print(cpf_gerado)

if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido')
else:
    print('CPF inválido')