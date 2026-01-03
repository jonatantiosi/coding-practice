"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
metodo abstrato sacar
implementado pelas subclasses

    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Cliente -> Conta
        (agregacao)

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    mretodo depositar
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método <--.
"""
from abc import ABC, abstractmethod



class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        # super().__init__()
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self): ...
    'Método abstrato implementado pelas subclases ContaCorrente e ContaPoupança'

    def depositar(self, valor):
        'Adiciona valor ao saldo'    
        self.saldo += valor
        print(f'R${valor} depositado à conta: Saldo atual:{self.saldo}')

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite_extra):
        super().__init__(agencia, numero_conta, saldo)
        self.limite_extra = limite_extra

    def sacar(self, quantidade, banco: 'Banco', cliente:'Cliente'):
        'Precisa receber quantidade, banco e cliente'
        'Permite saque até o máximo do limite extra passado na criação da conta'
        if banco.autentica_transacao(cliente, self):

            if self.saldo - quantidade < (- self.limite_extra):
                # Se tentar sacar valor maior que o limite extra
                print('Saldo insuficiente')

            elif self.saldo - quantidade < 0 and \
                self.saldo - quantidade > - self.limite_extra:
                # Saque com limite extra se não extrapolar o valor
                self.saldo -= quantidade
                limite_extra =  self.saldo
                print(f'Saque realizado utilizando limite extra. Saldo restante:'
                      f'{self.saldo:.2f}')
            
            else:
                # Saque padrão
                self.saldo -= quantidade
                print(f'Saque de R${quantidade:.2f} realizado com sucesso')

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, quantidade, banco: 'Banco', cliente:'Cliente'):
        'Precisa receber quantidade, banco e cliente'
        if banco.autentica_transacao(cliente, self):
            if self.saldo - quantidade < 0:
                print('Saldo insuficiente')
            else:
                self.saldo -= quantidade
                print(f'Saque de R${quantidade:.2f} realizado com sucesso')


class Pessoa(ABC):
    def __init__(self):
        # super().__init__()
        self.nome = 'Desconhecido'
        self.idade = 'Desconhecida'

    @property
    def get_nome(self):
        return self.nome

    @get_nome.setter
    def get_nome(self, nome):
        self.nome = nome

    @property
    def get_idade(self):
        return self.nome

    @get_idade.setter
    def get_idade(self, idade):
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, conta: Conta):
        super().__init__()
        self.conta = conta
    
    def __repr__(self):
        return f'{self.__class__.__name__}: {self.nome}, {self.idade} anos.'

class Banco:
    def __init__(self, agencia):
        self.agencia = agencia
        self.clientes = []
        self.contas = []

    def inclui_cliente(self, cliente: Cliente):
        'Inclui cliente da classe Cliente em uma lista'
        self.clientes.append(cliente)

    def inclui_conta(self, conta: Conta):
        'Inlcui conta da classe Conta numa lista, valida agencia do Banco'
        if conta.agencia == self.agencia:
            self.contas.append(conta)
        else:
            print('Conta com agencia de banco desconhecido')

    def autentica_transacao(self, cliente: Cliente, conta: Conta):
        'Verifica se os parametros cliente e conta estão na lista de incluidos'
        if cliente in self.clientes and conta in self.contas:
            print('Transação autorizada')
            return True
        print('Transação não autorizada')
        return False


# Criação das contas corrente e poupança
conta_1 = ContaCorrente('0001', '21092001', 3487.23, 1000)
conta_2 = ContaPoupanca('0002', '19091979', 8347.57)

# Criação clientes 
cliente_1 = Cliente(conta_1)
cliente_1.nome, cliente_1.idade  = 'Jonatan', 23
cliente_2 = Cliente(conta_2)
cliente_2.nome, cliente_2.idade  = 'Miriam', 46
# Mostra clientes criados
print(cliente_1)
print(cliente_2)
print()

# Criação bancos
banco_1 = Banco('0001')
banco_2 = Banco('0002')

# Teste de depósito
conta_1.depositar(4353.76)
conta_2.depositar(6455.65)
print()

# Inclui cliente 1 e sua conta no banco 1
banco_1.inclui_cliente(cliente_1)
banco_1.inclui_conta(cliente_1.conta)

# Inclui cliente 2 e sua conta no banco 2
banco_2.inclui_cliente(cliente_2)
banco_2.inclui_conta(cliente_2.conta)

# Teste saque cliente 1 no banco 1
conta_1.sacar(2782, banco_1, cliente_1)
# Teste saque cliente 2 no banco 2
conta_2.sacar(2187, banco_2, cliente_2)
# Teste saque cliente 1 no banco 2
conta_1.sacar(2782, banco_2, cliente_1)
# Teste saque cliente 2 no banco 1
conta_2.sacar(2187, banco_1, cliente_2)
print()

# Teste saque limite extra conta corrente. o + 999 é para fins de teste e só
# funciona se o saldo estiver positivo
conta_1.sacar(conta_1.saldo + 999, banco_1, cliente_1)
#Teste saque excedendo limite conta corrente
conta_1.sacar(10000, banco_1, cliente_1)
#Teste saque excedendo limite conta poupanca
conta_2.sacar(conta_2.saldo + 999, banco_2, cliente_2)

















