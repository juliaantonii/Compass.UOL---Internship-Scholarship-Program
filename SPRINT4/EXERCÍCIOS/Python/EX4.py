def calcular_valor_maximo(operadores, operandos):
    operacoes = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '%': lambda x, y: x % y}

    resultados = list(map(lambda op, opd: operacoes[op](opd[0], opd[1]), operadores, operandos))
    
    maximo = float('-inf')