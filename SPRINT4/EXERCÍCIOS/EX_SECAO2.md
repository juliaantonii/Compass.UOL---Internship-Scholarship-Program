# Exercícios de Programação - Python

_**EX1.**
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes. Você deverá aplicar as seguintes funções no exercício:_

+ **map;**

+ **filter;**

+ **sorted;**

+ **sum.**

_Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):_

+ **a lista dos 5 maiores números pares em ordem decrescente;**

+ **a soma destes valores.**

**_Resposta:_**

```python
with open('number.txt', 'r') as arquivo:
    numeros = list(map(int, (line.strip() for line in arquivo))) 

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

cinco_maiores_pares = numeros_pares_ordenados[:5]

soma = sum(cinco_maiores_pares)

print(cinco_maiores_pares)
print(soma)
```

&nbsp;

_**EX2.**
Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo. É obrigatório aplicar as seguintes funções:_

+ **len;**

+ **filter;**

+ **lambda.**

_Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código._

**_Resposta:_**

```python
def conta_vogais(texto: str) -> int:
    texto = texto.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

    is_vogal = lambda char: char in 'aeiou'

    vogais = filter(is_vogal, texto)

    return len(list(vogais))
```

&nbsp;

_**EX3.**
A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). Abaixo apresentando uma possível entrada para a função._

_**lancamentos = [(200,'D'), (300,'C'), (100,'C')]**_

_A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200. Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:_

+ **reduce (módulo functools);**

+ **map.**

**_Resposta:_**

```python
def calcula_saldo(lancamentos) -> float:
    from functools import reduce

    calcular_valor = lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0]

    valores = map(calcular_valor, lancamentos)

    saldo_final = reduce(lambda x, y: x + y, valores, 0)
    
    return saldo_final
```

&nbsp;

_**EX4.**
A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles. Veja o exemplo:_

_**Entrada**_

+ **operadores = ['+','-','*','/','+'];**
+ **operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)].**

_Aplicar as operações aos pares de operandos_

**[ 3+6 , -7-4.9, 8\*-8 , 10/2 , 8+4 ]** 

_Obter o maior dos valores_

**12**

_Na resolução da atividade você deverá aplicar as seguintes funções:_

+ **max;**

+ **zip;**

+ **map.**

_**Resposta:**_

```python
def calcular_valor_maximo(operadores, operandos):
    operacoes = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '%': lambda x, y: x % y}

    resultados = list(map(lambda op, opd: operacoes[op](opd[0], opd[1]), operadores, operandos))
    
    maximo = float('-inf')
```

&nbsp;

_**EX5.**
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício._

_Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:_

+ **Nome do estudante;**

+ **Três maiores notas, em ordem decrescente;**

+ **Média das três maiores notas, com duas casas decimais de precisão;**

_O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:_

+ **Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>**

_Exemplo:_

+ **Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67**

+ **Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33**

_Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:_

+ **round;**

+ **map;**

+ **sorted.**

_**Resposta:**_

```python
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
```

&nbsp;

_**EX6.**
Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. O analista responsável descreveu o requisito funcional da seguinte forma:_

_Para realizar um cálculo de custo, o sistema deverá permitir filtrar um determinado conjunto de produtos, de modo que apenas aqueles cujo valor unitário for superior à média deverão estar presentes no resultado. Vejamos o exemplo:_

_Conjunto de produtos (entrada):_

+ **Arroz: 4.99;**

+ **Feijão: 3.49;**

+ **Macarrão: 2.99;**

+ **Leite: 3.29;**

+ **Pão: 1.99.**

_Produtos com valor acima da média:_

+ **Arroz: 4.99;**

+ **Feijão: 3.49.**

_Observe que estamos definindo a assinatura de uma função como parte de sua resposta. Você não pode mudá-la, apenas codificar seu corpo. O parâmetro conteudo é um dicionário cuja chave contém o nome do produto e o valor, o respectivo preço (ponto flutuante)._

_Observe um exemplo de valor para conteudo:_

**{\
    "arroz": 4.99,\
    "feijão": 3.49,\
    "macarrão": 2.99,\
    "leite": 3.29,\
    "pão": 1.99\
}**

_O retorno da função obrigatoriamente deve ser uma lista. Cada elemento da lista é uma tupla em que a primeira posição contém o nome do produto e a segunda, o respectivo preço. Veja um exemplo de retorno:_

**[\
('feijão', 3.49),\
 ('arroz', 4.99)\
]**

_Importante: O retorno da função deve estar ordenado pelo preço do item (ordem crescente)._

_**Resposta:**_

```python
def maiores_que_media(conteudo: dict) -> list:
    
    valores = list(conteudo.values())
    media = sum(valores) / len(valores)
    
    produtos_acima_da_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]  

    produtos_acima_da_media = sorted(produtos_acima_da_media, key=lambda x: x[1])
    
    return produtos_acima_da_media
```

&nbsp;

_**EX7.**
_Generators são poderosos recursos da linguagem Python. Neste exercício, você deverá criar o corpo de uma função, cuja assinatura já consta em seu arquivo de início (def pares_ate(n:int):) ._

_O objetivo da função pares_ate é retornar um generator para os valores pares no intervalo [2,n] . Observe que n representa o valor do parâmetro informado na chamada da função._

_**Resposta:**_

```python
def pares_ate(n: int):
    for i in range(2, n + 1, 2):
        yield i

for numero in pares_ate(10):
    print(numero)
```

---