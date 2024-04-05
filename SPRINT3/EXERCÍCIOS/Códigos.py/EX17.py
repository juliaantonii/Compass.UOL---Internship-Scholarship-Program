# EX17.
# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def divide_lista(lista):
    tamanho = len(lista)
    tamanho_parte = tamanho // 3
    
    part1 = lista[:tamanho_parte]
    part2 = lista[tamanho_parte:tamanho_parte*2]
    part3 = lista[tamanho_parte*2:]
    
    return part1, part2, part3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
part1, part2, part3 = divide_lista(lista)

print(part1, part2, part3)