# 🔖 **SUMÁRIO**

Nesta página encontra-se 6 Tópicos Principais, são estes:

+ **[Programação Funcional](#1-programação-funcional);**
+ **[Python 3 - Curso Completo do Básico ao Avançado](#1-python-3---curso-completo-do-básico-ao-avançado-22);**
+ **[Docker para Desenvolvedores](#docker-para-desenvolvedores);**
+ **[Estatística Descritiva com Python](#estatística-descritiva-com-python);**
+ **[Exercícios e Desafios](#5-exercícios-e-desafios);**
+ **[Certificação](#📝-certificação).**

---

&nbsp;

# 1. Programação Funcional

<div align="center">

![Programação Funcional](<Images Sprint4/Programação Funcional.webp>)

**Fonte: [Alura](https://www.alura.com.br/artigos/programacao-funcional-o-que-e)**

</div>

A programação funcional é um paradigma de programação que trata o cálculo como uma avaliação de funções matemáticas e evita a mudança de estado e a mutabilidade de dados. Em vez de se concentrar em "como" realizar tarefas específicas, a programação funcional se concentra em "o que" precisa ser feito.

A programação funcional é usada em linguagens como Haskell, Lisp, Clojure, Erlang e também pode ser aplicada em linguagens de programação imperativas, como Python e JavaScript, por meio de recursos como funções de ordem superior e expressões lambda.

1. **Composição de Funções:** A composição de funções é um conceito fundamental na programação funcional que envolve a criação de novas funções combinando duas ou mais funções existentes. A ideia é que você pode criar funções mais complexas ao aplicar uma função a outra função, criando uma "cadeia" de transformações de dados.

2. **Funções de Pureza:** Funções puras são funções que não têm efeitos colaterais e sempre produzem o mesmo resultado para os mesmos argumentos. Isso torna o código mais previsível e testável.

3. **Imutabilidade:** Os dados em programação funcional são imutáveis, o que significa que uma vez que um valor é atribuído a uma variável, ele não pode ser alterado. Em vez disso, novos valores são criados por meio de transformações e operações de dados.

4. **Efeito colateral:** Toda interação da nossa função com o mundo externo No nosso dia a dia fazemos coisas como:
   
    * Acessar banco de dados;
  
    * Realizar chamadas assíncronas;

    * Alterar propriedades de objetos entre outras tarefas.

5. **Imperativo x Declarativo:** "Imperativo" e "declarativo" são dois paradigmas de programação que representam diferentes abordagens para resolver problemas de programação.

    * No paradigma imperativo, você se concentra em instruções e controle de fluxo, enquanto no paradigma declarativo, você se concentra em expressar relações e restrições;

    * A programação imperativa tende a ser mais detalhada e explícita, enquanto a programação declarativa tende a ser mais abstrata e expressiva;

    * A programação declarativa geralmente é mais orientada a expressões e funções, enquanto a programação imperativa usa frequentemente estruturas de controle como loops e condicionais.

6. **Estado Compartilhado:** O termo "estado compartilhado" refere-se a uma situação em que várias partes de um programa ou sistema têm acesso ou dependem do mesmo conjunto de dados ou variáveis em algum estado de memória compartilhada. Isso pode ocorrer em diferentes contextos de programação e pode ter implicações importantes na previsibilidade, concorrência e manutenção do código.

&nbsp;

# 2. Python 3 - Curso Completo do Básico ao Avançado 2/2

## Funções de Primeira Classe

Capacidade de tratar funções como valores de primeira classe em uma linguagem de programação. Isso significa que você pode atribuir funções a variáveis, passá-las como argumentos para outras funções e retorná-las como resultados de outras funções. Temos:

1. **Atribuição a Variáveis:** Você pode atribuir uma função a uma variável, assim como faria com um valor, como um número ou uma string. Por exemplo:

```python
def saudacao(nome):
    return f"Olá, {nome}!"

cumprimentar = saudacao
print(cumprimentar("Alice"))  # output: Olá, Alice!
```

2. **Argumentos de Função:** Você pode passar uma função como argumento para outra função. Isso é útil para abstrair comportamentos e criar funções de ordem superior que aceitam outras funções como entrada. Por exemplo:

```python
def aplicar(funcao, valor):
    return funcao(valor)

resultado = aplicar(lambda x: x * 2, 5)
print(resultado)  # output: 10
```

3. **Retorno de Função:** Uma função pode retornar outra função como resultado. Isso é útil para criar funções de fábrica ou criar funções com comportamentos diferentes com base em algum critério. Por exemplo:

```python
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

ola = criar_saudacao("Olá")
print(ola("Maria"))  # output: Olá, Maria!
```

4. **Armazenamento em Estruturas de Dados:** Você pode armazenar funções em estruturas de dados, como listas ou dicionários, e acessá-las quando necessário. Isso é útil para criar estratégias dinâmicas ou criar pipelines de processamento. Por exemplo:

```python
operacoes = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
resultado = operacoes[1](3)
print(resultado)  # output: 6
```

## Funções de Alta Ordem

Funções que podem receber outras funções como argumentos e/ou retornar funções como resultados. Essas funções são uma parte essencial da programação funcional e permitem a criação de abstrações de alto nível, abrindo caminho para a composição de funções, encapsulamento de comportamento e expressividade do código. Temos:

1. **Funções como Argumentos:** Uma função de alta ordem pode receber outras funções como argumentos. Isso permite que você passe comportamentos específicos como argumentos para a função de alta ordem, tornando-a mais flexível. Exemplos disso incluem funções map, filter e reduce em muitas linguagens funcionais.

2. **Funções como Resultados:** Uma função de alta ordem também pode retornar funções como resultados. Isso é útil para criar abstrações que geram comportamentos personalizados com base em parâmetros de entrada.
   
3. **Funções Anônimas:** Funções de alta ordem frequentemente usam funções anônimas (também conhecidas como lambdas) para expressar comportamentos de maneira concisa e direta.

### Closure

Uma closure (ou fechamento) é uma função que "captura" variáveis do ambiente circundante (escopo) em que foi criada, permitindo que essas variáveis sejam acessadas mesmo após a saída desse ambiente circundante. Em outras palavras, uma closure é uma função que "lembrará" do escopo em que foi definida, mesmo que esse escopo não esteja mais ativo. Exemplo seria:

```python
def multiplicador(x):
    def interna(y):
        return x * y
    return interna

dobrar = multiplicador(2)  # dobrar agora é uma closure
triplicar = multiplicador(3)  # triplicar é outra closure

print(dobrar(5))  # output: 10
print(triplicar(5))  # output: 15
```
### LAMBDA

Uma lambda function (função lambda), também conhecida como função anônima, é uma função pequena e sem nome que pode ter zero ou mais argumentos, mas pode conter apenas uma expressão. 

As funções lambda são úteis quando você precisa de uma função simples para uma tarefa específica, como uma função de ordenação personalizada ou uma função de filtro. Temos como exemplo:

```python
# Função lambda que retorna o quadrado de um número
quadrado = lambda x: x ** 2

# Função lambda que verifica se um número é par
eh_par = lambda x: x % 2 == 0

# Função lambda que combina duas strings com uma vírgula no meio
concatenar = lambda a, b: f"{a}, {b}"

# Uso de funções lambda com a função sorted para ordenar uma lista de tuplas pelo segundo elemento
pontuacoes = [(nome, nota) for nome, nota in [("Alice", 95), ("Bob", 88), ("Carol", 92)]]
pontuacoes_ordenadas = sorted(pontuacoes, key=lambda x: x[1], reverse=True)
```

### MAP

A função map é uma função de ordem superior em muitas linguagens de programação, incluindo Python, que permite aplicar uma função a cada item de uma sequência (como uma lista) e retorna um objeto iterável (por exemplo, uma lista, um gerador ou um objeto map) que contém os resultados da aplicação da função a cada item da sequência. Exemplo:

```python
# Lista de strings
nomes = ["Alice", "Bob", "Carol", "David"]

# Usando map para aplicar a função len a cada nome
comprimentos = map(len, nomes)

# Convertendo o resultado em uma lista para visualização
comprimentos_lista = list(comprimentos)

print(comprimentos_lista)  # output: [5, 3, 5, 5]
```

### FILTER

função de ordem superior que é usada para filtrar elementos de uma sequência, como uma lista, com base em uma função de teste. Ela cria um novo iterável (geralmente uma lista) contendo apenas os elementos da sequência original para os quais a função de teste retorna True. Na prática temos como exemplo:

```python
def é_par(numero):
    return numero % 2 == 0

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = filter(é_par, lista_numeros)

# Converter o resultado em uma lista (opcional)
lista_pares = list(resultado)

print(lista_pares)  # output [2, 4, 6, 8, 10]
```

## Funções de Imutabilidade

se refere à característica dos objetos que não podem ser alterados após a sua criação. Isso significa que, uma vez que um objeto imutável é criado, seus valores não podem ser modificados. Isso é importante para garantir a integridade dos dados em muitas situações. Algumas estruturas encontradas são:

1. **Strings (str):** Quando você faz alguma operação que pareça modificar uma string, na verdade está criando uma nova string com as modificações. Exemplo:
   
```python
string_original = "Olá, mundo!"
string_modificada = string_original.replace("mundo", "Python")
print(string_original)  # output: "Olá, mundo!"
print(string_modificada)  # output: "Olá, Python!"
```

2. **Tuplas (tuple):** Você não pode adicionar, remover ou alterar elementos em uma tupla após a sua criação. Exemplo:

```python
tupla = (1, 2, 3)
# tente tupla[0] = 4 e você receberá um erro TypeError
```

3. **Números Imutáveis:** Números inteiros (int) e números de ponto flutuante (float) são imutáveis em Python. Quando você faz uma operação aritmética com eles, cria-se um novo valor em vez de modificar o valor original. Exemplo:

```pyhton
x = 5
y = x + 2  # O valor de x não é alterado
```

## Generators

É uma estrutura especial que permite que você itere sobre uma sequência potencialmente grande de itens sem armazená-los todos na memória de uma vez. Isso é útil quando você precisa trabalhar com dados que podem ser muito grandes para caber completamente na memória ou quando deseja gerar dados sob demanda, sem calcular todos de uma vez.

1. **Funções Geradoras:** Definida como uma função normal, mas usa a palavra-chave yield para produzir valores um de cada vez. Quando uma função contém uma ou mais instruções yield, ela se torna uma função geradora. Exemplo:

```python
def contar_ate(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Criando um objeto gerador
gen = contar_ate(5)

# Iterando sobre o gerador
for num in gen:
    print(num)
```

2. **Expressões Geradoras:** Expressões geradoras são semelhantes às compreensões de lista, mas usam parênteses em vez de colchetes. Elas criam objetos geradores sob demanda. Exemplo:

```python
numeros_pares = (x for x in range(1, 11) if x % 2 == 0)

for num in numeros_pares:
    print(num)
```

Além disso, também podemos utilizar a função **'next()'**, como mostra abaixo:

```python
gen = contar_ate(3)
print(next(gen))  # Mostra 1
print(next(gen))  # Mostra 2
print(next(gen))  # Mostra 3
# print(next(gen))  # Gera um erro StopIteration porque o gerador está esgotado
```

Geradores são particularmente úteis quando você precisa processar grandes conjuntos de dados ou realizar avaliação sob demanda, ou seja, calcular valores apenas quando necessário. Eles são comumente usados em situações onde a eficiência de memória é crucial, como na leitura de arquivos grandes ou no trabalho com sequências infinitas.

&nbsp;

# 3. Docker para Desenvolvedores

Docker é uma plataforma de código aberto que permite criar, implantar e executar aplicativos em contêineres. Os contêineres são ambientes leves e independentes que incluem todo o software necessário para executar um aplicativo, incluindo o código, as bibliotecas e as dependências. 

Empresas como Microsoft, Google, Red Hat (IBM) começaram a utilizá-lo em meados de 2014. Essa abordagem de empacotamento de aplicativos em contêineres facilita a implantação consistente e portátil em diferentes ambientes, como servidores de desenvolvimento, teste e produção.

+ **Contêineres:** Os contêineres são instâncias isoladas de aplicativos que são executadas em um sistema host compartilhando o núcleo do sistema operacional subjacente. Eles são leves, rápidos e independentes, o que significa que um aplicativo em contêiner pode ser executado de maneira consistente em qualquer máquina que tenha o Docker instalado.

+ **Docker Image:** Uma imagem Docker é um pacote de software que inclui o código do aplicativo, suas bibliotecas e dependências, bem como instruções sobre como o aplicativo deve ser executado. As imagens são usadas como modelos para criar contêineres em tempo de execução.

+ **Dockerfile:** Um Dockerfile é um arquivo de configuração que define como uma imagem Docker deve ser construída. Ele lista as instruções para instalar pacotes, copiar arquivos, configurar variáveis de ambiente e executar comandos dentro do contêiner.

+ **Docker Hub:** O Docker Hub é um repositório público onde você pode encontrar imagens Docker prontas para uso, criadas pela comunidade ou por organizações. Você também pode hospedar suas próprias imagens personalizadas no Docker Hub ou em outros registros de contêineres.

<div align="center">

![Docker e Kubernetes](<Images Sprint4/Docker e Kubernetes.png>)

</div>

## Comandos

+ **Verificar a versão do Docker:**

```python
docker --version
```

+ **Baixar uma imagem do Docker Hub:**

```python
docker pull nome_da_imagem
```

+ **Listar imagens locais:**

```python
docker images
```

+ **Executar um contêiner a partir de uma imagem:**

```python
docker run nome_da_imagem
```

+ **Executar um contêiner em segundo plano (modo detached):**

```python
docker run -d nome_da_imagem
```

+ **Listar contêineres em execução:**

```python
docker ps
```

+ **Listar todos os contêineres (incluindo os parados):**

```python
docker ps -a
```

+ **Parar um contêiner em execução:**

```python
docker stop ID_do_contêiner
```
+ **Iniciar um contêiner parado:**

```python
docker start ID_do_contêiner
```

+ **Remover um contêiner parado:**

```python
docker rm ID_do_contêiner
```

+ **Acessar uma shell dentro de um contêiner em execução:**

```python
docker exec -it ID_do_contêiner /bin/bash
```

+ **Construir uma imagem a partir de um Dockerfile:**

```python
docker build -t nome_da_imagem /caminho/do/Dockerfile
```

+ **Remover uma imagem local:**

```python
docker rmi nome_da_imagem
```

+ **Verificar logs de um contêiner:**

```python
docker logs ID_do_contêiner
```

+ **Copiar arquivos entre o sistema host e um contêiner:**

```python
docker cp arquivo.txt ID_do_contêiner:/caminho/no/contêiner
```

+ **Criar uma rede personalizada:**

```python
docker network create nome_da_rede
```

+ **Listar redes disponíveis:**

```python
docker network ls
```

+ **Remover uma rede:**

```python
docker network rm nome_da_rede
```

+ **Verificar estatísticas de uso de recursos de um contêiner:**

```python
docker stats ID_do_contêiner
```

## Docker Swarm

O Docker Swarm é uma ferramenta de orquestração de contêineres que faz parte do ecossistema Docker. Ele permite que você gerencie um cluster de máquinas Docker como um único recurso, tornando a implantação e o gerenciamento de aplicativos baseados em contêineres em ambientes distribuídos mais fácil e eficiente. O Docker Swarm oferece recursos para balanceamento de carga, alta disponibilidade e escalabilidade de aplicativos.

## Kubernetes

O Kubernetes (também conhecido como K8s) é uma plataforma de orquestração de contêineres de código aberto amplamente utilizada para automatizar a implantação, o dimensionamento e o gerenciamento de aplicativos em contêineres. Foi originalmente desenvolvido pelo Google e é mantido pela Cloud Native Computing Foundation (CNCF).

O Kubernetes oferece uma série de recursos e abstrações que tornam o gerenciamento de aplicativos baseados em contêineres mais eficiente e escalável em ambientes de produção. 

# 4. Estatística Descritiva com Python

A estatística é uma disciplina matemática que envolve a coleta, a análise, a interpretação e a apresentação de dados. Ela desempenha um papel fundamental em uma ampla variedade de campos, incluindo ciência, negócios, economia, medicina, engenharia, ciências sociais e muitos outros. A estatística ajuda a compreender e resumir informações a partir de conjuntos de dados, tornando possível tirar conclusões, tomar decisões informadas e fazer previsões.

+ **Aleatoriedade:** A aleatoriedade refere-se à característica de eventos, resultados ou fenômenos que ocorrem de forma imprevisível ou não determinística. Em outras palavras, eventos aleatórios não podem ser previstos com certeza, e sua ocorrência é influenciada por fatores desconhecidos ou não controláveis. A aleatoriedade desempenha um papel significativo em muitos campos, incluindo matemática, estatística, ciências naturais, ciências sociais e computação.

+ **População:** A população é o conjunto completo de todos os elementos ou observações que estão sendo estudados ou sobre os quais você deseja fazer afirmações. Em muitos casos, a população pode ser muito grande, difícil ou dispendiosa de estudar em sua totalidade. Por exemplo, a população de todos os seres humanos em um país é uma população enorme e praticamente impossível de examinar em sua totalidade.

+ **Amostra:** Uma amostra é um subconjunto representativo da população. É uma seleção de elementos ou observações retirados da população com o objetivo de estimar, inferir ou tirar conclusões sobre a população maior a partir desses dados. A amostra deve ser escolhida de forma aleatória ou de acordo com critérios específicos para que seja representativa da população maior.

+ **Variável:** Uma variável é uma característica, atributo ou propriedade que pode variar ou assumir diferentes valores em diferentes situações ou em diferentes unidades de observação. Existem dois tipos principais de variáveis:

    + **Variáveis Categóricas (Qualitativas):** Representam características que podem ser categorizadas em grupos ou categorias. Exemplos incluem gênero (masculino, feminino), tipo de sangue (A, B, AB, O) ou cor dos olhos (azul, verde, castanho).

    + **Variáveis Numéricas (Quantitativas):** Representam características que podem ser medidas numericamente. Elas podem ser contínuas (valores dentro de um intervalo) ou discretas (valores distintos). Exemplos incluem idade, altura, peso ou temperatura.
  
+ **Medida Observada:** Uma medida observada é o valor específico que uma variável assume em uma unidade de observação ou em um determinado contexto. As medidas observadas são os dados brutos coletados durante um estudo ou pesquisa. Por exemplo, se você estiver medindo a altura de cinco pessoas, as medidas observadas seriam as alturas específicas dessas cinco pessoas, como 165 cm, 172 cm, 178 cm, 160 cm e 175 cm.

## Gráficos

O profissional da estatística se utiliza de gráficos pois eles se propõem a diferentes usos: exploração, descoberta, interpretação, diagnóstico, comunicação, apresentação, destaque, clareza, contar uma história. Os gráficos são recursos visuais muito utilizados para facilitar a leitura e compreensão das informações e divulgação de pesquisas em jornais, revistas, panfletos, livros e televisão.

+ **Gráficos de Barra:** Um gráfico de barras é usado para representar dados categóricos, ele consiste em barras verticais ou horizontais, onde o comprimento ou altura da barra representa a quantidade ou frequência de uma categoria. Pode ser usado para comparar valores entre diferentes categorias.

```python
import matplotlib.pyplot as plt
import seaborn as sns

y = [2, 5, 2, 7, 5, 1]
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']
x2 = ['Variável Um', 'Variável Dois', 'Variável Três', 'Variável Quatro', 'Variável Cinco', 'Variável Seis']

plt.barh(x2, y, color='g')
plt.xlabel('Variável eixo X', size=24)
plt.ylabel('Categorias', size=20)
plt.title('Título do meu gráfico')

plt.show()
```

<div align="center">

![Gráfico de Barras](<Images Sprint4/Gráfico Barras.png>)

</div>

+ **Gráficos de Coluna:** Juntamente aos gráficos em barra, são os mais utilizados. Indicam, geralmente, um dado quantitativo sobre diferentes variáveis, lugares ou setores e não dependem de proporções. Os dados são indicados na posição vertical, enquanto as divisões qualitativas apresentam-se na posição horizontal.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Dados
y = [2, 5, 2, 7, 5, 1]
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']

# Criação do gráfico de barras horizontais
plt.bar(x, y, color='b')

# Rótulos e título
plt.xlabel('Variável eixo X', size=24)
plt.ylabel('Categorias', size=20)
plt.title('Título do meu gráfico')

# Exibir o gráfico
plt.show()
```

<div align="center">

![Gráfico de Colunas](<Images Sprint4/Gráfico de Colunas.png>)

</div>

+ **Gráficos de Setores:** Indicado para expressar uma relação de proporcionalidade, em que todos os dados somados compõem o todo de um dado aspecto da realidade.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot()

y = [2, 5, 2, 7, 5, 1]
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']
x2 = ['Variável Um', 'Variável Dois', 'Variável Três', 'Variável Quatro', 'Variável Cinco', 'Variável Seis']

plt.pie(y, labels=x, radius=2)
plt.show()
```

<div align="center">

![Gráfico de Setores](<Images Sprint4/Gráfico de Setores.png>)

</div>

+ **Gráficos de Linhas:** São especialmente úteis para mostrar como uma variável muda ao longo do tempo. O eixo X geralmente representa o tempo ou outra variável contínua, como a idade.

```python
import matplotlib.pyplot as plt

y = [6, 8, 3, 1, 9]
x1 = [1, 2, 3, 4, 5]
x = ['seg', 'ter', 'qua', 'qui', 'sex']

plt.plot(x1, y, '*-')
plt.xlabel('Eixo X', size=20)
plt.ylabel('Eixo Y', size=20)
plt.title('Título do Gráfico', size=15)
plt.show()
```

<div align="center">

![Gráfico de Linhas](<Images Sprint4/Gráfico de Linhas.png>)

</div>

+ **Histogramas:** Forma comum de representação gráfica de dados estatísticos que exibem a distribuição de frequência de um conjunto de dados. Eles são usados para mostrar como os valores de uma variável estão distribuídos e proporcionam uma visão visual da frequência com que diferentes valores ocorrem em um conjunto de dados. 


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)

plt.hist(x, bins = 50)
plt.xlabel('Eixo X')
plt.ylabel('Frequências')

Text(0, 0.5, 'Frequências')
```

<div align="center">

![Histograma](<Images Sprint4/Histograma.png>)

</div>

## MTC

Podemos afirmar que são medidas estatísticas comuns usadas na análise de dados. Cada uma delas tem seu próprio propósito e fornece informações diferentes sobre os dados. Dependendo da natureza dos dados e do que você deseja analisar, uma ou mais dessas medidas podem ser relevantes.

+ **Média (M):** A média é uma medida de tendência central que representa o valor médio de um conjunto de dados. Para calcular a média, você soma todos os valores e divide pelo número de observações.

```python
import numpy as np

dados = [10, 20, 30, 40, 50]
media = np.mean(dados)
print("Média:", media)
```

OBS: Este exemplo é baseado em uma tabela.

+ **Mediana (Me):** A mediana é outra medida de tendência central que representa o valor central em um conjunto de dados quando eles estão organizados em ordem crescente ou decrescente. Se houver um número ímpar de observações, a mediana é o valor do meio; se houver um número par de observações, a mediana é a média dos dois valores centrais.

```python
import numpy as np

dados = [10, 20, 30, 40, 50]
mediana = np.median(dados)
print("Mediana:", mediana)
```

+ **Moda (Mo):** A moda é o valor que aparece com maior frequência em um conjunto de dados. Pode haver uma moda (conjunto de dados unimodal), mais de uma moda (conjunto de dados bimodal, trimodal, etc.) ou nenhum valor que se repita (conjunto de dados amodal).

```python
import numpy as np
from scipy import stats

dados = [10, 20, 30, 30, 40, 50, 50, 50]
moda = stats.mode(dados)
print("Moda:", moda.mode[0])
```

# 5. Exercícios e Desafios

Os exercícios deste tópico foram realizados com o programa VSCode e assim aplicados à plataforma Udemy. Pode se encontrar os exercícios resolvidos nos links abaixo:

+ [**EXERCÍCIOS DA SEÇÃO 2 - PYTHON;**](EXERC%C3%8DCIOS/EX_SECAO2.md)
+ [**EXERCÍCIOS DA SEÇÃO 3 - DOCKER.**](EXERC%C3%8DCIOS/EX_SECAO3.md)

&nbsp;

# 📝 Certificação

+ Certificação da conlusão do Curso Python 3: Do Básico ao Avançado de 26hrs.
  
![Certificado Python](<Images Sprint4/Certificado Python3 2.jpg>)

+ Certificação da conlusão do Curso Docker Para Desenvolvedores (com Docker Swarm e Kubernetes) de 12hrs.

![Certificado Docker](<Images Sprint4/Certificado Docker.jpg>)

+ Certificação da conlusão do Curso Estatística Descritiva com Python de 5.5hrs.

![Certificado Estatísticas](<Images Sprint4/Certificado Estatistica com Python.jpg>)

---