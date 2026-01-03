# secrets gera números aleatórios seguros
import secrets

random = secrets.SystemRandom()

# print(secrets.randbelow(100))
# print(secrets.choice([10, 11, 12]))

# nesse caso random.seed nao faz nada

r_range = random .randrange(10, 20, 2)
print('randrange:', r_range)

r_int = random.randint(10, 20)
print('randit:', r_int)

r_uniform = random.uniform(10, 20)
print('uniform:', r_uniform)

nomes = ['Jonatan', 'Paulo', 'Tiosi', 'Santana']
random.shuffle(nomes)
print('shuffle:', nomes)

nomes_2 = ['Jonatan', 'Paulo', 'Tiosi', 'Santana']
novos_nomes = random.sample(nomes_2, k=2)
print('sample:', novos_nomes)

nomes_3 = ['Jonatan', 'Paulo', 'Tiosi', 'Santana']
novos_nomes_2 = random.choices(nomes, k=5)
print('choices:', novos_nomes_2)

print('choice:', random.choice(nomes))

# criacao de senha
# pode ser usado direto no terminal com python -c
import string as s
from secrets import SystemRandom as Sr
senha = ''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12))
print(senha)
