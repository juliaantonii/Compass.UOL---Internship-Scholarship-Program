# 🔖 **SUMÁRIO**

Nesta página encontra-se 4 Tópicos Principais, são estes:

+ **[Hadop, MapReduce for Big Data Problems](#1-hadop-mapreduce-for-big-data-problems);**
+ **[Formação Spark com Pyspark: Curso Completo](#2-formação-spark-com-pyspark-curso-completo);**
+ **[Exercícios - Laboratórios AWS](#exercícios---laboratórios-aws);**
  + **[Tarefa 1: Python com Pandas e Numpy](#tarefa-1-python-com-pandas-e-numpy);**
  + **[Tarefa 2: Apache Spark - Contador de Palavras](#tarefa-2-apache-spark---contador-de-palavras);**
  + **[Lab AWS Glue](#lab-aws-glue);**
  + **[Tarefa 3: Desafio Parte 1 - ETL](#tarefa-3-desafio-parte-1---etl);**
+ **[Certificação](#📝-certificação).**

---

&nbsp;

# 1. Hadop, MapReduce for Big Data Problems

Hadoop é um framework de código aberto projetado para armazenar e processar dados em grande escala (big data) em clusters de servidores. Foi desenvolvido pela Apache Software Foundation e é amplamente utilizado em todo o mundo para gerenciar e analisar grandes volumes de dados. Hadoop é composto por vários componentes-chave que trabalham juntos para gerenciar eficazmente dados em grande escala. Aqui está uma explicação dos principais componentes do Hadoop:

+ **Hadoop Distributed File System (HDFS):** O HDFS é o sistema de arquivos distribuído do Hadoop. Ele foi projetado para armazenar grandes arquivos de dados de forma redundante em vários nós (servidores) de um cluster. O HDFS divide os arquivos em blocos menores (normalmente de 128 MB a 256 MB) e os distribui pelos nós do cluster. Isso permite alta escalabilidade e alta disponibilidade dos dados.

+ **MapReduce:** O MapReduce é um modelo de programação e um sistema de processamento em lote que permite o processamento de dados distribuídos em um cluster Hadoop. Ele funciona em duas etapas: a fase "Map" para o processamento inicial dos dados, seguida pela fase "Reduce" para agregar os resultados. O MapReduce permite a paralelização eficiente do processamento de dados.

+ **YARN (Yet Another Resource Negotiator):** O YARN é o gerenciador de recursos do Hadoop. Ele gerencia a alocação de recursos (CPU, memória, etc.) para as tarefas em execução no cluster. O YARN substituiu o gerenciador de recursos originalmente usado pelo MapReduce, oferecendo maior flexibilidade para executar diversas cargas de trabalho no mesmo cluster.

+ **Hadoop Common:** Este é um conjunto de bibliotecas e utilitários compartilhados usados pelos outros componentes do Hadoop. Ele inclui ferramentas para gerenciar o cluster, bibliotecas para manipular arquivos e logs, bem como ferramentas de monitoramento de desempenho.

+ **Ecossistema Hadoop:** Além desses componentes principais, o ecossistema Hadoop inclui muitos projetos e ferramentas adicionais para lidar com diferentes tipos de dados e executar tarefas diversas, como Hive (processamento de dados semelhante a SQL), Pig (linguagem de script para processamento de dados), HBase (banco de dados NoSQL), Spark (processamento de dados em memória) e muito mais.

O Hadoop é especialmente adequado para o processamento de dados em grande escala, como análise de logs, mineração de dados, processamento de dados geoespaciais e outras aplicações que exigem alta escalabilidade e tolerância a falhas. Ele foi amplamente adotado em diversos setores, incluindo empresas, pesquisa, mídias sociais e outros, para resolver problemas relacionados a big data.

<div align="center">

![Hadoop](<Images Sprint7/Hadoop.png>)

</div>

# 2. Formação Spark com Pyspark: Curso Completo

Spark é um framework de código aberto amplamente utilizado para processamento de dados em grande escala e análise de big data. Ele foi desenvolvido para ser rápido, flexível e escalável, sendo projetado para lidar com uma variedade de tipos de tarefas de processamento de dados, incluindo processamento em lote, processamento em tempo real, aprendizado de máquina e análise interativa.

Aqui estão algumas características-chave do Spark:

+ **Velocidade:** O Spark é conhecido por sua velocidade. Ele mantém os dados em memória sempre que possível, o que reduz significativamente o tempo de acesso aos dados. Isso o torna muito mais rápido do que sistemas de processamento de big data tradicionais, como o Hadoop MapReduce.

+ **Flexibilidade:** O Spark oferece suporte a várias linguagens de programação, incluindo Scala, Python, Java e R. Isso permite que os desenvolvedores escolham a linguagem com a qual se sintam mais confortáveis.

+ **Escalabilidade:** O Spark é altamente escalável e pode ser usado em clusters de servidores para processar grandes volumes de dados de forma distribuída. Ele é projetado para dimensionar horizontalmente, o que significa que você pode adicionar mais máquinas ao cluster conforme suas necessidades de processamento crescem.

+ **Suporte a Diversos Workloads:** O Spark suporta uma ampla gama de workloads, incluindo processamento em lote (usando o Spark Core e o Spark SQL), streaming em tempo real (usando o Spark Streaming), análise de gráficos (usando o GraphX) e aprendizado de máquina (usando o MLlib).

Agora, o PySpark é a interface Python para o Apache Spark. Ele permite que os desenvolvedores usem a potência do Spark em seus programas Python. Com o PySpark, você pode escrever aplicativos Spark usando Python, aproveitando todas as capacidades de processamento e análise distribuída do Spark.

Algumas características do PySpark:

+ **API Python:** O PySpark oferece uma API Python completa para interagir com o Spark, o que o torna uma opção conveniente para desenvolvedores que estão familiarizados com Python.

+ **Integração com Bibliotecas Python:** Você pode facilmente integrar bibliotecas Python populares, como NumPy, Pandas e scikit-learn, com o PySpark para realizar análises de dados mais avançadas e processamento de machine learning.

+ **Acesso a todas as funcionalidades do Spark:** Com o PySpark, você pode acessar todas as funcionalidades e componentes do Spark, incluindo Spark SQL, Spark Streaming e MLlib.

Em resumo, o Spark é um poderoso framework de processamento de big data, enquanto o PySpark é a interface Python que permite que você aproveite o Spark usando a linguagem de programação Python. Juntos, eles oferecem uma solução flexível e eficaz para processamento e análise de grandes volumes de dados.

# Exercícios - Laboratórios AWS

## Tarefa 1: Python com Pandas e Numpy

Nesta tarefa iremos utilizar as bibliotecas Pandas e NumPy para responder a quatro exercícios. Lembre-se de adicionar o código desenvolvido ao seu repositório no GitHub para que o monitor(a) da Sprint possa avaliá-lo posteriormente.

<div align="center">

![Spark](<Images Sprint7/Spark.png>)

![Spark Actors](<Images Sprint7/Spark Actors.png>)

</div>

_**1. Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.**_

_**Resposta:**_ O ator/atriz com maior número de filmes é Robert DeNiro com 79 filmes.

<div align="center">

![T1 Ex1](<Images Sprint7/T1Ex1.png>)

</div>

_**2. Apresente a média da coluna contendo o número de filmes.**_

_**Resposta:**_ A média do número de filmes é 37.88.

<div align="center">

![T1 Ex2](<Images Sprint7/T1Ex2.png>)

</div>

_**3. Apresente o nome do ator/atriz com a maior média por filme.**_

_**Resposta:**_ O ator/atriz com maior média por filme é Anthony Daniels com 451.8 de Média.

<div align="center">

![T1 Ex3](<Images Sprint7/T1Ex3.png>)

</div>

_**4. Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.**_

_**Resposta:**_ Ranking dos 5 filmes de acordo com a frequência no dataset

1 - O filme The Avengers aparece 6 vez(es) no dataset

2 - O filme Harry Potter / Deathly Hallows (P2) / aparece 4 vez(es) no dataset

3 - O filme Catching Fire aparece 4 vez(es) no dataset

4 - O filme The Dark Knight aparece 3 vez(es) no dataset

5 - O filme Star Wars: The Force Awakens aparece 3 vez(es) no dataset

<div align="center">

![T1 Ex4](<Images Sprint7/T1Ex4.png>)

</div>

&nbsp;

## Tarefa 2: Apache Spark - Contador de Palavras

Neste atividade você irá desenvolver um job de processamento com o framework Spark por meio de um container Docker. Lembre-se que seu código-fonte deverá estar no GitHub para posterior avaliação do monitor(a) da Sprint.

_**1. Realizar o pull da imagem jupyter/all-spark-notebook e Criar um container a partir da imagem.**_

_**Resposta:**_

<div align="center">

![Container T2](<Images Sprint7/ContainerT2.png>)

![Jup Img T2](<Images Sprint7/Jup Img T2.png>)

![Pyspark](<Images Sprint7/Pyspark.png>)

![Jupyter Lab](<Images Sprint7/JupyterLab.png>)

</div>

_**3 - Em outro terminal, execute o comando `pyspark` no seu container. Pesquise sobre o comando  docker exec para realizar esta ação. Utilize as flags -i e -t no comando.**_

_**Resposta:**_ O README.md usado para teste de leitura foi o [Contador de Palavras](https://github.com/juliaantonii/Contador-de-Palavras).

<div align="center">

![Exec Pyspark](<Images Sprint7/Exec Pyspark.png>)

![Comandos](<Images Sprint7/Comandos.png>)

![Comandos Usados](<Images Sprint7/Comandos Usados.png>)

![Contagem de Palavras](<Images Sprint7/Contagem de Palavras.png>)

</div>

## Lab AWS Glue

Processos de ETL (Extract, Transform and Load) estão presentes em todos os projetos de dados. O cenário costuma ser o mesmo: fontes de dados diversas com datasets de interesse que precisam ser ingeridos, transformados e armazenados em um ou mais destinos, com formatos diferentes da origem.

Neste laboratório você será guiado na construção de um processo de ETL simplificado utilizando o
serviço AWS Glue.

_**1. Preparando os dados de origem**_

<div align="center">

![Bucket Compass Lab](<Images Sprint7/Bucket Compass Lab.png>)

</div>

_**2. Criando a IAM Role para os jobs do AWS Glue**_

<div align="center">

![AWS Glue Role](<Images Sprint7/AWSGlueRole.png>)

</div>

_**3 - Configurando as permissões no AWS Lake Formation**_

![Database1](<Images Sprint7/Database1.png>)

![Database2](<Images Sprint7/Database2.png>)

![Database3](<Images Sprint7/Database3.png>)

</div>

_**4. Criando novo job no AWS Glue**_

<div align="center">

![Job 1](<Images Sprint7/Job1.png>)

![Job 2](<Images Sprint7/Job2.png>)

![Job 3](<Images Sprint7/Job3.png>)

</div>

_**5. Sua vez!**_

<div align="center">

![Script](<Images Sprint7/Script.png>)

</div>

_**6 - Criando novo crawler**_

<div align="center">

![Crawlers](<Images Sprint7/Crawlers.png>)

![Tables](<Images Sprint7/Tables.png>)

![Frequencia Registro Nomes EUA 1](<Images Sprint7/Frequencia Registro Nomes EUA 1.png>)

![Frequencia Registro Nomes EUA 2](<Images Sprint7/Frequencia Registro Nomes EUA 2.png>)

![Query](<Images Sprint7/Query Describe 1.png>)

![SQL Permitions](<Images Sprint7/SQL.png>)

</div>

## Tarefa 3: Desafio Parte 1 - ETL

Ingestão Batch: a ingestão dos arquivos CSV em Bucket Amazon S3 RAW Zone. Nesta etapa do desafio deve ser construído um código Python que será executado dentro de um container Docker para carregar os dados locais dos arquivos para a nuvem. Nesse caso utilizaremos, principalmente, as lib boto3 como parte do processo de ingestão via batch para geração de arquivo (CSV).

_**1. Implementar código Python:**_

+ ler os 2 arquivos (filmes e series) no formato CSV inteiros, ou seja, sem filtrar os dados

+ utilizar a lib boto3 para carregar os dados para a AWS

+ acessar a AWS e grava no S3, no bucket definido com RAW Zone

    + no momento da gravação dos dados deve-se considerar o padrão: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>
    Por exemplo:

                   S3:\\data-lake-do-fulano\Raw\Local\CSV\Movies\2022\05\02\movies.csv

                   S3:\\data-lake-do-fulano\Raw\Local\CSV\Series\2022\05\02\series.csv

_**Resposta:**_

![Script T3](<Images Sprint7/Script T3.png>)

_**2. Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado**_

<div align="center">

![Dockerfile](<Images Sprint7/Dockerfile.png>)

![Container T3](<Images Sprint7/Container T3.png>)

![Docker Run](<Images Sprint7/Docker Run.png>)

![Docker Run2](<Images Sprint7/Docker Run2.png>)

![Leitura de Movies](<Images Sprint7/Leitura Movies.png>)

![Leitura de Series](<Images Sprint7/Leitura Series.png>)

</div>

&nbsp;

# 📝 Certificação

+ Certificação da conclução do curso Formação Spark com Pyspark de 11hrs.

<div align="center">

![Certificado Formação Spark com Pyspark](<Images Sprint7/Certificado Formação Spark com Pyspark.jpg>)

</div>

+ Certificação da conclução do curso Learn By Example: Hadoop, MapReduce for Big Data problems de 14hrs.

<div align="center">

![Certificado Hadoop](<Images Sprint7/Certificado Hadoop.png>)

</div>

---