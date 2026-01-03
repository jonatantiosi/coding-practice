# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Qual a capital da Turquia?',
        'Opções': ['Bodrum', 'Istambul', 'Ankara', 'Jerusalem'],
        'Resposta': '3',
    },
    {
        'Pergunta': 'Qual o maior rio do mundo em volume de água?',
        'Opções': ['Amazonas', 'Nilo', 'Congo', 'Yangtze'],
        'Resposta': '1',
    },
    {
        'Pergunta': 'Qual dessas não é uma constelação?',
        'Opções': ['Cão maior', 'Lira', 'Arcadia', 'Pavão'],
        'Resposta': '3',
    },
]

# def pergunta(num):
#     return 'Pergunta:', perguntas[(num-1)]['Pergunta']
        
# pergunta1 =  pergunta(1) 
 

def pergunta(num):
    print('Pergunta:', perguntas[(num-1)]['Pergunta'])
    print('Opções:')
    for i, opcao in enumerate(perguntas[(num-1)]['Opções']):
        print(f'{i+1}){opcao}')


def reposta_valida(resposta, num):
    if resposta == perguntas[(num-1)]['Resposta']:
        return True
    return False

def valida_resposta(bool):
    if bool:
        print('Você acertou.')
        global respostas_corretas
        respostas_corretas += 1
    else:
        print('Você errou.')

def chama_pergunta(num):
    pergunta(num)
    resposta = input('')
    valida_resposta(reposta_valida(resposta, num))
    print()

respostas_corretas = 0


for i in range(3):
    chama_pergunta(i+1)
 
 
    # chama_pergunta(2)
    # chama_pergunta(3)


# pergunta(1)
# resposta1 = input('')
# valida_resposta(reposta_valida(resposta1, 1))
# print()

# pergunta(2)
# resposta1 = input('')
# valida_resposta(reposta_valida(resposta1, 2))
# print()

# pergunta(3)
# resposta1 = input('')
# valida_resposta(reposta_valida(resposta1, 3))
# print()


print(f'Você acertou {respostas_corretas} de 3 perguntas.')


# if reposta_valida(resposta1, 1):
#     print('Você acertou.')
#     respostas_corretas += 1
# else:
#     print('Você errou.')