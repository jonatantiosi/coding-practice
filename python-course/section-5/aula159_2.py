from dataclasses import dataclass, asdict, astuple


@dataclass(order=True, repr=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome:  str


if __name__ == '__main__':
    pessoa_1 = Pessoa('Luiz', 'Otávio')
    print(asdict(pessoa_1))
    print(asdict(pessoa_1).keys())
    print(astuple(pessoa_1))
    print(astuple(pessoa_1)[0])
