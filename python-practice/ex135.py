'''
135 — Injeção de dependência com lambda
 Tarefa: conecte uma ação de menu a uma função que utilize um objeto externo.
 Conceitos: lambda, adiamento de execução.
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar


def slot_example_1(status_bar: QStatusBar, message: str):
    status_bar.showMessage(message)


message = 'Lorem'
application = QApplication(sys.argv)
main_window = QMainWindow()
menu_bar = main_window.menuBar()
menu_1 = menu_bar.addMenu('Menu 1')
status_bar = main_window.statusBar()
action_1 = menu_1.addAction('Action 1')
action_1.triggered.connect(lambda: slot_example_1(status_bar, message))

main_window.show()
application.exec()
