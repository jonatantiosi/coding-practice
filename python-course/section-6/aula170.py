# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

# "C:\Users\Jonatan\Pictures\Maple"

# caminho = r"C:\\Users\\Jonatan\\Pictures\\Maple"
# print(caminho)

import os

caminho = os.path.join('C:\\Users', 'Jonatan', 'Pictures', 'Maple')

# print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    # print(pasta)
    # print(caminho_completo_pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue
    print(pasta)
    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)