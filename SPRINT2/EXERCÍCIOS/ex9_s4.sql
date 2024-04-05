SELECT 
    cdpro, nmpro
FROM 
    tbvendas
WHERE 
    dtven BETWEEN '2014-02-03' AND '2018-02-02' AND status = 'Concluído'
GROUP BY 
    qtd
order by 
    qtd  DESC
limit 1
