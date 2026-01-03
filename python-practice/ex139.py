'''
139 — Criar janela principal com layout básico
Tarefa: crie uma aplicação gráfica que abra uma janela principal, defina um
título e utilize um layout vertical como base da interface.
Conceitos: QApplication(sys.argv), QMainWindow, QWidget, QVBoxLayout,
setCentralWidget().
'''
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout)
import sys

application = QApplication(sys.argv)
main_window = QMainWindow()
central_widget = QWidget()
layout = QVBoxLayout()

central_widget.setLayout(layout)  # !!
main_window.setCentralWidget(central_widget)
main_window.setWindowTitle("Título")  # !!
main_window.show()  # !!

application.exec()
