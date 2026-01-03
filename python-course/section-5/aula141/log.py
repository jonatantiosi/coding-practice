# Abstração
# Herança - é um

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
                                # concatenacao

class Log:
    def _log(self, msg):
        # assinatura do metodo
        # template method
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    # adicionar coisas as outroas classes
    # assinatura tem que ser igual, nao mudar tipo nem retorno
    def _log(self, msg):
        print(msg)
        msg_formatada = f'{msg} - {self.__class__.__name__}'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
               arquivo.write(msg_formatada)
               arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} - {self.__class__.__name__}')

# if __name__ == '__main__':
#     lp = LogPrintMixin()
#     lp.log_error('error')
#     lp.log_success('success')
#     lf = LogFileMixin()
#     lf.log_error('error')
#     lf.log_success('success')

# print(LOG_FILE)