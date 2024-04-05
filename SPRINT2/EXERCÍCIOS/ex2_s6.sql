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
