import contas
import pessoas


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_conta_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_conta_cliente', True)
            return True
        print('_checa_conta_cliente', False)
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self. _checa_conta(conta) and \
            self._checa_conta_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f'{class_name}({attrs})'


if __name__ == '__main__':
    cliente_1 = pessoas.Cliente('Luiz', 30)
    conta_corrente_1 = contas.ContaCorrente(111, 222, 0, 0)
    cliente_1.conta = conta_corrente_1

    cliente_2 = pessoas.Cliente('Maria', 18)
    conta_poupanca_1 = contas.ContaPoupanca(112, 223, 100)
    cliente_2.conta = conta_poupanca_1

    banco_1 = Banco()
    banco_1.clientes.extend([cliente_1, cliente_2])
    banco_1.contas.extend([conta_poupanca_1, conta_corrente_1])
    banco_1.agencias.extend([111, 222])

    if banco_1.autenticar(cliente_1, conta_corrente_1):
        conta_corrente_1.depositar(10)
        cliente_1.conta.depositar(100)
        print(cliente_1.conta)
