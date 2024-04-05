# EX12.
# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.

# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']**_

import json

with open("person.json", "r") as arquivo:
    conteudo_json = arquivo.read()

dados = json.loads(conteudo_json)

print(dados)