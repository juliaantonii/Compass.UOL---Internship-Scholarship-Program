# 🔖 **SUMÁRIO**

Nesta página encontra-se 4 Tópicos Principais, são estes:

+ **[TAREFA 1: Desafio Parte 4 - Consumo e Apresentação dos Dados](#1-tarefa-1-desafio-parte-4---consumo-e-apresentação-dos-dados)**
+ **[Agradecimentos](#agradecimentos)**
+ **[Certificação](#📝-certificação).**

---

&nbsp;

# 1. Tarefa 1: Desafio Parte 4 - Consumo e Apresentação dos Dados

**Perguntas dessa tarefa:** Desenvolva um dashboard utilizando AWS QuickSight conforme instruções da tarefa.

Com os dados já refinados da Sprint 9, onde encontramos a tab_normalizada e suas sub-tabelas, utilizamos do AWS Athena para realizar algumas consulta que seram fundamentais para a análise dos dados. Tendo em mente que o tema a ser análisado é: Observação do Desempenho dos Subgêneros do Terror.

Foram selecionadas algumas palavras-chaves que mais aparecem quando relacionamos o tema Terror, e então desenvolve-se este código SQL, responsável por criar uma tabela chamada **frequencia_de_keyword** e a preenche com contagens de palavras-chave específicas relacionadas ao gênero de horror. Utilizando como base de analise uma tabela chamada **tab_normalizada** para contar a ocorrência de diferentes palavras-chave em filmes de horror.

```python
CREATE TABLE frequencia_de_keyword AS
SELECT 'murder' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%murder%'
UNION
SELECT 'supernatural' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%supernatural%'
UNION
SELECT 'revenge' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%revenge%'
UNION
SELECT 'police' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%police%'
UNION
SELECT 'kidnapping' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%kidnapping%'
UNION
SELECT 'demonic possession' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%demonic possession%'
UNION
SELECT 'slasher' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%slasher%'
UNION
SELECT 'psychological thriller' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%psychological thriller%'
UNION
SELECT 'haunted house' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%haunted house%'
UNION
SELECT 'persecution' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%persecution%'
UNION
SELECT 'conspiracy' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%conspiracy%'
UNION
SELECT 'thriller' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%thriller%'
UNION
SELECT 'gore' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%gore%'
UNION
SELECT 'assassin' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%assassin%'
UNION
SELECT 'survival' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%survival%'
UNION
SELECT 'alien invasion' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%alien invasion%'
UNION
SELECT 'alien' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%alien%'
UNION
SELECT 'assassination' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%assassination%'
UNION
SELECT 'extraterrestrial' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%extraterrestrial%'
UNION
SELECT 'paranormal' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%paranormal%'
UNION
SELECT 'possession' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%possession%'
UNION
SELECT 'trash' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%trash%'
UNION
SELECT 'disturbing' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%disturbing%'
UNION
SELECT 'suspense' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%suspense%'
UNION
SELECT 'creep' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%creep%'
UNION
SELECT 'sadism' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%sadism%'
UNION
SELECT 'monster' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%monster%'
UNION
SELECT 'torture' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%torture%'
UNION
SELECT 'extreme violence' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%extreme violence%'
UNION
SELECT 'creature' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%creature%'
UNION
SELECT 'demon' AS palavra, COUNT(*) AS quantidade
FROM tab_normalizada
WHERE genero LIKE '%Horror%' AND palavrachave LIKE '%demon%';
```

Com isso pronto, ao selecionarmos todas as colunas da tabela **frequencia_de_keywords**, obtemos a seguinte resposta:

<div align="center">

![Frequência de Keywords](<Images Sprint10/frequencia de keywords.png>)

</div>

Com essa tabela já criada, iremos realizar outra consulta no AWS Athena, cujo objetivo é criar a tabela **TopHorrorKeywordsPerDecade**, o script cria essa tabela que resume as principais palavras-chave de horror por década, classificadas por ocorrências. Cada palavra-chave também é categorizada em tipos específicos de terror, como "TERROR SLASHER", "TERROR SOBRENATURAL", "TERROR GORE", "TERROR THRILLER", "TERROR TRASH" ou "Other". Essa categorização é baseada nas palavras-chave específicas associadas a cada tipo de terror.

```python
CREATE TABLE IF NOT EXISTS TopHorrorKeywordsPerDecade AS
WITH RankedKeywords AS (
  SELECT
    CONCAT(SUBSTRING(anolancamento, 1, 3), '0s') AS decade,
    keyword,
    COUNT(*) AS keyword_count,
    ROW_NUMBER() OVER (PARTITION BY CONCAT(SUBSTRING(anolancamento, 1, 3), '0s') ORDER BY COUNT(*) DESC) AS keyword_rank,
    CASE
      WHEN keyword IN ('murder', 'revenge', 'police', 'kidnapping', 'assassin', 'assassination', 'slasher') THEN 'TERROR SLASHER'
      WHEN keyword IN ('supernatural', 'demonic possession', 'paranormal', 'possession', 'demon') THEN 'TERROR SOBRENATURAL'
      WHEN keyword IN ('gore', 'haunted house', 'disturbing', 'creep', 'sadism', 'torture', 'extreme violence') THEN 'TERROR GORE'
      WHEN keyword IN ('survival', 'thriller', 'conspiracy', 'suspense') THEN 'TERROR THRILLER'
      WHEN keyword IN ('alien', 'alien invasion', 'extraterrestrial', 'trash', 'monster', 'creature') THEN 'TERROR TRASH'
      ELSE 'Other'
    END AS keyword_category
  FROM (
    SELECT
      anolancamento,
      keyword
    FROM
      tab_normalizada
    CROSS JOIN
      (VALUES
        ('murder'), ('revenge'), ('police'), ('kidnapping'), ('assassin'),
        ('assassination'), ('slasher'), ('supernatural'), ('demonic possession'),
        ('paranormal'), ('possession'), ('demon'), ('gore'), ('haunted house'),
        ('disturbing'), ('creep'), ('sadism'), ('torture'), ('extreme violence'),
        ('survival'), ('thriller'), ('conspiracy'), ('suspense'), ('alien'),
        ('alien invasion'), ('extraterrestrial'), ('trash'), ('monster'), ('creature')
      ) AS keywords (keyword)
    WHERE
      LOWER(tab_normalizada.palavrachave) LIKE '%' || LOWER(keywords.keyword) || '%'
      AND LOWER(tab_normalizada.genero) = 'horror'
  ) AS keyword_data
  GROUP BY
    CONCAT(SUBSTRING(anolancamento, 1, 3), '0s'),
    keyword
)
SELECT
  decade,
  keyword,
  keyword_count,
  keyword_rank,
  keyword_category
FROM
  RankedKeywords
WHERE
  keyword_rank <= 3
ORDER BY
  decade, keyword_rank;

```

Ao seleciona-lá obtemos a seguinte resposta:

<div align="center">

![Top Horror Keywords Per Decade](<Images Sprint10/top horror keywords per decade.png>)

</div>

Com isso, iremos finalizar nossas consultas classificando os subgêneros do terror com as palavras-chaves, este script SQL cria uma tabela que contém informações específicas sobre filmes de horror associados a certas palavras-chave, os enquadrando de acordo com seu tema. 

+ GORE HORROR :

```python
CREATE TABLE gore_horror AS
SELECT
    titulo,
    popularidadefilme,
    orcamentofilme,
    receitafilme,
    (receitafilme - orcamentofilme) AS lucro
FROM (
    SELECT
        tn.tituloprincipal AS titulo,
        MAX(tn.popularidadefilme) AS popularidadefilme,
        MAX(tn.orcamentofilme) AS orcamentofilme,
        MAX(tn.receitafilme) AS receitafilme
    FROM
        tab_normalizada tn
    WHERE
        tn.genero LIKE '%Horror%'
        AND (
            tn.palavrachave LIKE '%gore%'
            OR tn.palavrachave LIKE '%haunted house%'
            OR tn.palavrachave LIKE '%disturbing%'
            OR tn.palavrachave LIKE '%creep%'
            OR tn.palavrachave LIKE '%sadism%'
            OR tn.palavrachave LIKE '%torture%'
            OR tn.palavrachave LIKE '%extreme violence%'
        )
        AND TRY_CAST(tn.anolancamento AS INTEGER) > 2018
        AND tn.orcamentofilme > 0  -- Considera apenas filmes com orçamento maior que 0
        AND tn.receitafilme > 0    -- Considera apenas filmes com receita maior que 0
    GROUP BY
        tn.tituloprincipal
) AS Subquery;
```

+ THRILLER HORROR : 

```python
CREATE TABLE thriller_horror AS
SELECT
    titulo,
    popularidadefilme,
    orcamentofilme,
    receitafilme,
    (receitafilme - orcamentofilme) AS lucro
FROM (
    SELECT
        tn.tituloprincipal AS titulo,
        MAX(tn.popularidadefilme) AS popularidadefilme,
        MAX(tn.orcamentofilme) AS orcamentofilme,
        MAX(tn.receitafilme) AS receitafilme
    FROM
        tab_normalizada tn
    WHERE
        tn.genero LIKE '%Horror%'
        AND (
            tn.palavrachave LIKE '%survival%'
            OR tn.palavrachave LIKE '%thriller%'
            OR tn.palavrachave LIKE '%conspiracy%'
            OR tn.palavrachave LIKE '%suspense%'
        )
        AND TRY_CAST(tn.anolancamento AS INTEGER) > 2018
        AND tn.orcamentofilme > 0  -- Considera apenas filmes com orçamento maior que 0
        AND tn.receitafilme > 0    -- Considera apenas filmes com receita maior que 0
    GROUP BY
        tn.tituloprincipal
) AS Subquery;
```

+ TRASH HORROR :

```python
CREATE TABLE trash_horror AS
SELECT
    titulo,
    popularidadefilme,
    orcamentofilme,
    receitafilme,
    (receitafilme - orcamentofilme) AS lucro
FROM (
    SELECT
        tn.tituloprincipal AS titulo,
        MAX(tn.popularidadefilme) AS popularidadefilme,
        MAX(tn.orcamentofilme) AS orcamentofilme,
        MAX(tn.receitafilme) AS receitafilme
    FROM
        tab_normalizada tn
    WHERE
        tn.genero LIKE '%Horror%'
        AND (
            tn.palavrachave LIKE '%alien%'
            OR tn.palavrachave LIKE '%alien invasion%'
            OR tn.palavrachave LIKE '%extraterrestrial%'
            OR tn.palavrachave LIKE '%trash%'
            OR tn.palavrachave LIKE '%monster%'
            OR tn.palavrachave LIKE '%creature%'
        )
        AND TRY_CAST(tn.anolancamento AS INTEGER) > 2018
        AND tn.orcamentofilme > 0  -- Considera apenas filmes com orçamento maior que 0
        AND tn.receitafilme > 0    -- Considera apenas filmes com receita maior que 0
    GROUP BY
        tn.tituloprincipal
) AS Subquery;
```

+ SOBRENATURAL HORROR :

```python
CREATE TABLE sobrenatural_horror AS
SELECT
    titulo,
    popularidadefilme,
    orcamentofilme,
    receitafilme,
    (receitafilme - orcamentofilme) AS lucro
FROM (
    SELECT
        tn.tituloprincipal AS titulo,
        MAX(tn.popularidadefilme) AS popularidadefilme,
        MAX(tn.orcamentofilme) AS orcamentofilme,
        MAX(tn.receitafilme) AS receitafilme
    FROM
        tab_normalizada tn
    WHERE
        tn.genero LIKE '%Horror%'
        AND (
            tn.palavrachave LIKE '%supernatural%'
            OR tn.palavrachave LIKE '%demonic possession%'
            OR tn.palavrachave LIKE '%paranormal%'
            OR tn.palavrachave LIKE '%possession%'
            OR tn.palavrachave LIKE '%demon%'
        )
        AND TRY_CAST(tn.anolancamento AS INTEGER) > 2018
        AND tn.orcamentofilme > 0  -- Considera apenas filmes com orçamento maior que 0
        AND tn.receitafilme > 0    -- Considera apenas filmes com receita maior que 0
    GROUP BY
        tn.tituloprincipal
) AS Subquery;
```

+ SLASHER HORROR :

```python
CREATE TABLE slasher_horror AS
SELECT
    titulo,
    popularidadefilme,
    orcamentofilme,
    receitafilme,
    (receitafilme - orcamentofilme) AS lucro
FROM (
    SELECT
        tn.tituloprincipal AS titulo,
        MAX(tn.popularidadefilme) AS popularidadefilme,
        MAX(tn.orcamentofilme) AS orcamentofilme,
        MAX(tn.receitafilme) AS receitafilme
    FROM
        tab_normalizada tn
    WHERE
        tn.genero LIKE '%Horror%'
        AND (
            tn.palavrachave LIKE '%murder%'
            OR tn.palavrachave LIKE '%revenge%'
            OR tn.palavrachave LIKE '%police%'
            OR tn.palavrachave LIKE '%kidnapping%'
            OR tn.palavrachave LIKE '%assassin%'
            OR tn.palavrachave LIKE '%assassination%'
            OR tn.palavrachave LIKE '%slasher%'
        )
        AND TRY_CAST(tn.anolancamento AS INTEGER) > 2018
        AND tn.orcamentofilme > 0  -- Considera apenas filmes com orçamento maior que 0
        AND tn.receitafilme > 0    -- Considera apenas filmes com receita maior que 0
    GROUP BY
        tn.tituloprincipal
) AS Subquery;
```

 Destaca-se estas consultas essenciais realizadas em nossa base de dados de filmes de terror, visando a extração de insights valiosos. As consultas incluem a frequência de palavras-chave, identificação das principais palavras-chave por década e análise específica de filmes associados a termos como gore e haunted house. Essas análises fornecerão a base para a criação de um dashboard interativo, possibilitando uma compreensão visual e intuitiva das tendências do mercado cinematográfico de terror. 

**Dashboard de Análise de Filmes de Terror:**

<div align="center">

![DashBoard](<Images Sprint10/DashBoard.jpg>)

</div>

Nosso dashboard foi cuidadosamente projetado para oferecer insights visuais sobre o fascinante mundo dos filmes de terror. Abaixo, apresentamos os principais gráficos e análises incorporados ao dashboard:

+ **Nuvem de Palavras-Chave (KEYWORD):**

Este gráfico proporciona uma representação visual das palavras-chave mais frequentes associadas aos filmes de terror. A dimensão das palavras na nuvem indica a sua relevância.

+ **Popularidade dos Subgêneros do Terror Conforme as Décadas:**

Oferecendo uma visão temporal, este gráfico destaca a popularidade dos subgêneros de terror ao longo das décadas. Insights valiosos sobre as mudanças de preferência da audiência podem ser extraídos dessa análise.

+ **Análise Financeira do Slasher Horror:**

Este gráfico fornece uma análise financeira específica para filmes do subgênero "Slasher". Inclui informações sobre orçamento, receita e lucro ao longo do tempo.

+ **Análise Financeira do Gore Horror:**

Similar à análise do "Slasher", este gráfico oferece uma perspectiva financeira específica para filmes de terror associados ao subgênero "Gore".

+ **Análise Financeira do Sobrenatural Horror:**

Destaca as métricas financeiras (orçamento, receita, lucro) para filmes de terror do subgênero "Sobrenatural".

+ **Análise Financeira do Thriller Horror:**

Focado no subgênero "Thriller", este gráfico proporciona insights sobre o desempenho financeiro desses filmes ao longo do tempo.

+ **Análise Financeira do Trash Horror:**

O gráfico dedicado ao subgênero "Trash" oferece informações sobre orçamento, receita e lucro, permitindo uma análise detalhada desse segmento.

Esses gráficos interativos no dashboard são ferramentas poderosas para a tomada de decisões informadas. Ao visualizar de forma clara e intuitiva as tendências, popularidade e desempenho financeiro dos diferentes subgêneros, nossa equipe terá a capacidade de otimizar estratégias e aprimorar a produção de filmes de terror de acordo com as preferências do público.

Com base na análise do dashboard, observamos que os filmes de terror do subgênero "Slasher" apresentam características notáveis, destacando-se como os mais populares e lucrativos para as empresas cinematográficas. Isso pode ser evidenciado pelos seguintes pontos:

**Popularidade Significativa:**

Através do gráfico de "Popularidade dos Subgêneros do Terror Conforme as Décadas", notamos que os filmes "Slasher" consistentemente mantêm uma alta popularidade ao longo do tempo. Essa constância sugere uma preferência duradoura do público por esse subgênero específico.

**Análise Financeira Positiva:**

O gráfico de "Análise Financeira do Slasher Horror" destaca que os filmes "Slasher" não apenas são populares, mas também se destacam financeiramente. A análise financeira revela que esses filmes tendem a gerar lucros significativos em relação aos seus orçamentos.

**Comportamento do Público e Lucratividade:**

A correlação entre a alta popularidade e o desempenho financeiro positivo sugere que os filmes de terror "Slasher" conseguem atrair uma grande audiência, resultando em receitas substanciais para as empresas de produção cinematográfica.

Esses insights podem ser fundamentais para orientar estratégias futuras na indústria cinematográfica de terror. Investir em filmes do subgênero "Slasher" pode ser uma abordagem sólida, considerando a combinação de popularidade e lucratividade que eles oferecem. No entanto, é crucial continuar monitorando as tendências do mercado e as preferências do público para garantir decisões informadas e sustentáveis a longo prazo.

&nbsp;

# Agradecimentos

Gostaria de agradeçer a **Compass.UOL** pela enriquecedora oportunidade de estágio. A experiência foi transformadora, proporcionando aprendizado e crescimento pessoal, acadêmico e profissional. 

Descobri um grande interesse nesta área profissional, e sou grata pelo apoio do meu **SQUAD #6** e pela cultura inspiradora da empresa.

---

&nbsp;

# 📝 Certificação

<div align="center">

![Certificação 1](<Images Sprint10/Certificação1.png>)

![Certificação 2](<Images Sprint10/Certificação2.png>)

![Certificação 3](<Images Sprint10/Certificação3.png>)

![Certificação 4](<Images Sprint10/Certificação4.png>)

![Certificação 5](<Images Sprint10/Certificação5.png>)

![Certificação 6 - 1](<Images Sprint10/Certificação6-1.png>)

![Certificação 6 - 2](<Images Sprint10/Certificação6-2.png>)

![Certificação 7](<Images Sprint10/Certificação7.png>)

![Certificação 8 - 9](<Images Sprint10/Certificação8-9.png>)

![Certificação 10](<Images Sprint10/Certificação10.png>)

</div>

---