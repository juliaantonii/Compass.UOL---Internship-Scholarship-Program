# EX1.
# Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

nome = input("nome:")
idade = int(input("idade:"))

ano_atual = 2023
ano_c100 = ano_atual + (100 - idade)

print(ano_c100)