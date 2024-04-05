# 🔖 **SUMÁRIO**

Nesta página encontra-se 4 Tópicos Principais, são estes:

+ **[TAREFA 1: Modelagem Relacional - Normalização](#1-tarefa-1-modelagem-relacional---normalização)**
+ **[TAREFA 2: Modelagem Dimensional - Criação de Modelo](#2-tarefa-2-modelagem-dimensional---criação-de-modelo)**
+ **[TAREFA 3: Desafio Parte 3 - Processamento da Trusted](#3-tarefa-3-desafio-parte-3---processamento-da-trusted)**
+ **[TAREFA 4: Desafio Parte 4 - Modelagem de Dados da Refined](#4-tarefa-4-desafio-parte-3---modelagem-de-dados-da-refined)**
+ **[TAREFA 5: Defasio Parte 5 - Processamento de Refined](#5-tarefa-5-desafio-parte-3---processamento-da-refined)**
+ **[Certificação](#📝-certificação).**

---

&nbsp;

# 1. TAREFA 1: Modelagem Relacional - Normalização

Um desafio prático relacionado a modelagem relacional, receberão um modelo desnormalizado para aplicarem as formas normais.

Aqui você irá praticar conceitos de Modelagem relacional que estudou anteriormente. Estaremos considerando a base de dados Concessionaria, cujo modelo é apresentado na Modelagem Lógica abaixo.


O desafio é normalizar esta base de dados, ou seja, aplicar as formas normais.

Observações: Para auxiliar na resolução, você poderá baixar o arquivo contendo o banco de dados (concessionaria.zip) para seu computador, e, com auxílio de algum cliente SQL, executar as queries localmente. Lembre-se de descompactar o arquivo antes.

São exemplos de clientes SQL o DBeaver, SQLiteStudio e DataGrip. O primeiro costuma ser utilizado com maior frequência.

<div align="center">

![Tb Locação](<Images Sprint9/tb_locacao.png>)

</div>

**Perguntas dessa tarefa:** Adicione sua resposta (formato .SQL) ao seu repositório Git na respectiva Sprint e coloque abaixo o link do GitHub onde o(s) arquivos SQL estão salvos.

Não é obrigatório, mas seria interessante:

- uma explicação breve dos passos seguidos para a normalização (aqui na janela abaixo)

- o desenho da Modelagem Lógica após a normalização. (anexado aqui abaixo)


**RESPOSTA:**

O exercício envolveu a normalização de uma base de dados para uma concessionária, originalmente apresentada em uma única tabela com diversos atributos. A normalização é um processo que visa organizar os dados de uma maneira eficiente, reduzindo a redundância e melhorando a integridade referencial.

Etapas de Normalização:

Identificação de Entidades:

A primeira etapa foi identificar as diferentes entidades envolvidas nos dados fornecidos. No seu caso, identificamos as entidades Combustiveis, Carros, Vendedores, e Locacoes.
Criação de Tabelas Separadas:

Cada entidade foi representada por uma tabela separada. Isso ajuda a evitar a repetição de dados e a manter a consistência.
Atribuição de Chaves Primárias e Estrangeiras:

Em cada tabela, uma coluna foi designada como chave primária (PK), que é uma maneira única de identificar cada registro. Além disso, foram definidas chaves estrangeiras (FK) para estabelecer relações entre as tabelas.
Refatoração de Relacionamentos:

Os relacionamentos entre as entidades foram reformulados usando chaves estrangeiras. Por exemplo, na tabela Locacoes, foram adicionadas referências para as chaves primárias de Clientes, Carros, e Vendedores.
Eliminação de Redundâncias:

O processo de normalização reduz a redundância de dados, garantindo que cada informação seja armazenada em apenas um local. Isso ajuda a evitar inconsistências e economiza espaço.
Melhoria na Manutenção e Consistência:

Com as tabelas normalizadas, a manutenção do banco de dados e a consistência dos dados se tornam mais fáceis de gerenciar. Alterações em uma entidade não afetam desnecessariamente outras partes do sistema.

Foi usada a seguinte lógica em SQL:

```SQL
-- Tabela Clientes
CREATE TABLE Clientes (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

-- Tabela Combustiveis
CREATE TABLE Combustiveis (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

-- Tabela Carros
CREATE TABLE Carros (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    chassisCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idCombustivel INT REFERENCES Combustiveis(idCombustivel)
);

-- Tabela Vendedores
CREATE TABLE Vendedores (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

-- Tabela Locacoes
CREATE TABLE Locacoes (
    idLocacao INT PRIMARY KEY,
    idCliente INT REFERENCES Clientes(idCliente),
    idCarro INT REFERENCES Carros(idCarro),
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    valorDiaria DECIMAL(18, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INT REFERENCES Vendedores(idVendedor)
);
```


<div align="center">

![Atv1 Part1](<Images Sprint9/Atv1_p1.png>)

![Atv1 Part2](<Images Sprint9/Atv1_p2.png>)

![Atv1 Part3](<Images Sprint9/Atv1_p3.png>)

</div>

# 2. TAREFA 2: Modelagem Dimensional - Criação de Modelo

A tarefa prática aqui é utilizar o Modelo Relacional criado por você na tarefa anterior e com base nela, criar uma Modelagem Dimensional.

Aqui você irá praticar conceitos de Modelagem Dimensional que estudou anteriormente. Estaremos considerando a base de dados Concessionaria, cujo modelo será o criado por vocês na seção anterior (Modelagem Relacional).

O desafio é montar o Modelo Dimensional com base no Modelo Relacional (normalizado - feito por vocês) na seção anterior.

Observações:

Dica: Criar views para fatos e dimensões

**Perguntas dessa tarefa:** Adicione sua resposta (formato .SQL) ao seu repositório Git na respectiva Sprint e coloque abaixo o link do GitHub onde o(s) arquivos SQL estão salvos.

Não é obrigatório, mas seria interessante:

- o desenho da Modelagem Dimensional (anexado aqui abaixo)

**RESPOSTA:**

A modelagem dimensional é uma técnica usada no projeto de data warehouses para fornecer uma visão mais intuitiva e eficiente dos dados. Nessa abordagem, você cria modelos que consistem em fatos e dimensões. Os fatos representam os números que você deseja analisar, enquanto as dimensões são as categorias pelas quais você deseja analisar esses fatos. 

Para a criação de tabelas, seguimos a seguinte lógica:

```sql
-- Tabela de Fatos (FatoLocacao)
CREATE TABLE FatoLocacao (
    idFatoLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    idDataTempo INT,
    qtdDiaria INT,
    valorDiaria DECIMAL(18, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES DimCliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES DimCarro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES DimVendedor(idVendedor),
    FOREIGN KEY (idDataTempo) REFERENCES DimDataTempo(idDataTempo)
);

-- Tabelas de Dimensões
CREATE TABLE DimCliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

CREATE TABLE DimCarro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    chassiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES DimCombustivel(idCombustivel)
);

CREATE TABLE DimVendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

CREATE TABLE DimDataTempo (
    idDataTempo INT PRIMARY KEY,
    dataLocacao DATETIME,
    horaLocacao TIME
);

-- Tabela de Dimensão Adicional (DimCombustivel
CREATE TABLE DimCombustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);
```

<div align="center">

![Atv2 Part1](<Images Sprint9/Atv2_p1.png>)

![diagrama tarefa 2](<Images Sprint9/diagrama tarefa 2.png>)
</div>



# 3. TAREFA 3: Desafio Parte 3 - Processamento da Trusted

A camada Trusted de um data lake corresponde àquela em que os dados encontram-se limpos e são confiáveis. É resultado da integração das diversas fontes de origem, que encontram-se na camada anterior, que chamamos de Raw.

Aqui faremos uso do Apache Spark no processo, integrando dados existentes na camada Raw Zone. O objetivo é gerar uma visão padronizada dos dados, persistida no S3,  compreendendo a Trusted Zone do data lake.  Nossos jobs Spark serão criados por meio do AWS Glue.

Todos os dados serão persistidos na Trusted no formato PARQUET, particionados por data de coleta do TMDB (dt=<ano-mês-dia> exemplo: dt=2023-11-31). A exceção fica para os dados oriundos do processamento batch (CSV), que não precisam ser particionados.

Iremos separar o processamento em dois jobs: o primeiro, para carga histórica, será responsável pelo processamento dos arquivos CSV  e o segundo, para carga de dados do TMDB (e outra API, se utilizada). Lembre-se que suas origens serão os dados existentes na RAW Zone.

Importante: Desenvolva os jobs no Glue utilizando a opção Spark script editor.  Após, na aba Job details, atente para as seguintes opções:

Worker type: Informe G 1x (opção de menor configuração).

Requested  number of workers: Informe 2, que é a quantidade mínima.

Job timeout (minutes): Mantenha em 60 ou menos, se possível.

Após realizar a atividade, lembre-se de finalizar qualquer execução ativa de job para não incorrer em custos desnecessários.

**Perguntas dessa tarefa:** Realize as atividades conforme as instruções. Neste espaço, você pode adicionar prints dos jobs criados. Contudo, lembre-se de adicionar todo código elaborado no seu repositório do Github.

**RESPOSTA:**

JOB 1

```python
# Job1 Script (CSV to Parquet)

import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_path_csv = args['S3_INPUT_PATH']
target_path_csv = args['S3_TARGET_PATH']

df_csv = spark.read.csv(source_path_csv, sep="|", header=True)

df_csv.write.format("parquet").mode("append").save(target_path_csv)

job.commit()
```

<div align="center">

![Atv3 Part1](<Images Sprint9/Atv3_p1.png>)

![Atv3 Bucket 1](<Images Sprint9/Atv3 Bucket 1.png>)
</div>

JOB 2

```SQL
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

# Obter argumentos
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Configurar o contexto do Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos
source_path_tmdb = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

movies_df = spark.read.json(source_path_tmdb)

# Escrever DataFrame Spark no caminho de destino
movies_df.write.parquet(target_path, mode='overwrite')

# Finalizar o job
job.commit()
```

<div align="center">

![Atv3 Part2](<Images Sprint9/Atv3_p2.png>)

![Atv3 Bucket 2](<Images Sprint9/Atv3 Bucket 2.png>)

</div>

# 4. TAREFA 4: Desafio Parte 3 - Modelagem de dados da Refined

A camada Refined corresponde à camada de um data lake em que os dados estão prontos para análise e extração de insights. Sua origem corresponde aos dados da camada anterior, a Trusted.

Devemos pensar em estruturar os dados seguindo os princípios de modelagem multidimensional, a fim de permitir consultas sobre diferentes perspectivas.

Nesta etapa do desafio, você deve fazer a modelagem de dados da camada refined, definindo as tabelas e, se necessário, views, a fim de disponibilizar os dados para a ferramenta de visualização (QuickSight, a partir da próxima Sprint). Lembre-se que a origem será os dados oriundos da Trusted Zone.

**Perguntas dessa tarefa:** Apresentar a modelagem de dados da camada Refined. Você pode exportar seu modelo de dados na forma de imagem e registrar aqui. Lembre-se de deixá-lo disponível também no seu repositório do Github.

**RESPOSTA:**

```SQL
-- Tabela Normalizada
CREATE TABLE tab_normalizada (
    id_filme INT PRIMARY KEY AUTO_INCREMENT,
    tituloprincipal VARCHAR(255) NOT NULL,
    anolancamento VARCHAR(4),
    tempominutos VARCHAR(5),
    genero VARCHAR(50),
    notamedia VARCHAR(5),
    quantidadevotos INT,
    mediavotos DOUBLE,
    popularidadefilme DOUBLE,
    orcamentofilme INT,
    receitafilme INT,
    palavrachave VARCHAR(255)
);

-- Tabela de Artistas
CREATE TABLE artista (
    id_artista INT PRIMARY KEY AUTO_INCREMENT,
    id_filme INT,
    generoartista VARCHAR(50),
    personagem VARCHAR(255),
    nomeartista VARCHAR(255),
    anonascimento VARCHAR(4),
    anofalecimento VARCHAR(4),
    profissao VARCHAR(50),
    FOREIGN KEY (id_filme) REFERENCES tab_normalizada(id_filme)
);

-- Tabela de Avaliação
CREATE TABLE avaliacao (
    id_filme INT PRIMARY KEY AUTO_INCREMENT,
    notamedia VARCHAR(5),
    quantidadevotos INT,
    mediavotos DOUBLE,
    popularidadefilme DOUBLE,
    FOREIGN KEY (id_filme) REFERENCES tab_normalizada(id_filme)
);

-- Tabela de Fatos do Filme
CREATE TABLE fatos_filme (
    id_filme INT PRIMARY KEY AUTO_INCREMENT,
    tituloprincipal VARCHAR(255) NOT NULL,
    anolancamento VARCHAR(4),
    tempominutos VARCHAR(5),
    genero VARCHAR(50),
    palavrachave VARCHAR(255),
    FOREIGN KEY (id_filme) REFERENCES tab_normalizada(id_filme)
);

-- Tabela Financeira
CREATE TABLE financeiro (
    id_filme INT PRIMARY KEY AUTO_INCREMENT,
    orcamentofilme INT,
    receitafilme INT,
    FOREIGN KEY (id_filme) REFERENCES tab_normalizada(id_filme)
);
```

<div align="center">

![Diagrama tarefa 4](<Images Sprint9/diagrama tarefa 4.png>)

</div>

**Tabela de Fatos (tab_normalizada):**

id_filme: Identificador único para cada filme (chave primária).
tituloprincipal: Título principal do filme.
anolancamento: Ano de lançamento do filme.
tempominutos: Duração do filme em minutos.
genero: Gênero do filme.
notamedia: Nota média atribuída ao filme.
quantidadevotos: Quantidade de votos recebidos pelo filme.
mediavotos: Média dos votos do filme.
popularidadefilme: Valor de popularidade associado ao filme.
orcamentofilme: Orçamento do filme.
receitafilme: Receita gerada pelo filme.
palavrachave: Palavras-chave associadas ao filme.
Tabelas de Dimensão:

**artista:**

id_artista: Identificador único para cada artista (chave primária).
id_filme: Chave estrangeira referenciando a tabela de fatos (tab_normalizada).
generoartista: Gênero do artista.
personagem: Personagem interpretado pelo artista.
nomeartista: Nome do artista.
anonascimento: Ano de nascimento do artista.
anofalecimento: Ano de falecimento do artista.
profissao: Profissão do artista.

**avaliacao:**

id_filme: Chave estrangeira referenciando a tabela de fatos (tab_normalizada).
notamedia: Nota média associada à avaliação do filme.
quantidadevotos: Quantidade de votos recebidos na avaliação.
mediavotos: Média dos votos recebidos na avaliação.
popularidadefilme: Valor de popularidade associado à avaliação.

**fatos_filme:**

id_filme: Identificador único para cada filme (chave primária).
tituloprincipal: Título principal do filme.
anolancamento: Ano de lançamento do filme.
tempominutos: Duração do filme em minutos.
genero: Gênero do filme.
palavrachave: Palavras-chave associadas ao filme.

**financeiro:**

id_filme: Chave estrangeira referenciando a tabela de fatos (tab_normalizada).
orcamentofilme: Orçamento do filme.
receitafilme: Receita gerada pelo filme.

**Relacionamentos:**

A tabela de fatos (tab_normalizada) está relacionada às tabelas de dimensão (artista, avaliacao, fatos_filme, financeiro) por meio de chaves estrangeiras, proporcionando uma estrutura multidimensional para análises. Este modelo permite a análise detalhada dos filmes a partir de diferentes perspectivas, considerando características como artistas, avaliações, dados financeiros e informações específicas do filme. Esse design facilita consultas analíticas em um ambiente de data lake.

&nbsp;

# 5. TAREFA 5: Desafio Parte 3 - Processamento da Refined

**Processamento de dados - Camada Refined**

Na atividade anterior, você definiu seu modelo de dados da camada Refined. Agora você deve processar os dados da camada Trusted, armazenando-os na Refined, de acordo com seu modelo.

Usaremos novamente do Apache Spark no processo, utilizando jobs cuja origem sejam dados da camada Trusted Zone e e o destino, a camada Refined Zone. Aqui, novamente, todos os dados serão persistidos no formato PARQUET, particionados, se necessário,  de acordo com as necessidades definidas para a camada de visualização. Além disso, é necessário registrar as tabelas geradas no AWS Glue Data Catalog para poder fazer consultas posteriormente.

Importante:

Desenvolva os jobs no Glue utilizando a opção Spark script editor. Após, na aba Job details, atente para as seguintes opções:

+ Worker type: Informe G 1x (opção de menor configuração).

+ Requested number of workers: Informe 2, que é a quantidade mínima.

+ Job timeout (minutes): Mantenha em 60 ou menos, se possível.

Após realizar a atividade, lembre-se de finalizar qualquer execução ativa de job para não incorrer em custos desnecessários.

**Perguntas dessa tarefa:** Desenvolva os jobs de processamento de acordo com as instruções. Aqui você pode apresentar prints do seu código. Lembre-se também de adicionar todo código produzido ao seu repositório no Github.

**RESPOSTA:**

<div align="center">

![crawlers desafio 3](<Images Sprint9/crawler desafio 3.png>)

![script refined](<Images Sprint9/script_refined.png>)

</div>

```python
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_CSV', 'S3_INPUT_PATH_TMDB', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_path_csv = args['S3_INPUT_PATH_CSV']
source_path_tmdb = args['S3_INPUT_PATH_TMDB']
target_path = args['S3_TARGET_PATH']

df_input_csv = spark.read.parquet(source_path_csv)
df_input_csv = df_input_csv.withColumn("id", monotonically_increasing_id())
df_input_csv.createOrReplaceTempView("csv")

df_input_tmdb = spark.read.parquet(source_path_tmdb)
df_input_tmdb = df_input_tmdb.withColumn("id", monotonically_increasing_id())
df_input_tmdb.createOrReplaceTempView("tmdb")

# Criar tabela tab_csv
consulta_tab_csv = """
SELECT DISTINCT
    tituloPincipal AS tituloPrincipal,
    anoLancamento,
    tempoMinutos,
    genero,
    notaMedia,
    numeroVotos,
    generoArtista,
    personagem,
    nomeArtista,
    anoNascimento,
    anoFalecimento,
    profissao
FROM csv
"""

df_result_tab_csv = spark.sql(consulta_tab_csv)
df_result_tab_csv.createOrReplaceTempView("tab_csv")

# Criar tabela tab_tmdb
consulta_tab_tmdb = """
SELECT DISTINCT
    CAST(id AS STRING) AS id_filme,
    title AS tituloPrincipal,
    popularity AS popularidadeFilme,
    vote_average AS mediaVotos,
    CAST(vote_count AS INT) AS quantidadeVotos,
    CAST(budget AS INT) AS orcamentoFilme,
    CAST(revenue AS INT) AS receitaFilme,
    CAST(keywords AS STRING) AS palavraChave
FROM tmdb
"""

df_result_tab_tmdb = spark.sql(consulta_tab_tmdb)
df_result_tab_tmdb.createOrReplaceTempView("tab_tmdb")

# Criar tabela tab_normalizada
consulta_normalizada = """
SELECT DISTINCT
    CAST(t2.id_filme AS STRING) AS id_filme,
    t1.tituloPrincipal,
    t1.anoLancamento,
    t1.tempoMinutos,
    t1.genero,
    t1.notaMedia,
    t1.numeroVotos,
    t1.generoArtista,
    t1.personagem,
    t1.nomeArtista,
    t1.anoNascimento,
    t1.anoFalecimento,
    t1.profissao,
    t2.popularidadeFilme,
    t2.mediaVotos,
    CAST(t2.quantidadeVotos AS INT) AS quantidadeVotos,
    CAST(t2.orcamentoFilme AS INT) AS orcamentoFilme,
    CAST(t2.receitaFilme AS INT) AS receitaFilme,
    CAST(t2.palavraChave AS STRING) AS palavraChave
FROM tab_csv t1
INNER JOIN tab_tmdb t2 ON t1.tituloPrincipal = t2.tituloPrincipal
"""

df_result_normalizada = spark.sql(consulta_normalizada)
df_result_normalizada.createOrReplaceTempView("tab_normalizada")

# Criar tabela fatos_filme
consulta_fatos_filme = """
SELECT
    id_filme,
    tituloPrincipal,
    anoLancamento,
    tempoMinutos,
    genero,
    palavraChave
FROM tab_normalizada
"""

df_result_fatos_filme = spark.sql(consulta_fatos_filme)
df_result_fatos_filme.createOrReplaceTempView("fatos_filme")

# Criar tabela financeiro
consulta_financeiro = """
SELECT
    id_filme,
    orcamentoFilme,
    receitaFilme
FROM tab_normalizada
"""

df_result_financeiro = spark.sql(consulta_financeiro)
df_result_financeiro.createOrReplaceTempView("financeiro")

# Criar tabela avaliacao
consulta_avaliacao = """
SELECT
    id_filme,
    notaMedia,
    quantidadeVotos,
    mediaVotos,
    popularidadeFilme
FROM tab_normalizada
"""

df_result_avaliacao = spark.sql(consulta_avaliacao)
df_result_avaliacao.createOrReplaceTempView("avaliacao")

# Criar tabela artista
consulta_artista = """
SELECT
    id_filme,
    generoArtista,
    personagem,
    nomeArtista,
    anoNascimento,
    anoFalecimento,
    profissao
FROM tab_normalizada
"""

df_result_artista = spark.sql(consulta_artista)
df_result_artista.createOrReplaceTempView("artista")

# Escrever as tabelas no S3
df_result_tab_csv.write.format("parquet").mode("overwrite").save(f"{target_path}/tab_csv/")
df_result_tab_tmdb.write.format("parquet").mode("overwrite").save(f"{target_path}/tab_tmdb/")
df_result_normalizada.write.format("parquet").mode("overwrite").save(f"{target_path}/tab_normalizada/")
df_result_fatos_filme.write.format("parquet").mode("overwrite").save(f"{target_path}/fatos_filme/")
df_result_financeiro.write.format("parquet").mode("overwrite").save(f"{target_path}/financeiro/")
df_result_avaliacao.write.format("parquet").mode("overwrite").save(f"{target_path}/avaliacao/")
df_result_artista.write.format("parquet").mode("overwrite").save(f"{target_path}/artista/")

job.commit()

```

<div align="center">

![parametros](<Images Sprint9/parametros.png>)

</div>

+ **--S3_INPUT_PATH_CSV:** s3://compass.desafio3/Trusted/TMDBProcessed/CSV/

+ **--S3_INPUT_PATH_TMDB:** s3://compass.desafio3/Trusted/TMDBProcessed/TMDB/

+ **--S3_TARGET_PATH:** s3://compass.desafio3/Refined/lab_glue/tmdb_refined_crawler/

<div align="center">

![S3 Refined](<Images Sprint9/S3 refined.png>)

</div>

&nbsp;

# 📝 Certificação

+ Certificação da conclução do curso Data & Analytics AWS 9/10.

<div align="center">

![Certificado Data & Analytics AWS 9/10](<Images Sprint9/Certificado.jpg>)

</div>

---