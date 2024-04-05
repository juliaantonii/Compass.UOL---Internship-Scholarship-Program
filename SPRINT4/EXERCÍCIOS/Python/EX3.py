def calcula_saldo(lancamentos) -> float:
    from functools import reduce

    calcular_valor = lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0]

    valores = map(calcular_valor, lancamentos)

    saldo_final = reduce(lambda x, y: x + y, valores, 0)
    
    return saldo_final