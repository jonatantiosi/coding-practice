import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self. idade = idade
        

pessoa1 = Pessoa('Jonatan', 23)
pessoa2 = Pessoa('Miriam', 45)
pessoa3 = Pessoa('Marcio', 45)

base_dados = [
    vars(pessoa1),
    vars(pessoa2),
    vars(pessoa3)
]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('Fazendo dump')
        json.dump(base_dados, arquivo, indent=2)

if __name__ == '__main__':
    fazer_dump()