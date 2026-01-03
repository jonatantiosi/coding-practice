'''
Conversão JSON ↔ dict
Tarefa: carregue uma string JSON em um dicionário Python com json.loads().
Depois, altere o valor de uma das chaves e converta de volta para JSON com
json.dumps().
Conceitos: json.loads, json.dumps, manipulação de dicionários.
'''
import json

string_json = '''{"Lorem": 0, "Ipsum": [2, 3]} '''
print('Inicialmente:', string_json)

# json para string
json_: dict = json.loads(string_json)

# alteração do valor da chave
json_["Lorem"] = 99

# string para json
string_json = json.dumps(json_)

print('Depois da alteraçao:', string_json)
