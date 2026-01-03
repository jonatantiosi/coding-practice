'''
Tarefa: crie uma cópia de 'Pictures/SolidColors' chamada
'Pictures/SolidColorsCopy' e renomeie-a para 'Pictures/SolidColorsBackup'.
Conceitos: shutil.copytree, shutil.move, os.path.join.
'''
import os
import shutil

CAMINHO = os.path.join(r'C:\Users', 'Jonatan', 'Pictures', 'SolidColors')
CAMINHO_COPY = CAMINHO.replace('SolidColors', 'SolidColorsCopy')
CAMINHO_BACKUP = CAMINHO_COPY.replace('SolidColorsCopy', 'SolidColorsBackup')


shutil.copytree(CAMINHO, CAMINHO_COPY, dirs_exist_ok=True)
shutil.move(CAMINHO_COPY, CAMINHO_BACKUP)
