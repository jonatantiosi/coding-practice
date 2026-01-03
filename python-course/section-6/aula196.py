# mypy: ignore-errors
# flake8: noqa

''' aula 196 parte 1'''

# Útil ao mexer com interfaces gráficas

from time import sleep
from threading import Thread

# print('Lorem')

# for i in range(10):
#     print(i)
#     sleep(.5)

# print('Ipsum')


class MinhaThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


thread_1 = MinhaThread(' Thread 1', 5)
thread_1.start()

thread_2 = MinhaThread(' Thread 2', 2)
thread_2.start()

thread_3 = MinhaThread(' Thread 3', 3)
thread_3.start()

for i in range(12):
    print(i)
    sleep(.5)

''' aula 196 parte 2'''

from time import sleep
from threading import Thread

'''
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


# se for apenas um arg: args=(arg1,)
thread_1 = Thread(target=vai_demorar, args=('Lorem', 2))
thread_1.start()

thread_2 = Thread(target=vai_demorar, args=('Ipsum', 3))
thread_2.start()

thread_3 = Thread(target=vai_demorar, args=('Dolor', 5))
thread_3.start()

for i in range(15):
    print(i)
    sleep(.5)
'''


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


# se for apenas um arg: args=(arg1,)
thread_1 = Thread(target=vai_demorar, args=('Lorem', 10))
thread_1.start()
# thread_1.join()

while thread_1.is_alive():
    print('Esperando a thread...')
    sleep(2)
print('Thread acabou.')
