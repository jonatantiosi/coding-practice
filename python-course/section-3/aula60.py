#operacao ternaria

# condicao = False
# variavel = 'valor' if condicao else 'outro valor'

# print(variavel)

digito = 5
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito >9 else digito

print(novo_digito)

print('valor' if False else 'outro valor' if False else 'ultimo')
# nao recomendado