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
