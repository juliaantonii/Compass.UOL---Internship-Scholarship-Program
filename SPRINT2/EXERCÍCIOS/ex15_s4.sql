SELECT
    tbvendas.cdven
FROM
    tbvendas
WHERE
    tbvendas.deletado = 1
ORDER BY
    tbvendas.cdven ASC;
