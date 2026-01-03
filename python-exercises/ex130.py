'''
130 — Layout em grade
 Tarefa: organize três botões em linhas e colunas diferentes.
 Conceitos: QGridLayout, addWidget(row, column[, rowSpan, columnSpan]).
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, \
    QGridLayout, QPushButton

application = QApplication(sys.argv)
main_window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()
button_1 = QPushButton('1')
button_2 = QPushButton('2')
button_3 = QPushButton('3')

main_window.setCentralWidget(central_widget)
central_widget.setLayout(layout)

layout.addWidget(button_1, 1, 1)
layout.addWidget(button_2, 2, 2)
layout.addWidget(button_3, 3, 3)

main_window.show()
application.exec()
