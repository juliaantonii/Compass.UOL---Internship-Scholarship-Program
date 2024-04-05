# Seção 6 - Exercícios

_**EX1.**
Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. Utilizar o caractere ; (ponto e vírgula) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:_

+ CodLivro
+ Titulo
+ CodAutor
+ NomeAutor
+ Valor
+ CodEditora
+ NomeEditora

_Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub. Abaixo (na caixa de envio), gentileza nos enviar o link do arquivo .csv que colocou no seu github._

**_Resposta:_**

```sql
SELECT
	livro.cod AS CodLivro,
	livro.titulo AS Titulo,
	autor.codautor AS CodAutor,
	autor.nome AS NomeAutor,
	livro.valor AS Valor,
	editora.codeditora AS CodEditora,
	editora.nome AS NomeEditora
FROM 
	livro
LEFT JOIN
	autor ON livro.autor = autor.codautor
LEFT JOIN
	editora ON livro.editora = editora.codeditora
ORDER BY
	valor DESC
LIMIT 10;
```

Segue abaixo o arquivo em formato .csv (referente a query dos 10 livros mais caros) conforme solicitado:

+ **ARQUIVO .CSV DA ATIVIDADE 1:** [**ATIVIDADE 1**](arquivo1.csv);

Segue abaixo link do arquivo no formato .csv (referente a query dos 10 livros mais caros) conforme solicitado:

+ **LINK DO ARQUIVO DISPONIBILIZADO NO GITHUB:** [**QUERY1 GITHUB**](https://github.com/juliaantonii/Compass-UOL/blob/main/SPRINT2/EXERC%C3%8DCIOS/arquivo1.csv);

---

&nbsp;

_**EX2.**
Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV. Utilizar o caractere | (pipe) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:_

+ CodEditora
+ NomeEditora
+ QuantidadeLivros

_Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub. Abaixo (na caixa de envio), gentileza nos enviar o link do arquivo .csv que colocou no seu github._

**_Resposta:_**

```sql
SELECT
	editora.codeditora AS CodEditora,
	editora.nome AS NomeEditora,
	COUNT(livro.cod) AS QuantidadeLivros
FROM 
	editora
INNER JOIN
	livro ON editora.codeditora = livro.editora
GROUP BY
	editora.codeditora, editora.nome
ORDER BY
	QuantidadeLivros DESC
LIMIT 5
```

Segue abaixo o arquivo em formato .csv (referente a query das 5 editoras com maior quantidade de livros na biblioteca) conforme solicitado:

+ **ARQUIVO .CSV DA ATIVIDADE 1:** [**ATIVIDADE 2**](arquivo2.csv);

Segue abaixo link do arquivo no formato .csv (referente a query das 5 editoras com maior quantidade de livros na biblioteca) conforme solicitado:

+ **LINK DO ARQUIVO DISPONIBILIZADO NO GITHUB:** [**QUERY2 GITHUB**](https://github.com/juliaantonii/Compass-UOL/blob/main/SPRINT2/EXERC%C3%8DCIOS/arquivo2.csv);
  
---