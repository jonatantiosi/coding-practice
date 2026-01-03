'''
120 — Acessar célula específica com tipagem
Tarefa: leia o valor de uma célula específica (ex.: “B3”), imprima o valor e
depois atualize-o, garantindo tipagem correta.
Conceitos: Worksheet.getitem, openpyxl.cell.Cell, typing.cast.
'''
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell import Cell
from pathlib import Path
from typing import cast


ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / 'workbook_new.xlsx'

workbook = cast(Workbook, load_workbook(WORKBOOK_PATH))
worksheet = cast(Worksheet, workbook.active)


cell_b3 = cast(Cell, worksheet['B3'])  # !!
print(cell_b3.value)
cell_b3.value = 25  # !!

workbook.save(WORKBOOK_PATH)  # !!
