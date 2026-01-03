'''
Crie um decorator chamado log_call que imprime "Chamando..." antes de executar
a função decorada.

Use-o em um método executar() da classe Tarefa.
'''


def log_call(metodo):
    def inner(*args, **kwargs):
        print('Chamando...', end=' ')
        return metodo(*args, **kwargs)
    return inner


class Tarefa:

    @log_call
    def executar(self):
        print('Executar')


tarefa_1 = Tarefa()

tarefa_1.executar()
