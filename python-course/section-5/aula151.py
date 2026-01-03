# Decorator functions, Class-based decorators

def add_repr(cls):
    # using composition
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls
    

class MyReprMixin:
    # using inheritance
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    

class Team(MyReprMixin):
    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr

# syntax sugar
@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

# Planet = add_repr(Planet)

brazil = Team('Brazil')
portugal = Team('Portugal')

earth = Planet('Earth')
mars = Planet('Mars')

print(brazil)
print(mars)