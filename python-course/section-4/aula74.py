'''
closure e funcoes que retornam outras funcoes
'''


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

saudacao_bom_dia = criar_saudacao('bom dia')
saudacao_boa_noite = criar_saudacao('boa noite')


print(saudacao_bom_dia('jonatan'))
print(saudacao_boa_noite('paulo'))
