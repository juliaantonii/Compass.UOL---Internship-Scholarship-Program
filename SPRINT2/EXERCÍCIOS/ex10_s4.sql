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
