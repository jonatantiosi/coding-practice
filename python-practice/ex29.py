'''
29. __new__ vs __init__

Crie a classe IdentificadorUnico:

    Use __new__ para gerar um ID aleatório (ex: com uuid4).

    Use __init__ para registrar o nome do dono.

    Mostre o ID e o nome depois de criar uma instância.
'''

import random
id_characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

print(len(id_characters))
print(id_characters[35])

def gerar_id():
    id = '' 
    for i in range(5):
        id += id_characters[random.randint(0,35)]
    return id

class UniqueIdentifier:

    def __new__(cls, *args, **kwargs):
        
        instance = super().__new__(cls)
        instance.id = gerar_id()
        return instance
        

    def __init__(self, name):
        self.name = name

user_1 = UniqueIdentifier('Jonatan')
user_2 = UniqueIdentifier('Miriam')

print(f'User "{user_1.name}", id: {user_1.id}')
print(f'User "{user_2.name}", id: {user_2.id}')


