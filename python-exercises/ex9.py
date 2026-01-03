try:
    import sys
    sys.path.append(r'C:\Users\Jonatan\Desktop\cursopython\meu_pacote')
    
except ModuleNotFoundError as error:
    print(error.__class__.__name__)

print(*sys.path, sep='\n')

from meu_pacote.utils import saudacao

nome = input('nome: ')
print(saudacao(nome))
