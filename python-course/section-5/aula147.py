# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Point:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        # string representation
        return f'({self.x},{self.y})'

    def __repr__(self):
        # representation of object
        # mais usadado para outros desenvolvedores
        # fallback de __str__
        class_name = self.__class__.__name__
        # class_name = type(self).__name__
        return f'{class_name}({self.x!r},{self.y!r},{self.z!r})'

ponto_1 = Point(1, 2)
ponto_2 = Point(3, 4)

print(ponto_1)
print(f'{ponto_2!s}')
print()

print(repr(ponto_1))
print(f'{ponto_2!r}')
