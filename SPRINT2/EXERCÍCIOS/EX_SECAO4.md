# Seção 4 - Exercícios

_**EX8.**
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd._

**_Resposta:_**

```sql
SELECT
	tbvendedor.cdvdd, tbvendedor.nmvdd
FROM
	tbvendedor
INNER JOIN
	tbvendas ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE
	tbvendas.status = 'Concluído'
GROUP BY
	tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY
	COUNT(tbvendas.cdven) DESC
LIMIT 1
```

&nbsp;

_**EX9.**
Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro._

**_Resposta:_**

```sql
SELECT 
    cdpro, nmpro
FROM 
    tbvendas
WHERE 
    dtven BETWEEN '2014-02-03' AND '2018-02-02' AND status = 'Concluído'
GROUP BY 
    qtd
order by 
    qtd  DESC
limit 1
```

&nbsp;

_**EX10.**
A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor._

_Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído._

_As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal._

**_Resposta:_**

```sql
SELECT
    tbvendedor.nmvdd AS vendedor,
    SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas,
    ROUND(
        (SUM
            (ROUND(tbvendas.qtd, 2) * ROUND(tbvendas.vrunt, 2) * ROUND(tbvendedor.perccomissao, 2)
            ) 
        / 100)
    , 2) AS comissao
FROM
    tbvendedor
INNER JOIN
    tbvendas ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE
    tbvendas.status = 'Concluído'
GROUP BY
    tbvendedor.nmvdd, tbvendedor.perccomissao
ORDER BY
    comissao DESC;
```

_**EX11.**
Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente._

**_Resposta:_**

```sql
SELECT
    tbvendas.cdcli,
    tbvendas.nmcli,
    SUM(tbvendas.qtd * tbvendas.vrunt) AS gasto
FROM
    tbvendas
WHERE
    tbvendas.status = 'Concluído'
GROUP BY
    tbvendas.cdcli, tbvendas.nmcli
ORDER BY
    gasto DESC
LIMIT 1;
```

_**EX12.**
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.Observação: Apenas vendas com status concluído._

**_Resposta:_**

```sql
SELECT
    tbdependente.cddep,
    tbdependente.nmdep,
    tbdependente.dtnasc,
    SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas
FROM
    tbvendedor
LEFT JOIN
    tbdependente ON tbvendedor.cdvdd = tbdependente.cdvdd
LEFT JOIN
    tbvendas ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE
    tbvendas.status = 'Concluído'
GROUP BY
    tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc
HAVING
    valor_total_vendas > 0
ORDER BY
    valor_total_vendas
LIMIT 1;
```

&nbsp;

_**EX13.**
Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas._

**_Resposta:_**

```sql
SELECT
    tbestoqueproduto.cdpro,
    tbvendas.nmcanalvendas,
    tbvendas.nmpro,
    SUM(tbvendas.qtd) AS quantidade_vendas
FROM
    tbvendas
JOIN
    tbestoqueproduto ON tbvendas.cdpro = tbestoqueproduto.cdpro
WHERE
    (tbvendas.nmcanalvendas = 'Ecommerce' OR tbvendas.nmcanalvendas = 'Matriz') AND
    tbvendas.status = 'Concluído'
GROUP BY
    tbestoqueproduto.cdpro, tbvendas.nmcanalvendas
ORDER BY
    quantidade_vendas ASC
LIMIT 10;
```

&nbsp;

_**EX14.**
Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente. Observação: Apenas vendas com status concluído._

**_Resposta:_**

```sql
SELECT
    tbvendas.estado,
    ROUND(AVG(tbvendas.qtd * tbvendas.vrunt), 2) AS gastomedio
FROM
    tbvendas
WHERE
    tbvendas.status = 'Concluído'
GROUP BY
    tbvendas.estado
ORDER BY
    gastomedio DESC;
```

&nbsp;

_**EX15.**
Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente._

**_Resposta:_**

```sql
SELECT
    tbvendas.cdven
FROM
    tbvendas
WHERE
    tbvendas.deletado = 1
ORDER BY
    tbvendas.cdven ASC;
```

&nbsp;

_**EX16.**
Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º). Obs: Somente vendas concluídas._

**_Resposta:_**

```sql
SELECT
    tbvendas.estado,
    tbvendas.nmpro,
    ROUND(AVG(tbvendas.qtd), 4) AS quantidade_media
FROM
    tbvendas
JOIN
    tbestoqueproduto ON tbvendas.cdpro = tbestoqueproduto.cdpro
WHERE
    tbvendas.status = 'Concluído'
GROUP BY
    tbvendas.estado, tbvendas.nmpro
ORDER BY
    tbvendas.estado, tbvendas.nmpro;
```

---

&nbsp;

<div align="center">

![Loja Sqlite](<../Images Sprint2/Caso de Estudo - Loja.png>)

**Fonte: Udemy**

---