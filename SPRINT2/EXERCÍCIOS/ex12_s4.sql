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
