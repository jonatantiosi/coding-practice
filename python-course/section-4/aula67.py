'''
refatorar: editar o código
'''


def soma(x, y, z=None):
    if z is not None:
        # anteriormente 'z=0, if z' dava Falsy e executava mesmo assim
        print(f'{x=}, {y=}, {z=}', x + y + z)
    else:
        print(f'{x=}, {y=}', x + y)

soma(3, 5)
soma(4, 6, 0)