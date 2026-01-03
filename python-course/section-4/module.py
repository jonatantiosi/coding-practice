import json
import os

familia = [
    {"name": "Jonatan", 
    "surname": "Tiosi", 
    "age": 23,
    "addresses": [
        {"line1": "av. brasil"},
        {"line2": "av. sao paulo"}

    ]
},
    {"name": "Miriam", "surname": "Tiosi", "age": 45},
    {"name": "Marcio", "surname": "Santana", "age": 45}
]

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

# with open(JSON_FILE, 'w') as file:
#     json.dump(familia, file, indent=2)

# print(json.dumps(familia, indent=2))

with open(JSON_FILE, 'r') as file:
    pessoas = json.load(file)
    # print(pessoas)

    print(json.dumps(pessoas))

    # for pessoa in pessoas:
    #     print(pessoa['name'])

json_string = '''
[{"name": "Jonatan", "surname": "Tiosi", "age": 23, "addresses": [{"line1": "av. brasil"}, {"line2": "av. sao paulo"}]}, {"name": "Miriam", 
"surname": "Tiosi", "age": 45}, {"name": "Marcio", "surname": "Santana", "age": 45}]
'''

pessoas = json.loads(json_string)
# converte para lista

for pessoa in pessoas:
    print(pessoa['name'])
