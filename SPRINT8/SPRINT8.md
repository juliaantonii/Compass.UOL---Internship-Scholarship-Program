# 🔖 **SUMÁRIO**

Nesta página encontra-se 4 Tópicos Principais, são estes:

+ **[ATIVIDADE 1 - Exercícios TMDB](#1-atividade-1---exercício-tmdb)**
+ **[ATIVIDADE 2 - Desafio](#2-atividade-2---desafio-pt2)**
+ **[ATIVIDADE 3 - Exercícios Geração de Massa de Dados](#3-atividade-3---exercícios-geração-de-massa-de-dados)**
+ **[ATIVIDADE 4 - Exercícios Apache Spark](#4-atividade-4---exercícios-apache-spark)**
+ **[Certificação](#📝-certificação).**

---

&nbsp;

# 1. ATIVIDADE 1 - Exercício TMDB

Nesta atividades iremos criar um processo de extração de dados da API do TMDB utilizando serviços da AWS.

Uma API (Application Programming Interface) é um conjunto de regras, protocolos e ferramentas que permitem que diferentes sistemas de software se comuniquem e troquem informações de forma eficiente e padronizada.

Em outras palavras, uma API é uma interface que permite que desenvolvedores de software acessem dados ou funcionalidades de um sistema ou aplicativo sem precisar conhecer todos os detalhes internos do sistema. Deste modo, a API fornece uma maneira de acessar esses recursos de forma programática, geralmente usando requisições HTTP (Hypertext Transfer Protocol) para recuperar e/ou enviar dados.

A API TMDB é uma API RESTful, o que significa que os dados são acessados através de URLs que correspondem a recursos específicos. Os desenvolvedores podem acessar informações de busca, detalhes de filmes e programas de TV, imagens e informações relacionadas a gêneros e classificações.

+ Para saber mais sobre a API do The Movie Database, visite o site oficial (https://www.themoviedb.org/documentation/api)  e verifique os termos de uso (https://www.themoviedb.org/documentation/api/terms-of-use) .

+ Para a realização das atividades é de grande importância que você faça a leitura da documentação disponível em https://developers.themoviedb.org/3/movies/get-movie-details .

Esta atividade corresponde a um laboratório. Não esperamos que você registre resposta neste espaço. Contudo, deves adicionar o código-fonte produzido ao seu repositório no Github. Lembre-se de remover suas credenciais de acesso antes de efetuar commit.

Perguntas dessa tarefa:

+ **Etapa 1 -  Criando sua conta no TMDB**

Será preciso criar uma conta no porta do TMDB para, após, solicitar as chaves de acesso para uso da API.

Os passos são:

- Acessar o portal pelo link https://www.themoviedb.org/

- Clique no botão Junte-se ao TMDB na barra de navegação no topo da página

- Preencha o formulário de inscrição com as informações solicitadas e clique em Registrar. Utilize seu e-mail pessoal neste passo.

-  Você irá receber um e-mail de confirmação. Siga o processo solicitado

- Faça login em sua nova conta no TMDB e vá para o seu perfil, clicando no ícone de usuário no canto superior direito da página

- Clique na guia  Visão geral, opção Editar Perfil

- Clique no menu API, à esquerda. A seguir, na opção Criar, escolhendo o tipo Developer

- Aceite os termos e preencha o formulário com as informações solicitadas sobre a aplicação.

----- Em Tipo de Uso, informe Pessoal

----- Em URL, você pode informar um endereço fictício.

----- No Resumo, informe que o objetivo é para estudos

Etapa 2 - Testando rapidamente as credenciais e a biblioteca



Uma vez que você tenha sua chave de API, você pode fazer solicitações à API usando a seguinte estrutura de URL:

https://api.themoviedb.org/3/{endpoint}?api_key={sua_chave_de_api}&{parâmetros_opcionais}

Onde {endpoint} é o recurso que você deseja acessar (por exemplo, movie/{movie_id} para obter detalhes de um filme específico) e {parâmetros_opcionais} são quaisquer parâmetros adicionais que você deseje incluir na solicitação (por exemplo, language=pt-BR para obter informações em português).

Abaixo exemplo de código Python:

```python
import requests
import pandas as pd

from IPython.display import display

api_key = "SUA CHAVE"

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

filmes = []

for movie in data['results']:
df = {'Titulo': movie['title'],
'Data de lançamento': movie['release_date'],
'Visão geral': movie['overview'],
'Votos': movie['vote_count'],
'Média de votos:': movie['vote_average']}

filmes.append(df)

df = pd.DataFrame(filmes)
display(df)
```

**RESPOSTA:**

<div align="center">

![Tarefa 1](<Images Sprint8/Tarefa1.png>)

</div>

# 2. ATIVIDADE 2 - Desafio PT.2

Etapa 2 - Ingestão streaming/micro batch

Nesta etapa do desafio capturaremos dados do TMDB, utilizando AWS Lambda para realizar chamadas de API. Os dados coletados devem ser persistidos no Amazon S3, na camada RAW, mantendo o formato da origem (JSON) e, se possível, agrupando os registros em arquivos com, no máximo, 100 registros cada.

O objetivo desta etapa é complementar os dados dos Filmes e Series, carregados na Etapa 1, com dados oriundos do TMDB. Opcionalmente, você pode complementar com mais dados de outra API de sua escolha.

Importante:

+ Os arquivos CSVs carregados na Etapa 1 (Sprint 7) não devem ser modificados.

+ Os novos dados devem ser complementares aos dados do CSV. Ou seja, devem existir informações novas sobre os dados do CSV.

+ Não é necessário realizar tratamento dos dados externos, o máximo que pode ser feito é o agrupamento de dados.

+ Cuidado para os arquivos JSON gerados não serem maior do que 10 MB.

+ Não agrupe JSON com estruturas diferentes.

+ Os IDs do IMDB presentes nos arquivos CSV podem ser utilizados em pesquisas  no TMDB.

+ Se você escolher fazer sobre um filme ou uma trilogia específica, considere utilizar pelo menos 4 métodos de API diferentes para possibilitar uma análise de dados qualificada.

Considere desenvolver seu código localmente primeiro e com poucos dados para depois leva-lo para a AWS Lambda e aumentar a pesquisa de dados. APIs normalmente limitam requisições. Evite realizar muitas requisições em fase de desenvolvimento ou teste para evitarmos qualquer bloqueio na conta de vocês

Esta atividade corresponde a parte do desafio final. Não esperamos que você registre resposta neste espaço. Contudo, deves adicionar o código-fonte produzido ao seu repositório no Github. Lembre-se de remover suas credenciais de acesso antes de efetuar commit.

Perguntas dessa tarefa:

Em sua conta AWS, no serviço AWS Lambda, realize as seguintes atividades:

1.  Criar nova camada (layer) no AWS Lambda para as libs necessárias à ingestão de dados.

2. Implementar o código Python em AWS Lambda para consumo de dados do TMDB:

   - Buscar, pela API, os dados que complementem a análise

   - Utilizar a lib boto3 para gravar os dados no AWS S3, em arquivos JSON, com 100 registros em cada arquivo.

    -----| no momento da gravação dos dados deve-se considerar o padrão de path: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>

              São exemplos de caminhos de arquivos válidos:

               - S3:\\data-lake-do-fulano\raw\tmdb\json\2023\10\31\prt-uty-nfd.json

               - S3:\\data-lake-do-fulano\raw\tmdb\json\2023\10\31\idf-uet-wqt.json

Informação adicional:

Podemos utilizar os serviços  CloudWatch Event ou Amazon EventBridge para agendar extrações periódicas de dados no Twitter de forma automática.

**RESPOSTA:**

Inicialmente, foi feita uma conferência sobre a presença dos arquivos .CSV dentro do bucket S3, com os caminhos:

+ s3://compass.desafio/RAW/LOCAL/CSV/Movies/2023/10/23/movies.csv

+ s3://compass.desafio/RAW/LOCAL/CSV/Series/2023/10/23/series.csv

Após isso, é necessário criar uma Função Lambda e sua camada. Dessa forma, torna-se mais simples aplicar processamento aos dados quando eles são inseridos ou deslocados na nuvem. 

![Função Lambda](<Images Sprint8/Função Lambda.png>)

A função é criada diretamente na plataforma da AWS, entretando a camada é produzida localmente, utilizando do Docker para compactar os códigos e dados adicionais. Seguimos os seguintes passos:

+ Criar o Dockerfile

```python
FROM amazonlinux:2.0.20200602.0
RUN yum update -y
RUN yum install -y \
python3-pip \
zip \
RUN yum -y clean all
RUN python3.7 -m pip install --upgrade pip
```

+ Aplicamos comandos ao terminal para criar uma imagem e bibliotecas

```python
docker build -t amazonlinuxpython37 .

docker run -it amazonlinuxpython37 bash

bash-4.2# cd ~
bash-4.2# mkdir layer_dir
bash-4.2# cd layer_dir/
bash-4.2# mkdir python
bash-4.2# cd python/
bash-4.2# pwd

pip install requests pandas urllib3==1.26.6 -t .

bash-4.2# cd ..
bash-4.2# zip -r minha-camada.zip .

docker container ls

docker cp <id do container>:/root/layer_dir/minha-camada.zip ./
```

![Dockerfile](<Images Sprint8/Dockerfile.png>)

Com o arquivo ZIP já pronto, criamos um novo bucket (tmdb_zip) e fazemos o upload deste. Retornamos ao Lambda, adicionando a camada orientada pelo caminho do bucket S3 (s3://tmdb.zip/minha-camada-pandas.zip).

![tmdb zip](<Images Sprint8/tmdb_zip.png>)

![tmdb zip 2](<Images Sprint8/tmdb_zip 2.png>)

Agora será necessário criar a função lambda, onde nos permite a incorporação de lógica personalizada em recursos da AWS, como os armazenamentos do Amazon S3 e as tabelas.


Este código é uma função Lambda AWS que consome dados da API do The Movie Database (TMDB), armazena esses dados no Amazon S3 e realiza uma análise para encontrar o filme com a maior média por década, registrando também o número de votos desse filme.

+ Ele começa configurando o nome do bucket S3 onde os dados serão armazenados e as chaves de API do TMDB.

+ Em seguida, ele faz uma consulta à API do TMDB para obter dados de filmes do gênero "terror" (ou qualquer gênero especificado). Os parâmetros da consulta são definidos na variável params.

+ Os dados obtidos da API do TMDB são armazenados na variável tmdb_data.

+ A data e hora atual são usadas para criar um nome de arquivo no S3 para armazenar os dados do TMDB.

+ Os dados do TMDB são armazenados no Amazon S3 usando a biblioteca boto3.

+ Após armazenar os dados no S3, a função analyze_tmdb_data é chamada com os dados do TMDB para realizar a análise.

+ A função analyze_tmdb_data cria um dicionário que armazena informações sobre os filmes com a maior média por década.

+ Ele itera pelos resultados da API do TMDB, calcula a década de lançamento de cada filme e compara as médias de votos para encontrar o filme com a maior média por década.

+ Os resultados da análise são armazenados em um formato JSON e também são enviados para o Amazon S3.

+ A função retorna um objeto com um status de sucesso e uma mensagem informando que os dados do TMDB foram consumidos e a análise foi armazenada no S3 com sucesso.

```python
import json
import requests
import boto3
from datetime import datetime

def get_movie_details(movie_id, api_key):
    movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US&append_to_response=revenue,budget'

    response = requests.get(movie_url)
    response.raise_for_status()  # Verifica se houve erro na requisição HTTP

    return response.json()

def get_movie_keywords(movie_id, api_key):
    keywords_url = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords'
    params = {'api_key': api_key}

    response = requests.get(keywords_url, params=params)
    response.raise_for_status()  # Verifica se houve erro na requisição HTTP

    data = response.json()
    if 'keywords' in data:
        return [keyword['name'] for keyword in data['keywords']]
    else:
        return []

def lambda_handler(event, context):
    api_key = 'MINHA CHAVE'
    base_url = 'https://api.themoviedb.org/3/discover/movie'
    s3_bucket_name = 'compass.desafio'
    
    params_tmdb = {
        'api_key': api_key,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'include_adult': 'false',
        'include_video': 'false',
        'page': 1
    }
    
    s3_client = boto3.client('s3')
    current_date = datetime.utcnow().strftime('%Y/%m/%d')
    s3_prefix = f'RAW/tmdb/json/{current_date}'
    
    current_page = 1
    while True:
        params_tmdb['page'] = current_page
        
        response = requests.get(base_url, params=params_tmdb)
        data = response.json()
        
        if 'results' not in data or not data['results']:
            break
        
        chunks = [data['results'][i:i + 100] for i in range(0, len(data['results']), 100)]
        
        for i, chunk in enumerate(chunks):
            for movie in chunk:
                movie_id = movie.get('id')
                if movie_id:
                    movie_details = get_movie_details(movie_id, api_key)
                    movie_keywords = get_movie_keywords(movie_id, api_key)

                    if movie_details is not None and movie_keywords is not None:
                        movie.update({
                            'revenue': movie_details.get('revenue'),
                            'budget': movie_details.get('budget'),
                            'keywords': movie_keywords
                        })

            s3_object_key = f'{s3_prefix}/prt-uty-nfd_{current_page}_{i + 1}.json'
            s3_object_url = f's3://{s3_bucket_name}/{s3_object_key}'
            
            s3_client.put_object(
                Bucket=s3_bucket_name,
                Key=s3_object_key,
                Body=json.dumps(chunk),
                ContentType='application/json'
            )
        
        current_page += 1
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data successfully saved to S3!')
    }
```

# 3. ATIVIDADE 3 - Exercícios Geração de Massa de Dados

**1. [Warm up]  Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória. Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.**

**RESPOSTA:**

<div align="center">

![Tarefa 3 1.2](<Images Sprint8/Tarefa 3 - 1.2.png>)

![Tarefa 3](<Images Sprint8/Tarefa 3 - 1.png>)

</div>

&nbsp;

**2. [Warm up] Em Python, declare e inicialize uma lista contendo o nome de 20 animais. Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um (você pode utilizar list comprehension aqui).  Na sequência, armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV.**

```
animais = ['cachorro', 'gato', 'coelho', 'porco', 'galinha',

           'vaca', 'ovelha', 'elefante', 'girafa', 'tigre',

           'zebra', 'rinoceronte', 'macaco', 'canguru', 'urso',

           'lobo', 'raposa', 'panda', 'pinguim', 'crocodilo']

animais.sort()

[print(animal) for animal in animais]

with open("animais.csv", "w") as arquivo:

    for animal in animais:

        arquivo.write(animal + "\n")
```

**RESPOSTA:**

<div align="center">

![Tarefa 3 - 2](<Images Sprint8/Tarefa 3 - 2.1.png>)

![Tarefa 3 - 3](<Images Sprint8/Tarefa 3 - 2.2.png>)

![Animais](<Images Sprint8/animais.png>)

![Animais Open](<Images Sprint8/animais open.png>)

</div>

&nbsp;

**3. [Laboratório] Elaborar um código Python para gerar um dataset de nomes de pessoas. Siga os passos a seguir para realizar a atividade:**

+ Passo 1:  Instalar biblioteca names para geração de nomes aleatórios. O comando de instalação é pip install names

+ Passo 2 Importar as bibliotecas random, time, os e names em seu código

+ Passo 3: Definir os parâmetros para geração do dataset, ou seja, a quantidades de nomes aleatórios e a quantidade de nomes que devem ser únicos.

Define a semente de aleatoriedade

```python
random.seed(40)

qtd_nomes_unicos = 3000

qtd_nomes_aleatorios = 10000000
```

Nota: Quando trabalhamos com números randômicos em computação, na realidade, estamos falando de valores pseudoaleatórios, uma vez que o computador não consegue gerar números verdadeiramente aleatórios. No caso do Python, a função random.seed inicializa o algoritmo responsável pela geração de valores randômicos. É um processo determinístico,  pois os valores gerados serão sempre os mesmos se utilizado a mesma configuração de inicialização. A este número inicial chamamos de semente de aleatoriedade.

+ Passo 4: Gerar os nomes aleatórios.

```python
aux=[]

for i in range(0, qtd_nomes_unicos):

    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados=[]

for i in range(0,qtd_nomes_aleatorios):

    dados.append(random.choice(aux))
```

+ Passo 5: Gerar um arquivo de texto contendo todos os nomes, um a cada linha. O nome do arquivo deve ser nomes_aleatorios.txt

+ Passo 6: Abrir o arquivo e verificar seu conteúdo (editor de texto)

**RESPOSTA:**

<div align="center">

![Tarefa 3 - 3.1](<Images Sprint8/Tarefa 3 - 3.1.png>)

![Tarefa 3 - 3.2](<Images Sprint8/Tarefa 3 - 3.2.png>)

![nomes](<Images Sprint8/nomes.png>)

![nomes open](<Images Sprint8/nomes open.png>)

</div>

&nbsp;

# 4. ATIVIDADE 4 - Exercícios Apache Spark

Neste laboratório você irá aplicar os recursos básicos de manipulação de dataframes através do framework Apache Spark.

1. Inicialmente iremos preparar o ambiente, definindo o diretório onde nosso código será desenvolvido. Para este diretório iremos copiar o arquivo nomes_aleatorios.txt.

Após, em nosso script Python, devemos importar as bibliotecas necessárias:

from pyspark.sql import SparkSession

from pyspark import SparkContext, SQLContext

Aplicando as bibliotecas do Spark, podemos definir a Spark Session e sobre ela definir o Context para habilitar o módulo SQL

spark = SparkSession \

                .builder \

                .master("local[*]")\

                .appName("Exercicio Intro") \

                .getOrCreate()

Nesta etapa, adicione código para ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv. Carregue-o para dentro de um dataframe chamado df_nomes e, por fim, liste algumas linhas através do método show. Exemplo: df_nomes.show(5)

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, when, expr
 
# part 1
# Crie uma sessão Spark
spark = SparkSession.builder \
    .master("local[*]")\
    .appName("Exercicio Intro") \
    .getOrCreate()
 
# Leia o arquivo CSV
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
 
df_nomes.show(5)
```

<div align="center">

![Etapa 1 Output](<Images Sprint8/Atv4 Etp1.png>)

</div>

2. No Python, é possível acessar uma coluna de um objeto dataframe pelo atributo (por exemplo df_nomes.nome) ou por índice (df_nomes['nome']). Enquanto a primeira forma é conveniente para a exploração de dados interativos, você deve usar o formato de índice, pois caso algum nome de coluna não esteja de acordo seu código irá falhar.

Como não informamos no momento da leitura do arquivo, o Spark não identificou o Schema por padrão e definiu todas as colunas como string. Para ver o Schema, use o método df_nomes.printSchema().

Nesta etapa, será necessário adicionar código para renomear a coluna para Nomes, imprimir o esquema e mostrar 10 linhas do dataframe.

```python
# part 2
# Mostre o esquema do DataFrame
df_nomes.printSchema()

# Mostre as 10 primeiras linhas do DataFrame
df_nomes.show(10)
```

<div align="center">

![Etapa 2](<Images Sprint8/Atv4 Etp2.png>)

</div>

3. Ao dataframe (df_nomes), adicione nova coluna chamada Escolaridade e atribua para cada linha um dos três valores de forma aleatória: Fundamental, Medio ou Superior.

Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos para próprio Spark.

```python
# part 3
# Adicione a coluna "Escolaridade" de forma aleatória
df_nomes = df_nomes.withColumn("Escolaridade", when(rand() <= 0.33, "Fundamental")
                                   .when((rand() > 0.33) & (rand() <= 0.67), "Médio")
                                   .otherwise("Superior"))
df_nomes.show()
```

4. Ao dataframe (df_nomes), adicione nova coluna chamada Pais e atribua para cada linha o nome de um dos 13 países da América do Sul, de forma aleatória.

Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos para próprio Spark.

```python
# part 4
# Adicione a coluna "Pais" de forma aleatória
paises_sul_america = ["Argentina", "Brasil", "Chile", "Colômbia", "Equador", "Paraguai", "Peru", "Uruguai", "Venezuela", "Bolívia", "Guiana", "Suriname", "Guiana Francesa"]
df_nomes = df_nomes.withColumn("Pais", when(rand() <= 0.1, "Argentina")
                                   .when(rand() <= 0.2, "Brasil")
                                   .when(rand() <= 0.3, "Chile")
                                   .when(rand() <= 0.4, "Colômbia")
                                   .when(rand() <= 0.5, "Equador")
                                   .when(rand() <= 0.6, "Paraguai")
                                   .when(rand() <= 0.7, "Peru")
                                   .when(rand() <= 0.8, "Uruguai")
                                   .when(rand() <= 0.9, "Venezuela")
                                   .otherwise("Bolívia"))
```

5. Ao dataframe (df_nomes), adicione nova coluna chamada AnoNascimento e atribua para cada linha um valor de ano entre 1945 e 2010, de forma aleatória. 

Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos para próprio Spark.

```python
# part 5
# Adicione a coluna "AnoNascimento" de forma aleatória
df_nomes = df_nomes.withColumn("AnoNascimento", expr("int(1945 + rand() * 66)"))
```

6. Usando o método select do dataframe (df_nomes), selecione as pessoas que nasceram neste século. Armazene o resultado em outro dataframe chamado df_select e mostre 10 nomes deste.

```python
# Selecione pessoas que nasceram neste século (a partir de 2000)
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000)
df_select.show(10)
```

7. Usando Spark SQL repita o processo da Pergunta 6. Lembre-se que, para trabalharmos com SparkSQL, precisamos registrar uma tabela temporária e depois executar o comando SQL. Abaixo um exemplo de como executar comandos SQL com SparkSQL:

df_nomes.createOrReplaceTempView ("pessoas")

spark.sql("select * from pessoas").show()

```python
# part 6
# Registre o DataFrame como uma tabela temporária
df_nomes.createOrReplaceTempView("pessoas")
 
# Execute a consulta SQL para selecionar pessoas que nasceram neste século
query_sql = """
SELECT *
FROM pessoas
WHERE AnoNascimento >= 2000
"""
df_select_sql = spark.sql(query_sql)
df_select_sql.show(10)
```

8. Usando o método select do Dataframe df_nomes, Conte o número de pessoas que são da geração Millennials (nascidos entre 1980 e 1994) no Dataset

```python
# part 8
# Contar o número de Millennials (nascidos entre 1980 e 1994)
df_millennials = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994))
count_millennials = df_millennials.count()
print(f"Número de Millennials: {count_millennials}")

9. Repita o processo da Pergunta 8 utilizando Spark SQL

```python
# part 9
# Execute a consulta SQL para contar o número de Millennials
query_millennials = """
SELECT COUNT(*) AS CountMillennials
FROM pessoas
WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994
"""
 
millennials_count = spark.sql(query_millennials).first()[0]
print(f"Número de Millennials: {millennials_count}")
 
df_nomes.createOrReplaceTempView("pessoas")
```

10. Usando Spark SQL, obtenha a quantidade de pessoas de cada país para uma das gerações abaixo. Armazene o resultado em um novo dataframe e depois mostre todas as linhas em ordem crescente de Pais, Geração e Quantidade

- Baby Boomers – nascidos entre 1944 e 1964;

- Geração X – nascidos entre 1965 e 1979;4

- Millennials (Geração Y) – nascidos entre 1980 e 1994;

- Geração Z – nascidos entre 1995 e 2015.

```python
# part 10
# Defina as consultas SQL
queryBoomers = """
SELECT Pais, 'Baby Boomers' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1944 AND AnoNascimento <= 1964
GROUP BY Pais
"""
 
queryGenX = """
SELECT Pais, 'Geracao X' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1965 AND AnoNascimento <= 1979
GROUP BY Pais
"""
 
queryMillennials2 = """
SELECT Pais, 'Millennials' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994
GROUP BY Pais
"""
 
queryGenZ = """
SELECT Pais, 'Geracao Z' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1995 AND AnoNascimento <= 2015
GROUP BY Pais
"""
 
# Execute as consultas SQL
dfResultado = spark.sql(queryBoomers).union(spark.sql(queryGenX)).union(spark.sql(queryMillennials2)).union(spark.sql(queryGenZ))
dfResultado = dfResultado.orderBy("Pais", "Geracao", "Quantidade")
dfResultado.show()
```

# 📝 Certificação

![Certificado Data Analytics 8/10](<Images Sprint8/Certificado Data Analytics 8-10.jpg>)
---
