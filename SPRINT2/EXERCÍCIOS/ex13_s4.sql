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
