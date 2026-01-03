'''
141 — Adicionar elemento de texto à interface
 Tarefa: crie um elemento de texto grande e o insira no layout vertical da
 janela principal.
 Conceitos: QLabel, setStyleSheet(), addWidget().
'''
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QLabel)
import sys

application = QApplication(sys.argv)
main_window = QMainWindow()
central_widget = QWidget()
layout = QVBoxLayout()

label_1 = QLabel('Lorem')
label_1.setStyleSheet('font-size: 50px')
layout.addWidget(label_1)

central_widget.setLayout(layout)
main_window.setCentralWidget(central_widget)
main_window.setWindowTitle("Título")
main_window.show()

main_window.adjustSize()
main_window.setFixedSize(main_window.size())

application.exec()
