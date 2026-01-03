import json

pessoas = {
    "pessoa1": {  # Chave string
        "name": "Jonatan", 
        "surname": "Tiosi", 
        "age": 23,
        "addresses": [
            {"line1": "av. brasil"},
            {"line2": "av. sao paulo"}
        ]
    },
    "pessoa2": {"name": "Miriam", "surname": "Tiosi", "age": 45},
    "teste1": (1, 2, 3),
    # tuplas sao convertidas para lista (array) e voltam como listas
    "teste2": True
}
 
with open('aula117.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoas, 
        arquivo,
        indent=2
)

with open('aula117.json', 'r', encoding='utf-8') as arquivo:
    pessoas = json.load(arquivo)
    print(pessoas)
    print(type(pessoas))

    