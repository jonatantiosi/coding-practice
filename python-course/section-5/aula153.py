# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe ser "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome, *args, **kwargs):
        print(nome, 'está chamando', self.phone)
        # return 123

call_1 = CallMe('12123412')

call_1('Jonatan')