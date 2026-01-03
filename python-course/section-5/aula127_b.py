import json
from aula127_a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)

    pessoa_1 = Pessoa(**pessoas[0])
    pessoa_2 = Pessoa(**pessoas[1]) 
    pessoa_3 = Pessoa(**pessoas[2]) 

    print(pessoa_1.nome, pessoa_1.idade)
    print(pessoa_2.nome, pessoa_1.idade)
    print(pessoa_3.nome, pessoa_2.idade)