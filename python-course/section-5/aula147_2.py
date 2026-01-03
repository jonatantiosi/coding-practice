# Exemplo de uso de dunder methods (métodos mágicos)
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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # representation of object
        # mais usadado para outros desenvolvedores
        # fallback de __str__
        class_name = self.__class__.__name__
        # class_name = type(self).__name__
        return f'{class_name}({self.x!r},{self.y!r})'
    
    def __add__(self, other):
        new_x = self.x + other.x 
        new_y = self.y + other.y
        return Point(new_x, new_y)
    
    def __gt__(self, other):
        # greater than
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other
    
    def __lt__(self, other):
        # less than
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self < resultado_other
    
if __name__ == '__main__':
    p1 = Point(4, 2)
    p2 = Point(6, 4)
    p3 = p1 + p2
    print(p3)
    print('p1 é maior que p2:', p1 > p2)
    print('p1 é menos que p2:', p1 < p2)


