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
