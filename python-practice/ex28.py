'''
28. Dunder __add__ e __gt__

Crie a classe ContaBancaria com saldo.
Implemente:

    __add__ para somar saldos entre contas.

    __gt__ para comparar qual conta tem mais saldo.
    Crie duas contas e teste os operadores + e >.
'''

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def __add__(self, other: 'BankAccount'):
        return self.balance + other.balance
    
    def __gt__(self, other: 'BankAccount'):
        return self.balance > other.balance
    

account_1 = BankAccount(2000)
account_2 = BankAccount(3000)

print(account_1 + account_2)
print(account_1 > account_2)
print(account_1 < account_2)