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

def my_planet (method):
    def inner(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Earth' in result:
            return 'You are in home'
        return result
    return inner
    

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

    @my_planet
    def say_name(self):
        return f'Planet is {self.name}'

# Planet = add_repr(Planet)

brazil = Team('Brazil')
portugal = Team('Portugal')

earth = Planet('Earth')
mars = Planet('Mars')

print(brazil)
print(mars)

print(earth.say_name())
print(mars.say_name())