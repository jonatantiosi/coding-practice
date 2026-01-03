'''
129 — Layout vertical com botões
 Tarefa: organize três botões verticalmente dentro da janela.
 Conceitos: QVBoxLayout, QWidget.setLayout.
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, \
    QVBoxLayout, QPushButton

application = QApplication(sys.argv)
main_window = QMainWindow()
central_widget = QWidget()
layout = QVBoxLayout()
button_1 = QPushButton('1')
button_2 = QPushButton('2')
button_3 = QPushButton('3')

main_window.setCentralWidget(central_widget)
central_widget.setLayout(layout)

layout.addWidget(button_1)  # !!
layout.addWidget(button_2)
layout.addWidget(button_3)

main_window.show()
application.exec()
