'''
112 — Thread com classe personalizada
Tarefa: crie uma classe que herde de Thread, receba texto e tempo no __init__ e
sobrescreva run() para imprimir o texto após dormir. Inicie ao menos duas
threads.
Conceitos: threading.Thread, herança, run, start.
'''
from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)


thread_1 = MyThread('Ipsum', 3)
thread_2 = MyThread('Lorem', 2)
thread_1.start()
thread_2.start()
