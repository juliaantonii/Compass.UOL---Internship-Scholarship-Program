import csv

dados = []

nome_arquivo = 'estudantes.csv'

with open(nome_arquivo, newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        nome = linha[0]
        notas = list(map(int, linha[1:]))
        dados.append((nome, notas))

media_tres_maiores = lambda notas: round(sum(sorted(notas)[-3:]) / 3, 2)

dados_ordenados = sorted(dados, key=lambda x: x[0])

for nome, notas in dados_ordenados:
    tres_maiores_notas = list(map(int, sorted(notas, reverse=True)[:3]))
    media = media_tres_maiores(notas)
    
    print(f"Nome: {nome} Notas: {tres_maiores_notas} Média: {media}")