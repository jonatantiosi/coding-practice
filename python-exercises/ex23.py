from abc import ABC, ABCMeta, abstractmethod

class Logger(ABC):
    @abstractmethod
    def _log(self, msg):
        ...
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
class LoggerPrint(Logger):
    def _log(self, msg):
        print(f'{msg}')
        
log_1 = LoggerPrint()
log_1.log_success('Lorem')
log_1.log_error('Ipsum')

    

    