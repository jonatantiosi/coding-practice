# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

# e.g. terminal (chave valor): python .\AulasUdemy\aula188.py -b 123 
parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str,  # tipo do argumento
    metavar='STRING',
    # default='Olá Mundo',  # valor padrao
    required=False,
    # nargs='+',  # recebe mais de um valor 
    # python .\AulasUdemy\aula188.py -b "A" "B" "C"
    action='append',  # recebe mais de um valor
    # python .\AulasUdemy\aula188.py -b "A" -b "B" -b "C"
    )

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
    )
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('Valor de basic:', args.basic)

print(args.verbose)