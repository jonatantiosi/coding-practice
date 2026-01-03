# criacao de senha
# pode ser usado direto no terminal com python -c
import string as s
from secrets import SystemRandom as Sr
senha = ''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12))
print(senha)
