with open('SPRINT3/DESAFIO/actors.csv', 'r') as file:
    lines = file.readlines()

header = lines[0].strip().split(',')

actor_index = header.index('Actor')
total_gross_index = header.index('Total Gross')

actor_total_gross_list = []
for line in lines[1:]:
    values = line.strip().split(',')
    actor = values[actor_index]
    total_gross = values[total_gross_index].strip()

    if total_gross.replace('.', '', 1).replace(',', '', 1).replace(' ', '', 1).replace('Jr.', '', 1).isdigit():
        total_gross = float(total_gross.replace(',', '').replace(' ', ''))
        actor_total_gross_list.append((actor, total_gross))

sorted_actor_total_gross = sorted(actor_total_gross_list, key=lambda x: x[1], reverse=True)

with open('SPRINT3/DESAFIO/etapa-5.txt', 'a') as file:
    for actor, total_gross in sorted_actor_total_gross:
        file.write(f'{actor} - {total_gross:.2f}\n')
