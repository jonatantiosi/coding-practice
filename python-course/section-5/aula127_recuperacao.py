import json


with open ('log_gatos.json', 'r', encoding='utf8') as arquivo:
    gatos_list = json.load(arquivo)

# print(gatos_list)


class Gato:
    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor

gato_1 = Gato(**gatos_list[0])
gato_2 = Gato(**gatos_list[1])
gato_3 = Gato(**gatos_list[2])

print(gato_1.nome)     
print(gato_2.nome)     
print(gato_3.nome)   
