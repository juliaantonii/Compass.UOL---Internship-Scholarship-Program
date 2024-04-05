with open('SPRINT3/DESAFIO/actors.csv', 'r') as file:
    lines = file.readlines()

max_num_movies = 0
actor_with_max_movies = ''

for line in lines[1:]:
    values = line.strip().split(',')
    num_movies = int(values[-4])
    
    if num_movies > max_num_movies:
        max_num_movies = num_movies
        actor_with_max_movies = values[0]

with open('SPRINT3/DESAFIO/etapa-1.txt', 'a') as output_file:
    output_line = f'O ator/atriz com maior número de filmes é {actor_with_max_movies}, com {max_num_movies} filmes.'
    output_file.write(output_line)