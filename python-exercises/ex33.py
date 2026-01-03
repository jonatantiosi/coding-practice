'''
Crie um decorator chamado @my_planet que modifica o comportamento da função
decorada:

    Se o planeta passado for "Earth", retorne "You are in home".

    Se for "Mars", retorne "You are in danger".

    Senão, retorne "Unknown planet".

Use esse decorator em uma função say_planet(planet).

'''


class Planet:
    def __init__(self, name):
        self.name = name


def my_planet(func):
    def inner(planet: Planet):
        if planet.name == 'Earth':
            return 'You are in home.'
        elif planet.name == 'Mars':
            return 'You are in danger.'
        return f'{func(planet)}. Unknown planet'
    return inner


@my_planet
def say_planet(planet):
    return f'You are on {planet.name}'


earth = Planet('Earth')
mars = Planet('Mars')
venus = Planet('Venus')

print(say_planet(mars))
print(say_planet(earth))
print(say_planet(venus))
