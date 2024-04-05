# EX19.
# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo: Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

# **import random
# amostra aleatoriamente 50 números do intervalo 0...500
# random_list = random.sample(range(500),50)

# Use as variáveis abaixo para representar cada operação matemática:
#+ mediana
# + media
# + valor_minimo 
# + valor_maximo 

# Importante: Esperamos que você utilize as funções abaixo em seu código:
# + random
# + max
# + min
# + sum

import random

# amostra aleatoriamente 50 números do intervalo 0...500                                        
random_list = random.sample(range(500), 50)

valor_minimo = min(random_list)
valor_maximo = max(random_list)
valor_soma = sum(random_list)
media = valor_soma / len(random_list)

random_list.sort()

tam_list = len(random_list)

# mediana é o número central de uma lista de dados, logo, se for par, não há "centro"
if tam_list % 2 == 0:
    indice1 = tam_list // 2 - 1
    indice2 = tam_list // 2
    mediana = (random_list[indice1] + random_list[indice2]) / 2
else:
    indice = tam_list // 2
    mediana = random_list[indice]

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")