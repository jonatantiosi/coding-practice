'''
132 — Menu com ação simples
 Tarefa: crie um menu na interface com uma ação simples, sem comportamento.
 Conceitos: QMainWindow.menuBar(), addMenu, QAction.
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

application = QApplication(sys.argv)
main_window = QMainWindow()
menu_bar = main_window.menuBar()
menu_1 = menu_bar.addMenu('Menu 1')
action_1 = menu_1.addAction('Action 1')

main_window.show()
application.exec()
