# Seção 4: Exercícios Python I - 2/2

_**EX6.**
Considere as duas listas abaixo:_

_**a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]\
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]**_

_Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições), imprimindo a lista de valores da interseção na saída padrão._

_Importante:  Esperamos que você utilize o construtor **set()** em seu código._

**_Resposta:_**

```python
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

set_a = set(a)
set_b = set(b)

interseção = set_a & set_b

result = list(interseção)
```

&nbsp;

_**EX7.**
Dada a seguinte lista:_

_**a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]**_

_Faça um programa que gere uma nova lista contendo apenas números ímpares._

**_Resposta:_**

```python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

impar = [num for num in a if num % 2 != 0]

print(impar)
```

&nbsp;

_**EX8.**
Verifique se cada uma das palavras da lista **['maça', 'arara', 'audio', 'radio', 'radar', 'moto']** é ou não um palíndromo. Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente._

_É necessário que você imprima no console exatamente assim:_

+ _**A palavra:** maça não é um palíndromo_
+ _**A palavra:** arara é um palíndromo_
+ _**A palavra:** audio não é um palíndromo_
+ _**A palavra:** radio não é um palíndromo_
+ _**A palavra:** radar é um palíndromo_
+ _**A palavra:** moto não é um palíndromo_

**_Resposta:_**

```python
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for element in palavras:
    if element == element[::-1]:
        print(f"A palavra: {element} é um palíndromo")
    else:
        print(f"A palavra: {element} não é um palíndromo")
```

&nbsp;

_**EX9.**
Dada as listas a seguir:_

+ _primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']_
+ _sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']_
+ _idades = [19, 28, 25, 31]_

_Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos". Você deve Utilizar a função **enumerate()**._

_Exemplo:_

_0 - João Soares está com 19 anos_

**_Resposta:_**

```python
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, primeiroNome in enumerate(primeirosNomes):
    sobrenome = sobreNomes[indice]
    idade = idades[indice]
    print (f"{indice} - {primeiroNome} {sobrenome} está com {idade} anos")
```

&nbsp;

_**EX10.**
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função._

_**['abc', 'abc', 'abc', '123', 'abc', '123', '123']**_

**_Resposta:_**

```python
def tirar_duplicados(lista):
    conjunto_sem_duplicatas = set(lista)
    nova_lista = list(conjunto_sem_duplicatas)
    return nova_lista

entrada = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

saida = tirar_duplicados(entrada)

print(saida)
```

&nbsp;

_**EX11.**
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo._

_Dica: leia a documentação da função **open(...)**_

**_Resposta:_**

```python
with open("arquivo_texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo, end='')
```

&nbsp;

_**EX12.**
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função._

_**['abc', 'abc', 'abc', '123', 'abc', '123', '123']**_

**_Resposta:_**

```python
import json

with open("person.json", "r") as arquivo:
    conteudo_json = arquivo.read()

dados = json.loads(conteudo_json)

print(dados)
```

&nbsp;

_**EX13.**
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função._

_**['abc', 'abc', 'abc', '123', 'abc', '123', '123']**_

**_Resposta:_**

```python
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
```

&nbsp;

_**EX14.**
Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido. Teste sua função com os seguintes parâmetros:_

_**(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)**_

**_Resposta:_**

```python
def print_parameters(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_parameters(1, 3, 4, 'hello', 'alguma coisa', 20)
```

&nbsp;

_**EX15.**
Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, True se a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:_

+ _**liga():** muda o estado da lâmpada para ligada_
+ _**desliga():** muda o estado da lâmpada para desligada_
+ _**esta_ligada():** retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário_

_Para testar sua classe:_

+ _Ligue a Lampada_
+ _Imprima: A lâmpada está ligada? True_
+ _Desligue a Lampada_
+ _Imprima: A lâmpada ainda está ligada? False_

**_Resposta:_**

```python
class Lampada:
    def __init__(self, ligada = False):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada

lampada = Lampada()
lampada.liga()

print("A lâmpada está ligada?", lampada.esta_ligada())

lampada.desliga()
print("A lâmpada ainda está ligada?", lampada.esta_ligada())
```

&nbsp;

_**EX16.**
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores._

_A string deve ter valor **"1,3,4,6,10,76"**_

**_Resposta:_**

```python
def soma_string_numeros(string_numeros):
    numeros = string_numeros.split(',')
    soma = sum(map(int, numeros))
    return soma

string_numeros = "1,3,4,6,10,76"
soma_total = soma_string_numeros(string_numeros)
print(soma_total)
```

&nbsp;

_**EX17.**
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo_

_**lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]**_

**_Resposta:_**

```python
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
```

&nbsp;

_**EX18.**
Dado o dicionário a seguir:_

_**speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}**_

_Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados._

**_Resposta:_**

```python
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

valores = list(speed.values())

valores_sem_duplicados = list(set(valores))

print(valores_sem_duplicados)
```

&nbsp;

_**EX19.**
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo: Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!_

_**import random\
\# amostra aleatoriamente 50 números do intervalo 0...500\
random_list = random.sample(range(500),50)**_


Use as variáveis abaixo para representar cada operação matemática:

+ mediana
+ media
+ valor_minimo 
+ valor_maximo 

Importante: Esperamos que você utilize as funções abaixo em seu código:

+ random
+ max
+ min
+ sum

**_Resposta:_**

```python
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
```

&nbsp;

_**EX20.**
Imprima a lista abaixo de trás para frente._

_**a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89].**_

**_Resposta:_**

```python
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

a.reverse()

print(a)
```

---