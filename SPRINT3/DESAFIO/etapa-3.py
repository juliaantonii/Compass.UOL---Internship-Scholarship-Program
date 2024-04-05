with open('SPRINT3/DESAFIO/actors.csv', 'r') as file:
    lines = file.readlines()

header = lines[0].strip().split(',')

avg_per_movie_index = header.index('Average per Movie')

actor_data = [line.strip().split(',') for line in lines[1:]]
max_avg_per_movie = 0.0
actor_with_max_avg = ''
for data in actor_data:
    avg_per_movie = float(data[avg_per_movie_index].replace(',', ''))
    if avg_per_movie > max_avg_per_movie:
        max_avg_per_movie = avg_per_movie
        actor_with_max_avg = data[0]

with open('SPRINT3/DESAFIO/etapa-3.txt', 'a') as output_file:
    output_line = f'O ator/atriz com a maior média de receita de bilheteria bruta por filme é {actor_with_max_avg}, com média de {max_avg_per_movie:.2f}.'
    output_file.write(output_line)