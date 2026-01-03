'''
26. Exceções Personalizadas

Crie uma exceção SenhaFracaError, que deve ser levantada se uma senha tiver menos de 6 caracteres.
Crie uma função criar_usuario(senha) que levanta essa exceção se a senha for fraca.
Use try/except para tratar isso e exibir uma mensagem amigável.
'''
from random import randint

class WeakPasswordError(Exception):

    def __init__(self, *args):
        ...

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password

def check_password(password):
    char_num = len(str(password))
    if char_num < 6:
        raise WeakPasswordError('Weak Password')
    
def create_user(username, password):
    check_password(password)
    return User(username, password)
    
try:    
    user_1 = create_user('lorem', randint(99999, 100000))
    print(f'{user_1.username}:{user_1._password}')
except WeakPasswordError:
    print('Senha fraca')
    
        

