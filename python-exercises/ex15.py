class ContaBancaria:
    senha_padrao = 11283712983

    def __init__(self, dono='Desconhecido', saldo=0, senha=senha_padrao):
        self.dono = dono
        self.__senha = senha
        self._saldo = saldo

    def exibir_saldo(self):
        print(f'Saldo atual = R${self._saldo:.2f}')

    def __verificar_senha(self):
        print('Verificando senha...')
        print(self.__senha)

conta_1 = ContaBancaria('Jonatan Tiosi', 2334.32, 21367821)

conta_1.exibir_saldo()
try:
    conta_1.__verificar_senha()
except AttributeError:
    print('Função protegida')

dono_1 = conta_1.dono
print('Dono: ', dono_1)

saldo_1 = conta_1._saldo
# por convencao nao deveria ser feito
print('Saldo: ', saldo_1)

try:
    senha_1 = conta_1.__senha
    print(senha_1)
except AttributeError:
    print('Atributo protegido')