'''
Tarefa: escreva mini-aplicação que mantém uma lista de tarefas em tarefas.json:
funções ler(), salvar(), adicionar(tarefa), listar(). Garanta que cria o
arquivo caso não exista. (Esse tema aparece no merged).
Conceitos: json.dump/load, FileNotFoundError, with open.
'''
import json

CAMINHO = (
    r'C:\Users\Jonatan\Desktop\PythonCoding\exercicios_extra\chatgpt'
    r'\lista_tarefas.json'
)

try:
    with open(CAMINHO, 'r', encoding='utf-8') as arquivo:
        lista_tarefas = json.load(arquivo)
except FileNotFoundError:
    print('Arquivo não encontrado, criando novo...')
    with open(CAMINHO, 'w', encoding='utf-8') as arquivo:
        lista_tarefas = []
        json.dump(lista_tarefas, arquivo, indent=4)


def adicionar(*tarefas):
    for tarefa in tarefas:
        lista_tarefas.append(tarefa)


def salvar():
    with open(CAMINHO, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4)


def listar():
    for i, tarefa in enumerate(lista_tarefas, 1):
        print(f'{i}: {tarefa}')


adicionar(
    'assistir serie em alemao',
    'anki cards algebra linear',
    'pesquisas intercambio'
)

listar()
salvar()
