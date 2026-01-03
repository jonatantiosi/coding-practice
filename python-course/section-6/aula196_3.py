from time import sleep
from threading import Thread
from threading import Lock


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Ingressos insuficientes.')
            sleep(.5)
            self.lock.release()
            return

        sleep(.5)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos. Restante: {self.estoque}')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 10):
        thread_1 = Thread(target=ingressos.comprar, args=(i,))
        thread_1.start()

    print(ingressos.estoque)
