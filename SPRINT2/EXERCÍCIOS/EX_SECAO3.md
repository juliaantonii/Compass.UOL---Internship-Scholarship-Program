# Seção 3 - Exercícios

_**EX1.**
Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma._

**_Resposta:_**

```sql
SELECT *
FROM 
    livro
WHERE 
    publicacao > '2014-12-31'
ORDER BY 
    cod ASC;
```

&nbsp;

_**EX2.**
Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor._

**_Resposta:_**

```sql
SELECT 
    titulo, valor
FROM 
    livro
ORDER BY 
    valor DESC
LIMIT 10;
```

&nbsp;

_**EX3.**
Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente._

**_Resposta:_**

```sql
SELECT
	count(livro.cod) AS quantidade,
	editora.nome,
	endereco.estado,
	endereco.cidade
FROM
	livro
LEFT JOIN
	editora ON livro.editora = editora.codeditora
LEFT JOIN
	endereco ON editora.endereco = endereco.codendereco
GROUP BY
	editora.nome, endereco.estado, endereco.cidade
ORDER BY
	quantidade DESC
LIMIT 5;
```

&nbsp;

_**EX4.**
Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria)._

**_Resposta_**

```sql
SELECT
    autor.nome,
	autor.codautor,
	autor.nascimento,
	COUNT(livro.cod) AS quantidade
FROM
	autor
LEFT JOIN
	livro ON autor.codautor = livro.autor
GROUP BY
	autor.nome, autor.codautor, autor.nascimento
ORDER BY
	autor.nome
```

&nbsp;

_**EX5.**
Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno._

**_Resposta_**

```sql
SELECT DISTINCT
    autor.nome
FROM
    autor
JOIN
    livro ON autor.codautor = livro.autor
JOIN
    editora ON livro.editora = editora.codeditora
JOIN
    endereco ON editora.endereco = endereco.codendereco
WHERE
    endereco.estado NOT IN ('SANTA CATARINA', 'RIO GRANDE DO SUL', 'PARANÁ')
ORDER BY
    autor.nome ASC;
```

&nbsp;


_**EX6.**
Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes._

**_Resposta_**

```sql
SELECT
	autor.codautor, autor.nome, count(livro.cod) AS quantidade_publicacoes
FROM
	autor
LEFT JOIN
	livro ON autor.codautor = livro.autor
GROUP BY
	autor.codautor, autor.nome
ORDER BY
	quantidade_publicacoes DESC
LIMIT 1;
```

&nbsp;

_**EX7.**
Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente._

**_Resposta_**

```sql
SELECT
    autor.nome
FROM
    autor
LEFT JOIN
    livro ON autor.codautor = livro.autor
WHERE
    livro.cod IS NULL
ORDER BY
    autor.nome
```

---

&nbsp;

<div align="center">

![Bibliotexa Sqlite](<../Images Sprint2/Caso de Estudo - Biblioteca.png>)

**Fonte: Udemy**

---