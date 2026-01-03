try:
    import sys
    sys.path.append(r'c:\Users\Jonatan\Desktop')
except ModuleNotFoundError:
    ...

# primeiro modulo chama-se __main__

import modulo_python
print(modulo_python)

print('este modulo chama', __name__)


import aula97_m
from aula97_m import variavel_modulo2
print(variavel_modulo2)

print(aula97_m.variavel_modulo)



# python nao reconhece coisas acima e.g. pastas(pacotes)

print(*sys.path, sep='\n')