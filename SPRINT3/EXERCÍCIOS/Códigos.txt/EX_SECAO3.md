# Seção 3: Exercícios Python I - 1/2

_**EX1.**
Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. Como saída, imprima o ano em que a pessoa completará 100 anos de idade._

**_Resposta:_**

```python
nome = input("nome:")
idade = int(input("idade:"))

ano_atual = 2023
ano_c100 = ano_atual + (100 - idade)

print(ano_c100)
```

&nbsp;

_**EX2.**
Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido)._

_Importante: Aplique a função **range()** em seu código._

_Exemplos de saída:_

_Par: 2\
Ímpar: 3_

**_Resposta:_**

```python
for numero in range(3):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        resultado = "Par:"
    else:
        resultado = "Ímpar:"
    print(resultado, numero)
```

&nbsp;

_**EX3.**
Escreva um código Python para imprimir os números pares de 0 até 20 (incluso). Importante: Aplique a função **range()** em seu código._

**_Resposta:_**

```python
for numero in range(0,21):
    if numero % 2 == 0:
        print(numero)
```

&nbsp;

_**EX4.**
Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não._

_Importante: Aplique a função **range()**._

**_Resposta:_**

```python
for num in range(2, 101):
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)
```

&nbsp;

_**EX5.**
Escreva um código Python que declara 3 variáveis:_

+ _**dia**, inicializada com valor 22;_
+ _**mes**, inicializada com valor 10;_
+ _**ano**, inicializada com valor 2022._

_Como saída, você deverá imprimir a data correspondente, no formato a seguir: **dia/mes/ano.**_

**_Resposta:_**

```python
dia = 22
mes = 10
ano = 2022

print(f'{dia}/{mes}/{ano}')
```

---