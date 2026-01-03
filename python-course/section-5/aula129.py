# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.
# nunca usei isso na minha vida

class Classe:
    @staticmethod
    def funcao_dentro_da_classe():
        print('a')

classe_1 = Classe()
classe_1.funcao_dentro_da_classe()
Classe.funcao_dentro_da_classe()