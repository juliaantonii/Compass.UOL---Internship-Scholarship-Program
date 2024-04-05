# 🔖 **SUMÁRIO**

Nesta página encontra-se 4 Tópicos Principais, são estes:

+ **[SQL para Análise de Dados: Do Básico ao Avançado](#1-sql);**
+ **[Data & Analytics - PB - AWS 2/10 - Exercícios II](#data--analytics---pb---aws-210---exercícios-ii);**
+ **[Big Data Fundamentos 3.0](#big-data-fundamentos-30);**
+ **[Certificação](#📝-certificação).**

---

&nbsp;

# SQL para Análise de Dados: Do Básico ao Avançado

## **1. SQL**

Pode se afirmar que **SQL (Structured Query Language)** é uma linguagem de consulta, onde você aplica um comando ao banco de dados e este te retorna com uma Query, isto é, uma resposta a sua solicitação. Esta também é considerada uma linguagem de armazenamento e processar informações em um banco de dados.
Durante o estudo, será necessário utilizar o SQLite como principal ferramenta.

&nbsp;

<div align="center">

![pgadmin logo](<Images Sprint2/pqadmin.webp>)

</div>

No SQL encontramos algumas estruturas com as quais iremos trabalhas, são elas:

+ **Relações (Tabela):** Conjunto de Tuplas e Atributos;

+ **Tuplas (Linhas):** Contém informações específicas;

+ **Atributos (Colunas):** Conjunto de diferentes tipos de dados.

Para manusear e analisar o banco de dados, colocamos em prática alguns comandos, são estes:

## **2. Comandos Básicos:**

+ **SELECT:** Serve para selecionar as colunas necessárias;

+ **DISTINCT:** Serve para remover linhas duplicadas e mostrar apenas linhas distintas. Aplica-se a seguir do comando _SELECT_;

+ **WHERE:** Serve para filtrar as linhas das tabelas de acordo com a condição aplicada;

+ **ORDER BY:** Serve para ordenar a seleção de acordo com uma regra definida pelo usuário, são estas:
    + **ASC:** Segue a ordem crescente;
    + **DESC:** Segue a ordem decrescente.

+ **LIMIT:** Serve para limitar o nº de linhas da consulta.

## **3. Comandos Operadores:**

+ **OPERADORES ARITMÉTICOS:** Servem para executar operações matemáticas com a base nos dados, os operadores possíveis são:

    + **SOMA (+);**
    + **SUBTRAIR (-);**
    + **DIVISÃO (/);**
    + **MULTIPLICAÇÃO (*).**

&nbsp;

+ **OPERADORES DE COMPARAÇÃO:** Servem para realizarmos comparações entre dois valores, retornando como TRUE ou FALSE, encontramos:
  
    + **IGUAL (=);** 
    + **MAIOR (>);**
    + **MAIOR OU IGUAL (>=);**
    + **MENOR (<);**
    + **MENOR OU IGUAL (<=);**
    + **DIFERENTE (<>).**

&nbsp;

+ **OPERADORES LÓGICOS:** Servem para unir expressões simples em uma composta, encontramos:
  
    + **AND:** Todas as condições verdadeiras;
    + **OR:** Pelo menos uma condição verdadeira;
    + **NOT:** Não satisfaz a condição;
    + **BETWEEN...AND:** Dentro de um intervalo;
    + **LIKE:** Pesquisar por padrão;
    + **IN:** Possíveis valores;
    + **IS NULL:** Para determinar se uma expressão é null (nula).

&nbsp;

+ **OPERADORES DE AGREGAÇÃO:** Servem para executar operações aritméticas nos registros da coluna selecionada, temos:
  
    + **COUNT:** Contagem de todos as linhas;
    + **GROUP BY:** Serve para agrupar registros semelhantes de uma coluna;
    + **HAVING:** Serve para filtrar as linhas da seleção por uma coluna agrupada, funcionam tanto com colunas agregadas como não agregadas;
    + **SUM:** Soma dos valores de uma coluna;
    + **AVG:** Média dos valores de uma coluna;
    + **MAX:** Maior valor de uma coluna;
    + **MIN:** Menor valor de uma coluna.
  
&nbsp;

+ **COMANDOS JOINS:**

    + **LEFT JOIN:** Seleciona apenas os dados da coluna da esquerda e aqueles que estão relacionados com a coluna da direita;
    + **RIGHT JOIN:** Seleciona apenas os dados da coluna da direita e aqueles que estão relacionados com a coluna da esquerda;
    + **INNER JOIN:** Seleciona apenas os dados que derem match (são semelhantes entre si) entre as tabelas;
    + **FULL JOIN:** Seleciona todos os dados de ambas as tabelas.

&nbsp;

<div align="center">

![SQL Joins](<Images Sprint2/JOIN.png>)

**Fonte:** [**PodProgramar**](https://podprogramar.com.br/introducao-a-sql/)

</div>

&nbsp;

# Data & Analytics - PB - AWS 2/10 - Exercícios II
Os exercícios deste tópico, considerando a base de dados **biblioteca**, foram realizados com o programa SQLite e assim aplicados à plataforma. Pode se encontrar os exercícios resolvidos nos links abaixo:

+ [**SEÇÃO 3 - EXERCÍCIOS**](EXERC%C3%8DCIOS/EX_SECAO3.md);
+ [**SEÇÃO 4 - EXERCÍCIOS**](EXERC%C3%8DCIOS/EX_SECAO4.md);
+ [**SEÇÃO 6 - EXERCÍCIOS**](EXERC%C3%8DCIOS/EX.SECAO6.md).

&nbsp;

# Big Data Fundamentos 3.0
O seguinte estudo foi realizado com base nas informações do curso do [Data Science Academy](https://www.datascienceacademy.com.br/profile).

## **1. Big Data**
Conjunto de dados, considerados grandes e complexos, onde não podem ser processados por bancos de dados ou aplicações, isto é por métodos tradicionais. Estes são gerados em alta velocidade e com super densidade.
A principal importância dos dados armazenados e disponíveis é a forma com que eles são processados e para que são utilizados, sendo assim analisados e aproveitados, gerando resultados.

---

## **2. 4V's do Big Data?**
1. **Volume**: Tamanho de dados, conforme a movimentação, as informações são capturadas;

2. **Variedade**: Formato dos dados (EX: vídeo, imagens, áudio, docs, etc.);

3. **Velocidade**: Geração de dados, se refere à criação de dados e a movimentação deste;

4. **Veracidade**: Confiabilidade dos dados, analisa se as informações obtidas são verdadeiras.

---

## **3. Ciência de Dados?**
Pode se afirmar que a Ciência de Dados é um conjunto de técnicas para análise de dados, sendo divergente ao Big Data, contudo, aplicados a metodologia da Ciência de Dados para analisar o Big Data.

&nbsp;

<div align="center">

![!\[Data Science\](<Images Sprint2/1__fR-2Yg-xaWXssnj08Zqeg.webp>)](<Images Sprint2/ciclo data science.webp>)

**Fonte:** [**Medium**](https://medium.com/techbloghotmart/afinal-como-se-desenvolve-um-projeto-de-data-science-233472996c34)

</div>

---

## **4. Bancos de Dados Relacionais?**

É possível dizer que são bancos de dados estruturados e com schema bem definido, estes dados são aplicados em tabelas que se relacionam entre si. Valendo ressaltar que Schema é a organização de dados, criado antes de armazenar as informações.

---
## **5. Bancos de Dados Não Relacionais (NoSQL)?**

Tem origem do princípio que os dados podem ser semi ou não estruturados, onde estes possuem formatos muito diferentes, não se relacionando em suas organizações. Abaixo visualizamos os diversos tipos de bancos de dados NoSQL:

&nbsp;

<div align="center">

![NoSQL](<Images Sprint2/NOSQL2.png>)

**Fonte:** [**Gran**](https://blog.grancursosonline.com.br/nosql-ja-ouvir-falar/)

</div>

---

## **6. Armazenamento Paralelo**

Consiste em distribuir o armazenamento de dados através de diversos servidores (computadores), aumentando assim a capacidade de armazenar informações. Este é construido com base em uma estrutura, onde:

+ **World (Mundo)**: Representa as informações externas que serão coletadas;

+ **Switch**: Dispositivo que controla o tráfego de rede e assim envia aos computadores;

+ **Rack**: Estrutura física responsável por manter o computador/servidor;

+ **Clusters**: Consiste em computadores fracamente ou fortemente ligados que trabalham em conjunto, de modo que, em muitos aspectos, podem ser considerados como um único sistema.

+ **Sistema de Arquivo**: Software responsável por gerenciar a forma que vai gravar/armazenar as informações/arquivos coletados, mantendo assim uma conexão entre software e hardware, exemplos desde sistema são: NTFS, ext3, etc;

+ **Hadoop HDFS (Hadoop Distributed File System)**: Sistema de arquivos distribuídos que fornece acesso de alta capacidade aos dados do aplicativo sem a necessidade de definir esquemas antecipadamente.

&nbsp;

<div align="center"

![armazenamento paralelo](<Images Sprint2/armazenamento paralelo.png>)

**Fonte:** [**TIBCO**](https://www.tibco.com/pt-br/reference-center/what-is-massively-parallel-processing)

</div>

---

## **7. Cloud Computing**

É a computação em nuvem, esta que entrega serviços de computação, abrangendo servidores, armazenamento, bancos de dados, rede, software, análise e inteligência por meio da internet, ofertando métodos e recursos flexíveis e inovadores, além disso tudo, estes serviços apresentam um ótimo custo benefício.

---

## **8. Machine Learning**

O MLOps (Machine Learning Ops) é um conjunto de práticas para colaboração e comunicação entre Cientistas de Dados e Profissionais de Operações, normalmente é uma tarefa realizada pelo engenheiro de Machine Learning.

O objetivo principal do MLOps é superar os desafios que surgem quando os modelos de aprendizagem de máquina são implementados em ambientes do mundo real. Abaixo vemos alguns exemplos de como se aplica o MLOps:

+ Análise de dados com base em conhecimentos  em desenvolvimento  e  implantação  de aplicações  web;

+ Mudança dos objetivos de negócios no modelo, mantendo os padrões de desempenho;

+ Auxilia nas lacunas de comunicação entre as equipes técnicas e de negócios que não possuemuma  linguagem  comum;

+ Avaliar o risco / custo de algumas falhas encontradas.

Além de todo esse conhecimento, também devemos compreender algum destes termos:

+ **DevOps**: Abordagem para desenvolvimento de software que acelera o ciclo de vida de construção usando automação, otimizando o tempo de produção;

+ **AIOps**: AIOps é a fusão de Inteligência Artificial (IA) com Operações de TI, otimizando a análise e resolução automatizada de problemas complexos relacionados à área de banco de dados;

+ **DataOps**: Metodologia ágil e orientada a processos para desenvolver e entregar análises. Esta fornece ferramentas, processos e estruturas organizacionais. Possui como objetivo desenvolver produto de dados e ativar dados com valor comercial;

---

## **9. O que é DAAS?**

DaaS (Data as a Service) é um modelo onde dados são fornecidos e gerenciados por terceiros, permitindo acesso e uso sob demanda. Abaixo podemos observar os principais benefícios do DaaS:


<div align="center">

![Benefícios de Daas](<Images Sprint2/Benefícios do Daas.png>)

**Fonte:** [**Data Science Academy**](https://www.datascienceacademy.com.br/profile)
</div>

---

&nbsp;

# 📝 Certificação

+ Certificação da conlusão do Curso de Certificado SQL Análise de Dados: Do Básico ao Avançado de 6hrs.

![Certificado SQL Análise de Dados: Do Básico ao Avançado](<Images Sprint2/Certificado SQL Análise de Dados - Do Básico ao Avançado.jpg>)

+ Certificação da conlusão do Curso de Data Analytics - PB - AWS 2/10.

![Certificado Data Analytics AWS 2](<Images Sprint2/Certificação Data Analytics AWS 2.jpg>)

+ Certificação da conlusão do Curso de Big Data Fundamentos 3.0 de 12hrs.
  
![Certificado Big Data Fundamentos 3.0](<Images Sprint2/Certificado Big Data Fundamentos 3.0.jpg>)

---