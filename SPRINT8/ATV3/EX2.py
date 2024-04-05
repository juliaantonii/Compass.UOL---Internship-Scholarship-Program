import os

caminho_da_pasta = r'C:\Users\User\Desktop\Repositórios GitHub\Compass.UOL REPO\SPRINT8\ATV3'

animais = ["Cachorro", "Gato", "Pato", "Leopardo", "Hamster", "Raposa", "Pinguim", "Golfinho", "Macaco", "Foca", "Canguru",
           "Tubarão", "Papagaio", "Panda", "Arara", "Lobo", "Polvo", "Águia", "Peixe-palhaço", "Pelicano"]

animais_ordenados = sorted(animais)

[print(animal) for animal in animais_ordenados]

caminho_do_arquivo = os.path.join(caminho_da_pasta, 'animais.csv')

with open(caminho_do_arquivo, "w") as arquivo_csv:
    for animal in animais_ordenados:
        arquivo_csv.write(f"{animal}\n")

print(f"Animais armazenados em {caminho_do_arquivo} no formato CSV.")

