'''
25. Polimorfismo com Envio de Mensagem

Crie uma superclasse abstrata Mensagem, com método abstrato enviar().
Crie duas subclasses: MensagemEmail e MensagemSMS, cada uma com uma forma diferente de “enviar”.
Crie uma função que receba um objeto Mensagem e chame enviar(), sem saber o tipo da subclasse.
'''

from abc import ABC, abstractmethod

class Mensagem(ABC):

    @abstractmethod
    def enviar(self):... # self precisa ser instanciado anyways

class MensagemEmail(Mensagem):

    def __init__(self, msg):
        self.msg = msg
        super().__init__()

    def enviar(self):
        print(f'Via e-mail: {self.msg}')

class MensagemSMS(Mensagem):

    def __init__(self, msg):
        self.msg = msg
        super().__init__()

    def enviar(self):
        print(f'Via SMS: {self.msg}')


def enviar_mensagem(msg:Mensagem):
    msg.enviar()

enviar_mensagem(MensagemSMS('Oi'))
enviar_mensagem(MensagemEmail('Oi'))