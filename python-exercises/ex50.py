'''
50 — __add__ e __gt__ com conta bancária
Tarefa: crie Conta(saldo) com __add__ que retorna nova Conta com soma dos
saldos (em vez de número) e __gt__ para comparação por saldo.
Teste c3 = c1 + c2.
 Conceitos: dunder __add__, retornar instância, comparação.
'''


class Conta:

    def __init__(self, saldo):
        self.saldo = saldo

    def __add__(self, other: 'Conta'):
        return Conta(self.saldo + other.saldo)

    def __gt__(self, other: 'Conta'):
        return self.saldo > other.saldo

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.saldo}$'


conta_1 = Conta(3242)
conta_2 = Conta(2378)
conta_3 = conta_1 + conta_2

print(conta_3)
print(conta_1 > conta_2)
