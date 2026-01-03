'''
127 — Janela principal
 Tarefa: crie uma aplicação com uma janela principal e exiba-a corretamente.
 Conceitos: QMainWindow.
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

application = QApplication(sys.argv)
main_window = QMainWindow()

main_window.show()
application.exec()
