# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)


class Connection:
    def __init__(self, host='localhost'):
        # método de instância
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        # setter
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        # authentication 
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print(msg)



# c1 = Connection()
c1 = Connection.create_with_auth('jonatan', 1234)



# c1.set_user('jonatan')
# c1.set_password(1234)

Connection.log('mensagem')
print(c1.user, c1.password)