with open('SPRINT3/DESAFIO/actors.csv', 'r') as file:
    lines = file.readlines()

header = lines[0].strip().split(',')

top_movie_index = header.index('#1 Movie')

actor_data = [line.strip().split(',') for line in lines[1:]]
movie_count = {}
for data in actor_data:
    top_movie = data[top_movie_index]
    if top_movie in movie_count:
        movie_count[top_movie] += 1
    else:
        movie_count[top_movie] = 1

sorted_movies = sorted(movie_count.items(), key=lambda x: (-x[1], x[0]))

with open('SPRINT3/DESAFIO/etapa-4.txt', 'w') as output_file:
    for seq, (movie, count) in enumerate(sorted_movies, start=1):
        output_line = f'{seq} - O filme "{movie}" aparece {count} vez(es) no dataset.\n'
        output_file.write(output_line)
