'''
Tarefa: copie o conteúdo da pasta 'Pictures/SolidColors' para
'Pictures/SolidColorsCopy', mantendo toda a estrutura interna
(subpastas e arquivos).
Conceitos: os.walk, os.makedirs, shutil.copy, os.path.join.
'''
import os
import shutil

CAMINHO = os.path.join(r'C:\Users', 'Jonatan', 'Pictures', 'SolidColors')
NOVO_CAMINHO = CAMINHO.replace('SolidColors', 'SolidColorsCopy')

# os.makedirs(NOVO_CAMINHO, exist_ok=True)

shutil.copytree(CAMINHO, NOVO_CAMINHO, dirs_exist_ok=True)
