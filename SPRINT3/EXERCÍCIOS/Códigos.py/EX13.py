# EX13.
# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.

# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def my_map(lst, f):
    result = []
    for item in lst:
        result.append(f(item))
    return result

def power_of_two(x):
    return x ** 2

entrada_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

saida_list = my_map(entrada_list, power_of_two)

print(saida_list)