import os
import json

def listar(tarefas):
    print()
    if not tarefas:
        # lista vazia é falsy
        print('nenhuma tarefa para listar')
        return
        # usando return para parar a execucao da funcao
        # guard clause
    print('Tarefas')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()
    

def desfazer(tarefas, tarefas_desfazer):
    print()
    if not tarefas:
        # lista vazia é falsy
        print('nenhuma tarefa para desfazer')
        return
        # usando return para parar a execucao da funcao
    tarefa = tarefas.pop()
    print(f'{tarefa} removida da lista')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)

def refazer(tarefas, tarefas_desfazer):
    print()
    if not tarefas_refazer:
        # lista vazia é falsy
        print('nenhuma tarefa para refazer')
        return
        # usando return para parar a execucao da funcao
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa} adicionada da lista')
    print()
    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        # lista vazia é falsy
        print('você não digitou nenhuma tarefa')
        return
        # usando return para parar a execucao da funcao
    tarefas.append(tarefa)
    print(f'{tarefa} adicionada da lista')
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json. load(arquivo)
    except FileNotFoundError :
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            dados = json. dump(tarefas, arquivo, indent = 2)
    return dados



CAMINHO_ARQUIVO = r'aulas111-120\\aula.119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:

    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando:')

    comandos = {
        # lambda adia a execução da funcao
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa, tarefas),
        'clear': lambda: os.system('cls')
    }


    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else\
        comandos['adicionar']
    comando()

    salvar(tarefas, CAMINHO_ARQUIVO)

    # if tarefa == 'listar':
    #     listar(tarefas)

    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)

    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)

    # elif tarefa == 'clear':
    #     os.system('cls')

    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)

