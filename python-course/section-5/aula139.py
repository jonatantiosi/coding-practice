# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

class MinhaString(str):
    # super class
    def upper(self):
        print('Chamou upper')
        return super().upper()

string = MinhaString('Jonatan')
print(string.upper())

class A:
    atributo_a = 'valor a'
    def metodo(self):
        print('a')
    
    def __init__(self, atributo):
        self.atributo = atributo

class B(A):

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    atributo_b = 'valor b'
    def metodo(self):
        print('b')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def metodo(self):
        print(self.atributo)
        # classe atual
        super().metodo()
        # uma classe acima da classe atual
        super(B, self).metodo()    
        # uma classe acima da classe explicita
        # A.metodo(self) também funciona, mas é recomendável usar super()
        
print(C.mro())
# method resolution order

c = C('c', 'outra_coisa')
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
print(c.outra_coisa)