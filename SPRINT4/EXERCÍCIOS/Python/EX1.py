with open('number.txt', 'r') as arquivo:
    numeros = list(map(int, (line.strip() for line in arquivo))) 

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

cinco_maiores_pares = numeros_pares_ordenados[:5]

soma = sum(cinco_maiores_pares)

print(cinco_maiores_pares)
print(soma)