'''
133 — Ação de menu disparando função
 Tarefa: conecte uma ação de menu para executar uma função que imprime algo no
 terminal.
 Conceitos: QAction.triggered, connect.
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow


def slot_example_1(message: str):
    print(message)


# def slot_example_2(message: str):
#     print('hard coded message')


application = QApplication(sys.argv)
main_window = QMainWindow()
menu_bar = main_window.menuBar()
menu_1 = menu_bar.addMenu('Menu 1')
action_1 = menu_1.addAction('Action 1')
mensagem = 'Lorem'
action_1.triggered.connect(lambda: slot_example_1(mensagem))
# action_1.triggered.connect(slot_example_2)

main_window.show()
application.exec()
