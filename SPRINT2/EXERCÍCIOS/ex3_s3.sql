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
