import random
import time
import os
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

caminho_do_arquivo = r'C:\Users\User\Desktop\Repositórios GitHub\Compass.UOL REPO\SPRINT8\ATV3\nomes_aleatorios.txt'

with open(caminho_do_arquivo, "w") as arquivo:
    for nome in dados:
        arquivo.write(nome + "\n")

print(f"Arquivo 'nomes_aleatorios.txt' gerado em {caminho_do_arquivo}")

with open(caminho_do_arquivo, "r") as arquivo:
    print("\nConteúdo do arquivo 'nomes_aleatorios.txt':")
    for i, linha in enumerate(arquivo):
        if i < 10: 
            print(linha.strip()) 
        else:
            break  
