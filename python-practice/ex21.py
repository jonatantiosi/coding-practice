class A:
    def __init__(self):
        pass
    
    def falar(self):
        print('A')

class B(A):
    def __init__(self):
        pass
    
    def falar(self):
        print('B')

    
class C(A):
    def __init__(self):
        pass
    
    def falar(self):
        print('C')

class D(B, C):
    def __init__(self):
        pass
    
    def falar(self):
        print('D')


d = D()
d.falar()
print(D.mro())