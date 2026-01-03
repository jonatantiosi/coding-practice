"""
Introdução ao empacotamento e desempacotamento
"""

nomes = ['jonatan', 'paulo', 'lorem', 'ipsum']
nome1, nome2, nome3, nome4 = nomes
print(nome3)

_, nome1, *_ = ['jonatan', 'paulo', 'lorem', 'ipsum']
# convencao python variavel resto _
print(nome1, _)

