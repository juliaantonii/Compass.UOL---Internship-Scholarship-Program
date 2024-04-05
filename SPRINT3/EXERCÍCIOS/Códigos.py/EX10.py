# EX10.
# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.

# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def tirar_duplicados(lista):
    conjunto_sem_duplicatas = set(lista)
    nova_lista = list(conjunto_sem_duplicatas)
    return nova_lista

entrada = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

saida = tirar_duplicados(entrada)

print(saida)