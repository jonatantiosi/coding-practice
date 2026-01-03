# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial



class Foo:
    def __init__(self):
        self.public = 'público'
        self._protected = 'protegido'
        self.__private = 'privado'

    def metodo_publico(self):
        print(self.__private)
        self.__metodo_private()
        return 'metodo_público'
    
    def _metodo_protected(self):
        return 'não deveria ser acessado, por convencao'
    
    def __metodo_private(self):
        print('metodo privado')
        
    
f = Foo()
        
print(f.public)
print(f.metodo_publico())
print(f'{f._protected}, {f._metodo_protected()}')