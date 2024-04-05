with open("SPRINT3/DESAFIO/actors.csv", "r") as file:
    lines = file.readlines()

header = lines[0].strip()
lines = lines[1:]

gross_values = []
for line in lines:
    values = line.strip().split(",")
    gross = float(values[-1])
    gross_values.append(gross)

total_gross_sum = sum(gross_values)
num_entries = len(gross_values)
average_gross = total_gross_sum / num_entries

with open("SPRINT3/DESAFIO/etapa-2.txt", "a") as file:
    output_line = f"Média da receita de bilheteria bruta dos principais filmes: {average_gross:.2f}"
    file.write(output_line)