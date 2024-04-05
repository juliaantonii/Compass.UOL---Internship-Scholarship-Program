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
