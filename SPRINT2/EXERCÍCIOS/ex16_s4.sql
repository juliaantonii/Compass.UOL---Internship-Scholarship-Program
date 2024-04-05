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
