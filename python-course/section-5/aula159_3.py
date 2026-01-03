from dataclasses import dataclass, field, fields


@dataclass(order=True, repr=True, frozen=False, init=True)
class Pessoa:
    nome: str = field(
        default='Missing'
    )
    sobrenome:  str = 'Not sent'
    idade: int = 0  # Apenas valores imutáveis
    # enderecos: list[str] = []  # Não funciona
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    pessoa_1 = Pessoa('Luiz', 'Otávio')
    print(pessoa_1)
    print(fields(pessoa_1))
