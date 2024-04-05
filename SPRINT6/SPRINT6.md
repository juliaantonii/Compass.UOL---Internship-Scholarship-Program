# 🔖 **SUMÁRIO**

Nesta página encontra-se 4 Tópicos Principais, são estes:

+ **[Data Analytics Fundamentals](#1-data-analytics-fundamentals);**
+ **[Data Analytics on AWS - Business](#2-data-analytics-on-aws---business);**
+ **[Exercícios - Laboratórios AWS](#exercícios---laboratórios-aws);**
  + **[Lab AWS S3](#2-lab-aws-s3);**
  + **[Lab AWS Athena](#3-lab-aws-athena);**
  + **[Lab AWS Lambda](#4-lab-aws-lambda);**
+ **[Certificação](#📝-certificação).**

---

&nbsp;

# 1. Data Analytics Fundamentals

##  Introdução

Neste tópico vamos analisar o conceito de análise de dados e as soluções de avaliação de dados, além dos cinco desafios da avaliação de dados, isto é, os 5 V's.

+ **Avaliação:** É um exame detalhado de algo para entender sua natureza ou determinar suas características essenciais.

+ **Avaliação de Dados:** É o processo de compilar, processar e analisar dados para que você possa usá-los para tomar decisões.

## Volume

Quando as empresas têm mais dados do que conseguem processar e analisar, elas têm um problema de volume.

<div align="center">

![Volume](<Images Sprint6/Volume.jpg>)

</div>

Há três classificações amplas de tipos de origem dos dados:

+ **Dados Estruturados:** são organizados e armazenados na forma de valores que são agrupados em linhas e colunas de uma tabela.

+ **Dados Semiestruturados:** muitas vezes são armazenados em conjuntos de pares de chave-valor que são agrupados em elementos em um arquivo.

+ **Dados Não Estruturados:** não são estruturados de forma consistente. Alguns dados podem ter uma estrutura semelhante a dados semiestruturados, mas outros podem conter apenas metadados.

O Amazon S3 é um armazenamento de objetos criado para armazenar e recuperar qualquer quantidade de dados de qualquer lugar. Para aproveitar ao máximo o Amazon S3, você precisa entender alguns conceitos simples. Em primeiro lugar, o Amazon S3 armazena dados como objetos em buckets.

+ **Objeto:** É composto por um arquivo e quaisquer metadados que descrevam esse arquivo.

+ **Buckets:** São contêineres lógicos para objetos.

Depois que os objetos foram armazenados em um bucket do Amazon S3, eles recebem uma chave de objeto. Veja abaixo um exemplo de URL para um único objeto em um bucket chamado doc, com uma chave de objeto composta pelo prefixo 2006-03-01 e o arquivo nomeado AmazonS3.html.

<div align="center">

![URL AmazonS3](<Images Sprint6/Link Endereço AmazonS3.png>)

</div>

### Atividade 1

**_Qual dos seguintes elementos faz parte de um URL de objeto do Amazon S3?_**

**_Resposta:_** Chave do objeto e Bucket.

## Veracidade

Quando se tem dados que não são controlados, provenientes de vários sistemas diferentes e não consegue fazer curadoria dos dados de maneiras significativas, você sabe que tem um problema de veracidade.

+ **Integridade dos Dados:** é a manutenção e a garantia de precisão e consistência dos dados durante todo o seu ciclo de vida.

+ **Veracidade:** dos dados é o grau em que os dados são exatos, precisos e confiáveis.

<div align="center">

![Veracidade](<Images Sprint6/Veracidade.jpg>)

**Fonte: [AWS Skill Builder](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/570/data-analytics-fundamentals-portuguese)**

</div>

Para garantir a integridade dos dados durante todas essas etapas, você pode seguir as seguintes práticas:

+ **Criação de Dados:**

    + Estabeleça padrões e políticas para a entrada de dados corretos desde o início.
    + Utilize validações e verificações para garantir que os dados criados estejam livres de erros.

+ **Agregação de Dados:**

    + Mantenha documentação detalhada sobre como os dados são agregados e de onde eles vêm.
    + Verifique a integridade dos dados após a agregação para identificar qualquer discrepância.

+ **Armazenamento de Dados:**

    + Armazene dados em sistemas seguros e resilientes.
    + Implemente controles de acesso para proteger os dados contra alterações não autorizadas.

+ **Acesso aos Dados:**

    + Controle o acesso aos dados, garantindo que apenas pessoas autorizadas possam visualizá-los ou modificá-los.
    + Registre todas as ações de acesso para fins de auditoria.

+ **Arquivamento de Dados:**

    + Arquive dados de acordo com políticas de retenção bem definidas.
    + Verifique a integridade dos dados ao longo do processo de arquivamento.

+ **Compartilhamento de Dados:**

    + Estabeleça políticas claras de compartilhamento de dados, incluindo permissões e restrições.
    + Utilize métodos seguros para compartilhar dados externamente, quando necessário.

Como discutimos, bancos de dados relacionais dependem de esquemas de banco de dados para organizar o conteúdo dentro do banco de dados e impor a integridade referencial e de domínio. Os programadores também usam esses esquemas ao escrever o software para interagir com o banco de dados. Alguns desses esquemas são:

+ **Esquemas de Dados:** Um esquema de dados é o conjunto de metadados usado pelo banco de dados para organizar objetos de dados e impor restrições de integridade. O esquema define os atributos do banco de dados, fornecendo as descrições de cada objeto e como ele interage com outros objetos no banco de dados. Um ou mais esquemas podem residir no mesmo banco de dados.

+ **Esquemas Lógicos:** Os esquemas lógicos se concentram nas restrições a serem aplicadas aos dados no banco de dados. Isso inclui a organização de tabelas, visualizações e verificações de integridade.

+ **Esquemas Físicos:** Os esquemas físicos se concentram no armazenamento real de dados em disco ou em um repositório de nuvem. Esses esquemas têm detalhes sobre os arquivos, índices, tabelas particionadas, clusters e muito mais.

### Atividade 1

**_Em que estágio do ciclo de vida dos dados os consumidores testarão a veracidade dos dados?_**

**_Resposta:_** Compartilhamento.

### Atividade 2

**_Quais das perguntas a seguir devem ser feitas ao se preparar para uma avaliação da integridade dos dados?_**

**_Resposta:_** Qual deve ser a limpeza?, O que é uma alteração aceitável? e Os dados originais têm valor?

### Atividade 3

**_Faça a correspondência entre cada tipo de integridade ou esquema e a respectiva definição._**

**_Resposta:_**

| Integridade | Definição |
|---|---|
| Integridade relacional | Garante que ambos os membros de uma relação permaneçam consistentes |
| Integridade da entidade | Garante que os valores em um campo permaneçam consistentes |
| Esquema de informações | Um banco de dados de metadados contendo informações sobre todos os objetos do banco de dados |
| Esquema lógico | Lista as restrições, relações e propriedades de tabelas e exibições em um banco de dados |

&nbsp;

Para manter a veracidade nos dados armazenados, consistência é essencial. Quando dados são armazenados como arquivos, a consistência é controlada pelo aplicativo que está desenvolvendo os arquivos. Quando os dados são armazenados em um banco de dados, a consistência é responsabilidade do banco de dados que os armazena. 

+ **ACID:** Acrônimo para Atomicidade, Consistência, Isolamento e Durabilidade. É um método para manter a consistência e a integridade em um banco de dados estruturado.

    O objetivo de um banco de dados compatível com ACID é retornar a versão mais recente de todos os dados e garantir que os dados inseridos no sistema atendam a todas as regras e restrições atribuídas em todos os momentos.

+ **BASE:** Acrônimo para BAsicamente disponível, eStado flexível, Eventualmente consistente. É um método para manter a consistência e a integridade em um banco de dados estruturado ou semiestruturado.

    O objetivo é que a alteração acabe sendo totalmente consistente em toda a frota. 

<div align="center">

![Tabela ACID x BASE](<Images Sprint6/Tabela ACID x BASE.png>)

**Fonte: [AWS Skill Builder](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/570/data-analytics-fundamentals-portuguese)**

</div>

### Atividade 4

**_Quando a consistência das alterações em todas as instâncias é a minha principal preocupação, a conformidade com ___________ é o método apropriado para impor a conformidade._**

**_Resposta:_** ACID.

### Atividade 5

**_Quando os dados estão sendo gerados em um ambiente altamente ativo e a disponibilidade é minha principal preocupação, a conformidade com ___________ é o método apropriado para impor a conformidade._**

**_Resposta:_** BASE.

**Extração, transformação e carregamento (ETL)** é o processo de coletar dados de origens brutas e transformá-los em um tipo comum. Esses novos dados são carregados em um local final para serem disponibilizados para avaliação e inspeção analíticas. Em ambientes modernos baseados na nuvem, geralmente nos referimos a esse processo como ELT (extração, transformação e carregamento). As etapas são simplesmente executadas em uma ordem diferente, mas o resultado é o mesmo.

Há quatro áreas principais para as quais você deve planejar na etapa de **extração dos dados**.

1. Você deve identificar onde todos os dados de origem residem. Esses dados podem ser armazenados on-premises por sua empresa, mas também podem incluir dados encontrados on-line.

2. Você deve planejar cuidadosamente quando a extração ocorrerá devido ao possível impacto do processo de cópia no sistema de origem.

3. Você deve planejar onde os dados serão armazenados durante o processamento. Ele geralmente é chamado de local intermediário.

4. Você deve planejar com quefrequência a extração deve ser repetida.

Na etapa de **transformação dos dados**, devemos seguir um formato uniforme e consultável, essa fase envolve o uso de uma série de regras e algoritmos para inserir os dados no formato final. A limpeza de dados também ocorre durante essa parte do processo.

As transformações podem ser básicas, como a limpeza de dados para atualizar formatos ou fazer substituições de dados. Pode ser a substituição de valores NULL por zero ou a substituição da palavra feminino pela letra F. Essas alterações aparentemente pequenas podem ter um grande impacto sobre a utilidade desses dados para analistas posteriormente, no processo de visualização.

Por fim, temos a etapa de **carregar os dados**, onde escolhemos um local para carregar os dados recém-transformados. Na fase de transformação ditamos o formato que o datastore terá, esse formato pode ser um banco de dados, um data warehouse ou um data lake. Assim que o processo for concluído com êxito, os dados nesse local estarão prontos para serem analisados.

Quando se trata de executar o componente de transformação de dados do ETL, há duas opções na AWS: o Amazon EMR e o AWS Glue. Esses dois serviços fornecem resultados semelhantes, mas exigem diferentes quantidades de conhecimento e investimento de tempo.

+ **Amazon EMR:** É uma abordagem mais prática para criar seu pipeline de dados.

+ **AWS Glue:** É uma ferramenta de ETL gerenciada sem servidor que oferece uma experiência muito mais simplificada do que o Amazon EMR.

### Atividade 6

**_Quais das afirmações a seguir sobre os serviços de ETL da AWS são verdadeiras?_**

**_Resposta:_** 
Os serviços de ETL da AWS podem transformar dados relacionais em dados não relacionais e Os serviços de ETL da AWS podem transformar dados em arquivos de dados armazenados no Amazon S3.

## Valor

Quando há grandes volumes de dados usados para corroborar algumas informações valiosas, você pode estar perdendo o valor dos seus dados.

Armazenar terabytes de dados que nunca ninguém verá, analisará ou visualizará é um esforço inútil. O esforço real deve ser para descobrir qual é o valor real dos dados e aprender maneiras de extrair esse valor dos terabytes de dados coletados pela sua empresa.

<div align="center">

![Valor](<Images Sprint6/Valor.jpg>)

**Fonte: [AWS Skill Builder](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/570/data-analytics-fundamentals-portuguese)**

</div>

Análise de informações é o processo de análise de informações para encontrar o valor contido nelas. Tendo isso em mente, podemos afirmar que podemos seguir as seguintes analises:

+ **Avaliação Descritiva: O QUE ACONTECEU?** Utiliza-se dos dados disponíveis como única entrada considerada, exiginto maior nível de esforço e interpretação dos humanos.

+ **Avaliação Diagnóstica: POR QUE ISSO ACONTECEU?** Ocorre a comparação dos dados históricos com os outros dados, analisando se há dependências e padrões que podem dispor de respostas.

+ **Avaliação Preditiva: O QUE ACONTECERÁ?** Utiliza das informações geradas da avaliação descritiva e diagnóstica, prevendo eventos futuros.

+ **Avaliação Prescritiva: O QUE DEVO FAZER?** Utilizada para receitar ações a serem tomadas com base nos dados fornecidos até então.

+ **Avaliação Cognitiva e Artificial: QUAIS SÃO AS AÇÕES RECOMENDADAS?** Envolve o uso de tecnologia e algoritmos para entender e avaliar processos mentais, tomar decisões ou melhorar o desempenho cognitivo.

É importante ter uma compreensão sólida da velocidade que você pode esperar dos diferentes tipos de processamento.

+ **Análise em Batch:** Envolve consulta a grandes quantidades de dados “frios”. A análise em batch é implementada em grandes conjuntos de dados para produzir um grande número de resultados analíticos de forma regular.

+ **Análise Interativa:** Envolve a execução de consultas intrincadas em conjuntos de dados complexos em altas velocidades. Esse tipo de análise é interativo, pois permite que o usuário consulte e veja os resultados imediatamente.

+ **Análise em Stream:** Exige a ingestão de uma sequência de dados e a atualização incremental de métricas, relatórios e estatísticas de resumo em resposta a cada registro de dados recebido. Esse método é mais adequado para funções de monitoramento e resposta em tempo real.

Abaixo apresentamos os componentes e os serviços envolvidos:

1. **Ingerir/Coletar:** Você pode coletar dados de duas maneiras: em batches grandes ou em um processo de stream.

<div align="center">

![Coletar Serviços](<Images Sprint6/Coletar dados - Serviços.png>)

</div>

2. **Armazenar:** Você pode armazenar dados de duas maneiras: armazenando objetos ou armazenando registros em um banco de dados ou data warehouse.

<div align="center">

![Armazenar Serviços](<Images Sprint6/Armazenar dados - Serviços.png>)

</div>

3. **Processar:** O processamento e a análise de dados são feitos em vários estágios diferentes, sendo um processo iterativo. Há o processamento e a limpeza iniciais pelos quais os dados passarão. Em seguida, os dados serão colocados em um datastore analítico. Isso pode ocorrer no nível de objeto ou registro. Os dados podem ser reprocessados e analisados a partir do datastore analítico.

<div align="center">

![Processar Serviços](<Images Sprint6/Processar dados - Serviços.png>)

</div>

4. **Consumir/Visualizar:** Você pode consumir e visualizar dados de diversas maneiras, usando uma grande variedade de ferramentas. Muitas vezes, a ferramenta para consumir e visualizar os dados é a mesma.

<div align="center">

![Consumir Serviços](<Images Sprint6/Consumir dados - Serviços.png>)

</div>

### Atividade 1

**_Faça a correspondência entre cada pergunta e o tipo de análise necessário para respondê-la._**

**_Resposta:_**

<div align="center">

| Tipo de Análise | Pergunta |
| --- | --- |
| Descritivo | Quais foram as vendas totais em abril? |
| Diagnóstico | Qual é o total de vendas ano a ano para a região Ásia-Pacífico? |
| Prescritivo | Quais produtos devo comprar se gosto do time Seattle Seahawks? |
| Preditivo | Qual é o crescimento projetado para internações relacionadas a tabagismo no próximo ano? |
| Cognitivo | Qual é o número médio de veículos detectados pela minha campainha de vídeo? |

</div>

&nbsp;

> “A análise de dados eficaz é mais do que apenas dados e gráficos. É sobre encontrar e contar uma história.” - Glen Rabie

Os relatórios analíticos são apresentados em vários formatos e tamanhos diferentes. A origem dos dados raramente afeta os relatórios resultantes. Os relatórios são organizados para atender às necessidades dos consumidores dos relatórios. Os relatórios podem sem:

+ Relatórios Estáticos;

+ Relatórios Interativos;

+ Painéis.

Relatórios e painéis são compostos por vários gráficos e tabelas para responder perguntas.

### Atividade 2

**_Quais das opções a seguir são tipos de relatório? (Escolha três alternativas.)_**

**_Resposta:_** Estático, Interativo e Painel.

&nbsp;

# 2. Data Analytics on AWS - Business

## Oportunidade de Mercado

+ Dados como um ativo estratégico para as empresas;
+ Desafios da análise de dados enfrentados pelas atuais empresas;
+ Pipeline de análise de dados e o Data Flywheel.

Inicialmente devemos ter em mente o que é Big Data, podemos afirmar que são dados elevada quantidade e com exponencial crescimento, tornando seu armazenamento e gerenciamento um desafio. Seus principais aspectos são: Volume, Velocidade, Variedade e Veracidade. 

Os dados obtidos se transformam em **insights**, assim obtém de valor econômico e oferece serviços personalizados, dados são informações sobre pessoas, eventos, itens e transações, estas informações precisam ser transmitidas, processadas, analisadas e armazenadas. 

> **Obs: Insight é a compreensão de uma causa e efeito específicos dentro de um contexto específico.**

Assim como apresentado no módulo passado, o Big Data possui os 4 V's nas suas características, são estes:

+ **Volume:** Escala de tamanho de dados;

+ **Velocidade:** Taxa de criação e crescimento dos dados;

+ **Variedade:** Variedade dos formatos;

+ **Veracidade:** Incerteza dos dados.

As empresas orientadas por dados veem e tratam os dados como ativo estratégico, isto é, seguem os seguintes passos:

1. Coletar e reter todos os dados;
2. Transformam dados em insights;
3. Disponibilizar dados para usuários e clientes relevantes;
4. Criar novos produtos e serviços;
5. Invista em tecnologias de processamento de dados.

Há muitas formas de analisarmos os dados, algumas ferramentas são:

+ Hadoop (2006);
+ ElasticSearch (2010);
+ Presto (2012);
+ Spark (2014).

Um pipeline de dados é uma série de etapas de processamento para preparar dados corporativos para análise. 

<div align="center">

![Pipeline Dados](<Images Sprint6/Pipeline Dados.png>)

**Fonte: [Data Science Tech](https://blog.dsbrigade.com/pipeline-de-dados-com-servicos-aws/)**

</div>

Para criarmos um bom pipeline de análise de dados com AWS podemos utilizar das seguintes ferramentas para cada uma das etapas:

<div align="center">

| Etapa | Ferramenta AWS |
|---|---|
| Coletar | Amazon Kinesis Data Streams, Amazon Kinesis Data Firehouse, AWS Snowball, AWS Direct Connect |
| Armazenamento | Amazon S3, Amazon S3 Glacier, Amazon DynamoDB, Amazon RDS, Amazon ES, Amazon CloudSearch, Amazon Aurora |
| Processar / Analisar | Amazon EMR, Amazon Athena, Amazon Redshift, Amazon Kinesis Data Analytics, Amazon SageMaker |
| Visualizar | Amazon QuickSight |

</div>

&nbsp;

### Atividade 1

**_Qual é a primeira etapa de uma jornada do cliente para se tornar uma empresa orientada por dados?_**

**_Resposta:_** Migrar dados on-premises para a nuvem.

### Atividade 2

**_Quais são as quatro características do big data?_**

**_Resposta:_** Volume, velocidade, variedade, veracidade.

### Atividade 3

**_Quais são os dois desafios comuns que as empresas enfrentam na análise de big data?_**

**_Resposta:_** Falta de conhecimento técnico e privacidade e segurança de dados.

### Atividade 4

**_Quais são os componentes do pipeline de dados?_**

**_Resposta:_** Coletar, armazenar, processar e analisar, visualizar.

## Soluções de Análise de Dados na AWS

A Amazon Web Services (AWS) oferece uma ampla gama de serviços e soluções para análise de dados, permitindo que as organizações processem, armazenem, analisem e visualizem grandes volumes de dados de maneira eficiente e escalável. Abaixo, vou destacar algumas das principais soluções de análise de dados na AWS:

<div align="center">

![Extração Data Lakes](<Images Sprint6/Extração Data Lakes.png>)

**Fonte: [Amazon AWS](https://aws.amazon.com/pt/blogs/aws-brasil/como-extrair-valor-dos-seus-dados-com-data-lakes-e-analises-na-aws/)**

</div>

+ **Amazon Redshift:** Um data warehouse totalmente gerenciado que permite armazenar e analisar grandes volumes de dados usando SQL. É altamente escalável e integrado com outras ferramentas de análise, como o Amazon QuickSight.

+ **Amazon Athena:** Um serviço de análise interativa que permite consultar dados diretamente no Amazon S3 usando SQL padrão, sem a necessidade de carregar dados para um banco de dados.

+ **Amazon EMR (Elastic MapReduce):** Uma estrutura de computação em nuvem que permite processar e analisar grandes volumes de dados usando estruturas de processamento distribuído, como Hadoop e Spark.

+ **Amazon Quicksight:** Uma ferramenta de visualização de dados totalmente gerenciada que permite criar painéis interativos e relatórios com facilidade. É integrada com muitos outros serviços da AWS.

+ **AWS Glue:** Um serviço de ETL (Extração, Transformação e Carga) totalmente gerenciado que simplifica o processo de preparação de dados para análise, automatizando tarefas de integração e transformação de dados.

+ **Amazon Kinesis:** Uma plataforma para coletar, processar e analisar dados em tempo real, como streaming de vídeo, logs e dados de sensores.

+ **AWS Data Pipeline:** Um serviço que permite orquestrar e automatizar fluxos de trabalho de dados, facilitando a movimentação de dados entre diferentes serviços da AWS e fontes externas.

+ **AWS Data Lake:** Um conceito que envolve a criação de um repositório centralizado de dados em bruto, geralmente usando o Amazon S3, para armazenar todos os tipos de dados antes da análise. Isso permite flexibilidade na análise posterior.

+ **AWS Glue DataBrew:** Uma ferramenta de preparação de dados visual que ajuda a limpar, normalizar e transformar dados de maneira fácil e eficiente.

+ **Amazon SageMaker:** Uma plataforma de aprendizado de máquina totalmente gerenciada que permite criar, treinar e implantar modelos de aprendizado de máquina com facilidade para análise preditiva.

+ **Amazon Timestream:** Um banco de dados de séries temporais totalmente gerenciado que é otimizado para armazenar e consultar dados de séries temporais, como métricas de IoT e registros de aplicativos.

+ **Amazon Managed Grafana:** Um serviço que permite criar e implantar painéis de observabilidade com o Grafana sem a necessidade de gerenciar a infraestrutura subjacente.

Essas são apenas algumas das muitas soluções de análise de dados disponíveis na AWS. A escolha da solução dependerá das necessidades específicas da sua organização, do tipo de dados que você está lidando e dos seus objetivos de análise. A AWS oferece flexibilidade para construir pipelines de dados e arquiteturas de análise personalizadas com base nas suas necessidades.

### Atividade 1

**_Qual é o nome da abordagem de arquitetura que permite às empresas armazenar todos os dados (estruturados, não estruturados e semiestruturados) em um único repositório?_**

**_Resposta:_** Data Lake.

### Atividade 2

**_Qual é o nome do serviço de data warehouse da AWS?_**

**_Resposta:_** Amazon RedShift.

### Atividade 3

**_Qual é o nome do serviço de visualização de dados da AWS?_**

**_Resposta:_** Amazon QuickSight.

### Atividade 4

**_Qual serviço da Nuvem AWS você deve usar para modernizar data warehouses herdados?_**

**_Resposta:_** Amazon Redshift.

### Atividade 5

**_Qual produto da AWS você usaria para dados em transmissão?_**

**_Resposta:_** Amazon Kinesis.

### Atividade 6

**_Quais dessas soluções podem ser aplicadas usando algoritmos para encontrar padrões nos dados depois que eles são protegidos em um data lake?_**

**_Resposta:_** Governança de dados.

## 3. Conversas de negócios

As conversas de negócios relacionadas à Amazon Web Services (AWS) geralmente envolvem discussões sobre como a AWS pode atender às necessidades de uma organização em termos de computação em nuvem e serviços relacionados. Aqui estão alguns tipos comuns de conversas de negócios relacionadas à AWS:

+ **Planejamento de Migração para a Nuvem:** Muitas organizações consideram mover suas cargas de trabalho locais para a nuvem da AWS. As conversas de negócios aqui se concentram em estratégias de migração, custos associados, segurança, conformidade e benefícios da mudança para a nuvem.

+ **Arquitetura de Nuvem:** Empresas discutem como projetar suas aplicações e infraestrutura na AWS para garantir escalabilidade, desempenho e alta disponibilidade. Isso inclui escolher serviços adequados, como servidores EC2, bancos de dados gerenciados, balanceadores de carga, etc.

+ **Análise de Custos:** Conversas relacionadas a otimização de custos, identificando maneiras de reduzir despesas ao utilizar estrategicamente os recursos da AWS, como instâncias reservadas, orçamentos e relatórios de uso.

+ **Segurança e Conformidade:** Discussões sobre as práticas de segurança da AWS e como atender aos requisitos de conformidade da indústria, como GDPR, HIPAA, etc.

+ **Público-Alvo:** Esta seção pode explicar quem é o público-alvo do módulo de treinamento. Pode ser direcionado a profissionais de vendas, gerentes de contas, consultores de soluções, arquitetos de soluções ou qualquer pessoa envolvida em vendas, consultoria ou parcerias relacionadas à AWS.

+ **Perguntas de Descoberta:** Essa seção abordaria as perguntas que os profissionais envolvidos nas conversas de negócios relacionadas à AWS devem fazer para entender as necessidades e desafios do cliente. Perguntas de descoberta são fundamentais para personalizar as soluções da AWS de acordo com os requisitos específicos do cliente. Exemplos de perguntas de descoberta podem incluir:

    + Quais são os desafios de negócios que sua organização está enfrentando?
    + Qual é a infraestrutura de TI atual da sua empresa?
    + Quais são seus objetivos de negócios de curto e longo prazo?
    + Você tem requisitos de conformidade específicos?
    + Como você lida com a escalabilidade e disponibilidade de recursos de TI?

Alguns exemplos de objeções comuns podem incluir preocupações com segurança, custos, complexidade ou resistência à migração para a nuvem. O treinamento pode incluir estratégias para superar essas objeções, como a apresentação de estudos de caso, demonstrações de segurança robusta na AWS e análises de custo-benefício.

# Exercícios - Laboratórios AWS

## 2. Lab AWS S3

**Etapa 1: Criar um bucket.**

As instruções a seguir fornecem uma visão geral de como criar seus buckets para hospedagem de conteúdo estático.

<div align="center">

![Criar bucket](<Images Sprint6/Criar bucket.png>)

![Criar bucket2](<Images Sprint6/Criar bucket2.png>)

</div>

**Etapa 2: Habilitar hospedagem de site estático.**

Depois de criar um bucket, você pode habilitar a hospedagem de site estático nele.

<div align="center">

![Hospedagem](<Images Sprint6/Hospedagem.png>)

![Hospedagem2](<Images Sprint6/Hospedagem2.png>)
</div>

**Etapa 3: editar as configurações do Bloqueio de acesso público.**

Por padrão, o Amazon S3 bloqueia o acesso público à sua conta e aos seus buckets. Se quiser usar um bucket para hospedar um site estático, use estas etapas para editar as configurações de bloqueio de acesso público.

<div align="center">

![Acesso público](<Images Sprint6/Acesso público.png>)

</div>

**Etapa 4: Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível.**

Depois de editar as configurações do bloqueio de acesso público do S3, é possível adicionar uma política de bucket para conceder acesso público de somente leitura ao bucket. Ao conceder um acesso público de leitura, qualquer pessoa na Internet poderá acessar seu bucket.

<div align="center">

![Política bucket](<Images Sprint6/Política bucket.png>)

</div>

**Etapa 5: Configurar um documento de índice.**

Quando você habilita a hospedagem de sites estáticos para seu bucket, deve informar o nome do documento de índice (por exemplo, index.html). Naturalmente, o arquivo informado deverá estar presente no bucket para que a configuração tenha efeito.

<div align="center">

![Documento index](<Images Sprint6/Documento index.png>)

</div>

**Etapa 6: configurar documento de erros.**

Depois de habilitar a hospedagem de sites estáticos para seu bucket, faça upload para o bucket de um arquivo HTML para notificação de erros.

<div align="center">

![Todos documentos](<Images Sprint6/Todos documentos.png>)

</div>

**Etapa 7: testar o endpoint do site.**

Depois de configurar a hospedagem de site estático para seu bucket, você pode testá-lo em seu navegador.

<div align="center">

![Endpoint](<Images Sprint6/Endpoint.png>)

&nbsp;

</div>

## 3. Lab AWS Athena

**Etapa 1: Configurar Athena.**

<div align="center">

![Pasta queries](<Images Sprint6/Pasta queries.png>)

![Localizando query](<Images Sprint6/Localização Query.png>)

</div>

**Etapa 2: Criar um banco de dados.**

<div align="center">

![Create meubanco](<Images Sprint6/Create meubanco.png>)

</div>

**Etapa 3: Criar uma tabela.**

Agora que você tem um banco de dados, pode criar uma tabela do Athena para ele.

<div align="center">

![Criar tabela](<Images Sprint6/Criar tabela.png>)

![Criar tabela 2](<Images Sprint6/Criar tabela2.png>)

![Teste query](<Images Sprint6/Teste query.png>)

</div>

```sql
select nome 
from nomedobanco.nomedatabela 
where ano = 1999 
order by total 
limit 15;

# Output

#	nome
1	Adaiah
2	Aanya
3	Abinaya
4	Abriona
5	Achsah
6	Aalijah
7	Aania
8	Aaren
9	Abbigaile
10	Abla
11	Abrianne
12	Aby
13	Accalia
14	Adalee
15	Abish
```

**Desafio: Crie uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.**

<div align="center">

![Desafio](<Images Sprint6/Desafio.png>)

![Desafio2](<Images Sprint6/Desafio2.png>)
</div>

```sql
WITH DadosPorDecada AS (
  SELECT
    nome,
    ano,
    CASE
      WHEN ano BETWEEN 1950 AND 1959 THEN '1950s'
      WHEN ano BETWEEN 1960 AND 1969 THEN '1960s'
      WHEN ano BETWEEN 1970 AND 1979 THEN '1970s'
      WHEN ano BETWEEN 1980 AND 1989 THEN '1980s'
      WHEN ano BETWEEN 1990 AND 1999 THEN '1990s'
      WHEN ano BETWEEN 2000 AND 2009 THEN '2000s'
      WHEN ano BETWEEN 2010 AND 2019 THEN '2010s'
      WHEN ano BETWEEN 2020 AND 2029 THEN '2020s'
      ELSE 'Outras'
    END AS decada,
    total
  FROM meubanco.nomes
)
, DecadasTop3 AS (
  SELECT
    decada,
    nome,
    SUM(total) AS total_por_nome,
    ROW_NUMBER() OVER (PARTITION BY decada ORDER BY SUM(total) DESC) AS rank
  FROM DadosPorDecada
  GROUP BY decada, nome
)
SELECT
  decada,
  nome,
  total_por_nome
FROM DecadasTop3
WHERE rank <= 3
ORDER BY decada, total_por_nome DESC;
```

&nbsp;

## 4. Lab AWS Lambda

**Etapa 1: Criar a função do Lambda.**

<div align="center">

![Criar função](<Images Sprint6/Criar função.png>)

</div>

**Etapa 2: Construir o código.**

<div align="center">

![Origem do código](<Images Sprint6/Origem do código.png>)

![Origem do código 2](<Images Sprint6/Origem do código2.png>)

</div>

**Etapa3: Criar uma Layer.**

<div align="center">

![Dockerfile](<Images Sprint6/Dockerfile.png>)

![Layer 1](<Images Sprint6/Layer1.png>)

![Layer 2](<Images Sprint6/Layer2.png>)

![Layer 3](<Images Sprint6/Layer3.png>)

![Criar camada](<Images Sprint6/Criar camada.png>)

</div>

**Etapa 4: Utilizando a Layer.**

<div align="center">

![Configurações camada](<Images Sprint6/Configurações camada.png>)

![Response código](<Images Sprint6/Response código.png>)

</div>

&nbsp;

# 📝 Certificação

+ Certificação da conclução do curso Data Analytics Fundamentals de 4hrs.

<div align="center">

![Data Analytics Fundamentals](<Certification PNG/Data Analytics Fundamentals.png>)

</div>

+ Certificação da conclução do curso Data Analytics on AWS Business de 4hrs.

<div align="center">

![Data Analytics on AWS Business](<Certification PNG/Data Analytics on AWS Business.png>)

</div>

+ Certificação da conclução do curso Introduction to Amazon Kinesis Streams de 15m.

<div align="center">

![Amazon Kinesis Streams](<Certification PNG/Amazon Kinesis Streams.png>)

</div>

+ Certificação da conclução do curso Introduction to Amazon Kinesis Analytics de 7m.

<div align="center">

![Amazon Kinesis Analytics](<Certification PNG/Amazon Kinesis Analytics.png>)

</div>

+ Certificação da conclução do curso Introduction to Amazon Elastic MapReduce de 15m.

<div align="center">

![Amazon Elastic MapReduce](<Certification PNG/Amazon Elastic MapReduce.png>)

</div>

+ Certificação da conclução do curso Introduction to Amazon Athena de 10m.

<div align="center">

![Amazon Athena](<Certification PNG/Amazon Athena.png>)

</div>

+ Certificação da conclução do curso Introduction to Amazon Quicksight de 18m.

<div align="center">

![Amazon Quicksight](<Certification PNG/Amazon Quicksight.png>)

</div>

+ Certificação da conclução do curso Introduction to AWS IoT Analytics de 30m.

<div align="center">

![AWS IoT Analytics](<Certification PNG/AWS IoT Analytics.png>)

</div>

+ Certificação da conclução do curso Getting Started with Amazon Redshift de 1hr.

<div align="center">

![Getting Started with Amazon Redshift](<Certification PNG/Getting Started with Amazon Redshift.png>)

</div>

+ Certificação da conclução do curso Deep Dive into Concepts and Tools for Analyzing Streaming Data de 35m.

<div align="center">

![Deep Dive into Concepts and Tools for Analyzing Streaming Data](<Certification PNG/Deep Dive into Concepts and Tools for Analyzing Streaming Data.png>)

</div>

+ Certificação da conclução do curso Best Practices for Data Warehousing with Amazon Redshift de 1hr30m.

<div align="center">

![Best Practices for Data Warehousing with Amazon Redshift](<Certification PNG/Best Practices for Data Warehousing with Amazon Redshift.png>)

</div>

+ Certificação da conclução do curso Serverless Analytics de 25m.

<div align="center">

![Serverless Analytics](<Certification PNG/Serverless Analytics.png>)

</div>

+ Certificação da conclução do curso Why Analytics for Games de 25m.

<div align="center">

![Why Analytics for Games](<Certification PNG/Why Analytics for Games.png>)

</div>

+ Certificação da conclução do curso Data & Analytics - PB - AWS 6/10.

<div align="center">

![Data & Analytics - PB - AWS 6/10](<Certification PNG/Data & Analytics - PB - AWS 6-10.jpg>)

</div>

---