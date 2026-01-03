'''
140 — Ajustar tamanho fixo da janela após montagem
Tarefa: após adicionar todos os elementos visuais à janela, ajuste
automaticamente o tamanho e impeça redimensionamento manual.
Conceitos: adjustSize(), setFixedSize().
'''
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout)
import sys

application = QApplication(sys.argv)
main_window = QMainWindow()
central_widget = QWidget()
layout = QVBoxLayout()

central_widget.setLayout(layout)
main_window.setCentralWidget(central_widget)
main_window.setWindowTitle("Título")
main_window.show()

main_window.adjustSize()
main_window.setFixedSize(main_window.width(), main_window.height())

application.exec()
