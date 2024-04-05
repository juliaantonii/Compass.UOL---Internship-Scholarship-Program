# 🔖 **SUMÁRIO**

Nesta página encontra-se 8 Tópicos Principais, são estes:

+ **[Python 3 - Curso Completo do Básico ao Avançado 1/2](#1-python-3---curso-completo-do-básico-ao-avançado-12);**
+ **[Variáveis e Tipos de Dados](#2-variáveis-e-tipos-de-dados);**
+ **[Operadores](#3-operadores);**
+ **[Conversão de Tipos e Coerções](#4-conversão-de-tipos-e-coerções);**
+ **[Estruturas de Controle](#5-estruturas-de-controle);**
+ **[Manipulação de Arquivos](#6-manipulação-de-arquivos);**
+ **[Exercícios e Desafios](#7-exercícios-e-desafio);**
+ **[Certificação](#📝-certificação).**

---

&nbsp;

# 1. Python 3 - Curso Completo do Básico ao Avançado 1/2

Devido a sua alta flexibilidade, Python é considerada uma das linguagens de programação mais simples e mais usadas pelo mundo. Esta possui sua sintaxe limpa, ou seja, contém alta legibilidade e clareza.

Durante os estudos podemos encontrar o "Zen do Python", este é um conjunto de princícios, explorando conceitos fundamentais para manter o código "elegante" e fácil. Abaixo vemos os 10 principais:

1. **Bonito é melhor que feio:** Enfatiza a importância de escrever um código que seja visualmente agradável e fácil de ler;

```python
# errado
a=1;b=2,4;print(b//a)

# recomendado
a = 1
b = 2,4

print(b // a)
```

2. **Explícito é melhor que implícito:** Deixar suas intenções claras ajuda a melhorar a legibilidade do código e reduz as chances de confusão quando outras pessoas forem ler.

```python
# errado
a = 1
b = 2,4

result = a + b

print(result)

# recomendado
a = 1
b = 2,4

result = float(a) + b

print(result)
```

3. **Simples é melhor que complexo:** Manter um código direto e fácil de entender é mais preferível a soluções complexas e complicadas.

```python
# errado
numeros = [1, 2, 3]
num_ao_cubo = []
for num in numeros:
   num_ao_cubo.append(num ** 3)

print(num_ao_cubo)

# recomendado
numeros = [1, 2, 3]
num_ao_cubo = [num ** 3 for num in numeros]

print(num_ao_cubo)
```

4. **Complexo é melhor que complicado:** Importante diferenciar entre a complexidade decorrente da natureza do problema e as complicações desnecessárias.

```python
# errado
if a > 0:
   if b > 0:
       faca_algo()
   else:
       faca_outra_coisa()
else:
   faca_outra_coisa_diferente()

# recomendado
if a > 0 and b > 0:
   faca_algo()
elif a > 0 and b <= 0:
   faca_outra_coisa()
else:
   faca_outra_coisa_diferente()
```

5. **Linear é melhor que aninhado:** Escrita de código com menos níveis de indentação e aninhamento.
   
```python
# errado
if condicao1:
   if condicao2:
       faca_algo()

# recomendado
if condicao1 and condicao2:
   faca_algo()
```

6. **Esparso é melhor do que denso:** Não tente “amontoar” tudo na mesma linha.
   
```python
# errado
result = a+b+c+d

# recomendado
result = a + b + c + d
```
7. **Legibilidade conta:** O código deve ser escrito de forma clara, compreensível e facilmente interpretado por humanos.
   
```python
# errado
x = x + 1

# recomendado
x += 1
```

8. **Casos especiais não são especiais o suficiente para quebrar as regras:** Mesmo em casos especiais ou cenários excepcionais, é importante aderir às regras e aos princípios gerais de codificação.

9. **Embora a praticidade supere a pureza:** Embora aderir às melhores práticas seja importante, a praticidade e as considerações do mundo real devem ter considerações maiores sobre seguir cegamente regras rígidas.

10. **Os erros nunca devem passar silenciosamente:** Quando ocorrem erros no código, eles devem ser tratados e relatados adequadamente. Ignorar ou esconder erros pode levar a um comportamento inesperado no seu código.

&nbsp;

<div align="center">

![python logo](<Images Sprint3/python logo.png>)

</div>

&nbsp;

# 2. Variáveis e Tipos de Dados

Há vários tipos de dados e cada um deles tem uma função e característica, podemos listar como:

+ **Booleanos (bool):** Indicam o que é verdadeiro ou falso;
+ **Inteiros (int):** Sem componentes fracionais, ex: 1, 20, 500, etc;
+ **Ponto Flutuante (float):** Números com ponto decimal, ex: 1.5, 7.34, 25.52, etc;
+ **Strings (str):** Sequência de caracteres, isto é, texto;
+ **Listas (list):** Sequência de dados, ex: [19, Julia, 21.12];
+ **Dicionário (dict):** Valores organizados em chave ({}), dois pontos (:) e em seguida o valor, ex: {"nome":"julia","idade":19};
+ **NoneType:** Usado para definir valores nulos ou nenhum valor, ex: var_value = none.

# 3. Operadores

Os operadores possuem a sua própria precedência, funcionando da mesma maneira que a lógica matemática, isto é, um operador vem antes do outro. Exemplo:

> 8 * 2 - 1 (sempre priorizamos a multiplicação/adição antes da subtração/adição, logo:) \
> (8 * 2) - 1 \
> 16 - 1 \
> Resposta: 15

Em python temos tal precedência:

<div align="center">

![tabela de precedência](<Images Sprint3/tabela de precedencia.png>)

</div>

&nbsp;

## **Operadores Aritméticos:** 

Usados para criar expressões matemáticas, havendo os seguintes operadores binários:

+ **Soma ( + ):**

```python
print (2 + 3) # output: 5
```
+ **Subtração ( - ):**

```python
print (4 - 7) # output: -3 
```
+ **Multiplicação ( * ):**

```python
print (2 * 5.3) # output: 10.6
```
+ **Divisão ( / ):**

```python
 print (8 / 4) # output: 2
```
+ **Divisão Inteira ( // ):**

```python
print (9.4 // 3) # output: 3.0
```
+ __Exponenciação ( ** ):__

```python
print (2 ** 8) # output: 256
```
+ **Módulo ( % ):**

```python
print (10 % 3) # output: 1
```

_**DESAFIO:** Defina seu percentual de despesas com base no seu salário e nas despesas._ 

```python
salario = float(input(Digite o valor do seu salário:))
despesas = float(input(Digite o valor de suas despesas:))

percentual_despesas = ( despesas / salario ) * 100

print ( percentual_despesas)
```

&nbsp;

+ **Operadores Relacionais:** Operador que obtém relação do membro da esquerda com o membro da direita, retornando com TRUE ou FALSE.

    + **Maior que ( > ):**
    ```python
    print (3 > 4) # output: False
    ```

    + **Maior ou Igual ( >= ):**
    ```python
    print (4 >= 3) # output: True
    ```

    + **Menor que ( < ):**
    ```python
    print (1 < 2) # output: True
    ```

    + **Menor ou Igual ( <= ):**
    ```python
    print (3 <= 1) # output: False
    ```

    + **Diferente ( != ):**
    ```python
    print (3! = 2) # output: False
    ```

    + **Igual ( == ):**
    ```python
    print (3 == 3) # output: True

    print (3 == '3') # output: False
    ```

&nbsp;

+ **Operadores de Atribuição:** Servem para atribuir valores à variáveis, utilizando com base os operadores aritméticos e/ou relacionais. Exemplo:

```python
a = 3
a = a + 7
print (a) # output: a = 10 // pode ser apresentado também como: a += 7
```

# 4. Conversão de Tipos e Coerções

Apesar de Python possuir o recurso de tipagem dinâmica, ela também é fortemente tipada, com isso, normalmente operações precisam lidar com objeto de mesma classe/tipo, para alguns casos existem conversões automáticas ou implícitas (coerção) e em outros é necessitando converter explicitamente estes objetos.

Exemplo disso seria a soma de um inteiro (int) ou ponto flutuante (float) com um texto/string (str), para realizarmos a conversão, aplicamos a tipagem desejada e entre parênteses o valor, como podemos observar abaixo:

```python
print (2 + float('3,4')) # output: 5.4 // observamos que transforma a string '3.4' em um ponto flutuante, sendo possível a soma
```
# 5 .Estruturas de Controle

Estruturas de controle são blocos de código em um programa de computador que permitem tomar decisões ou repetir a execução de determinadas instruções com base em certas condições.

+ **IF:** Estrutura condicional que permite executar um bloco de código se uma determinada condição for verdadeira;
+ **ELSE:** Cláusula opcional que pode ser usada para executar um bloco de código alternativo se a condição do if for falsa;
+ **WHILE:** Estrutura de loop que repete um bloco de código enquanto uma condição é verdadeira;
+ **FOR:** Estrutura de loop que permite iterar sobre uma sequência (como uma lista, tupla ou string) e executar um bloco de código para cada item da sequência;
+ **BREAK:** Usada para interromper imediatamente a execução de um loop (while ou for) e sair do loop, mesmo que a condição do loop ainda seja verdadeira;
+ **SET:**  Tipo de coleção em Python que armazena elementos únicos, ou seja, não permite duplicatas.

&nbsp;

# 6. Manipulação de Arquivos

A manipulação de arquivos em Python é uma habilidade essencial para lidar com a leitura e escrita de informações em arquivos do sistema. O Python fornece várias funções e métodos que permitem interagir com arquivos de diferentes maneiras. Encontramos:

+ **Abrindo um Arquivo:** Para trabalhar com um arquivo, você precisa abri-lo usando a função open(). A função aceita dois argumentos: o nome do arquivo e o modo de operação (leitura, escrita, etc.);

+ **Lendo de um Arquivo:** Você pode usar o método read() para ler o conteúdo de um arquivo e armazená-lo em uma variável.

+ **Escrevendo em um Arquivo:** Você pode usar o método write() para escrever conteúdo em um arquivo.

+ **Fechando um Arquivo:** Sempre feche um arquivo após usá-lo usando o método close().
  
+ **Usando 'with' para Gerenciamento de Contexto:** A declaração with é uma maneira mais segura de abrir e fechar arquivos automaticamente.

+ **Modos de Operação:** Os modos de operação mais comuns são:

   + **"r":** Leitura (padrão);
   + **"w":** Escrita, cria um novo arquivo ou substitui o conteúdo existente;
   + **"a":** Escrita, acrescenta ao final do arquivo ou cria um novo arquivo;
   + **"b":** Modo binário para arquivos;
   + **"x":** Criação exclusiva, falha se o arquivo já existir.


# 7. Exercícios e Desafio

Os exercícios foram realizados com o auxílio dos programas VSCode e Anaconda, e assim aplicados à plataforma. Estes foram divididos em diferentes formatos, pode se encontrar os exercícios resolvidos e suas devidas classificações nos links abaixo:

**Exercícios em Formato Markdown (.md):**

+ [**SEÇÃO 3**](EXERC%C3%8DCIOS/C%C3%B3digos.txt/EX_SECAO3.md);
+ [**SEÇÃO 4**](EXERC%C3%8DCIOS/C%C3%B3digos.txt/EX_SECAO4.md);
+ [**SEÇÃO 6**](EXERC%C3%8DCIOS/C%C3%B3digos.txt/EX_SECAO6.md);


**Exercícios em Formato Python (.py):**

+ [**Exercício 1**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX1.py);
+ [**Exercício 2**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX2.py);
+ [**Exercício 3**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX3.py);
+ [**Exercício 4**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX4.py);
+ [**Exercício 5**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX5.py);
+ [**Exercício 6**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX6.py);
+ [**Exercício 7**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX7.py);
+ [**Exercício 8**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX8.py);
+ [**Exercício 9**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX9.py);
+ [**Exercício 10**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX10.py);
+ [**Exercício 11**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX11.py);
+ [**Exercício 12**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX12.py);
+ [**Exercício 13**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX13.py);
+ [**Exercício 14**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX14.py);
+ [**Exercício 15**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX15.py); 
+ [**Exercício 16**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX16.py);
+ [**Exercício 17**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX17.py);
+ [**Exercício 18**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX18.py);
+ [**Exercício 19**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX19.py);
+ [**Exercício 20**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX20.py);
+ [**Exercício 21**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX21.py);
+ [**Exercício 22**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX22.py);
+ [**Exercício 23**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX23.py);
+ [**Exercício 24**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX24.py);
+ [**Exercício 25**](EXERC%C3%8DCIOS/C%C3%B3digos.py/EX25.py);

**Resposta dos Desafios em Texto (.txt):**

+ [**Exercício 1**](DESAFIO/etapa-1.txt);
+ [**Exercício 2**](DESAFIO/etapa-2.txt);
+ [**Exercício 3**](DESAFIO/etapa-3.txt);
+ [**Exercício 4**](DESAFIO/etapa-4.txt);
+ [**Exercício 5**](DESAFIO/etapa-5.txt).

**Exercícios em Formato Python (.py):**

+ [**Exercício 1**](DESAFIO/etapa-1.py);
+ [**Exercício 2**](DESAFIO/etapa-2.py);
+ [**Exercício 3**](DESAFIO/etapa-3.py);
+ [**Exercício 4**](DESAFIO/etapa-4.py);
+ [**Exercício 5**](DESAFIO/etapa-5.py).

&nbsp;

# 📝 Certificação

+ Certificação da conlusão do Curso Python 3: Do Básico ao Avançado de 16hrs.
  
![Print Conclusão Sprint3](<Images Sprint3/Certificado Sprint3.png>)

![Certificado Data Analytics 3](<Images Sprint3/Data Analytics_PB _AWS 3.jpg>)

---