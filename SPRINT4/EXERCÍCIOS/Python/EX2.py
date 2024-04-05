def conta_vogais(texto: str) -> int:
    texto = texto.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

    is_vogal = lambda char: char in 'aeiou'

    vogais = filter(is_vogal, texto)

    return len(list(vogais))