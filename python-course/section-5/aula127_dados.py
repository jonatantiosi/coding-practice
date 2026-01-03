# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

class Gato:

    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor

    # ainda não sei exportar/importar métodos
    def brincando(self, brinquedo):
        return f'{self.nome} está brincando com {brinquedo}'


gato_1 = Gato('Maple', 'Angorá Turco', 'Tricolor')
gato_2 = Gato('Amimir', 'Angorá', 'Cinza')
gato_3 = Gato('Lucifer', 'Angorá', 'Preto')

gatos = [gato_1, gato_2, gato_3]
list_gatos = []

for gato in gatos:
    list_gatos.append(gato.__dict__)

print(list_gatos)

with open('log_gatos.json', 'w', encoding='utf8') as arquivo:
    json.dump(list_gatos, arquivo, indent= 2)