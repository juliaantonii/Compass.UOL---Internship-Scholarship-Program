import json
import boto3
import requests
from datetime import datetime

def lambda_handler(event, context):
    # Nome do seu bucket S3
    s3_bucket_name = 'compass.desafio'
    
    # Configure as chaves de API do TMDB
    tmdb_api_key = "-"
    tmdb_url = '-'
    
    # Parâmetros para consulta na API do TMDB (exemplo: filmes de terror)
    params = {
        'api_key': tmdb_api_key,
        'with_genres': '27',  # Código de gênero para filmes de terror
        'language': 'en-US',  # Idioma dos resultados
        'page': 1  # Página da consulta
    }

    # Realiza a consulta à API do TMDB
    response = requests.get(tmdb_url, params=params)
    tmdb_data = response.json()
    
    # Nome do arquivo no S3
    current_datetime = datetime.now()
    year = current_datetime.strftime('%Y')
    month = current_datetime.strftime('%m')
    day = current_datetime.strftime('%d')
    s3_file_name = f'raw/tmdb/json/{year}/{month}/{day}/tmdb_data.json'
    
    # Armazena os dados do TMDB no S3
    s3 = boto3.client('s3')
    s3.put_object(Bucket=s3_bucket_name, Key=s3_file_name, Body=json.dumps(tmdb_data))
    
    # Realize a análise dos dados do TMDB para entender como o ano de lançamento afeta notas e popularidade
    analysis_result = analyze_tmdb_data(tmdb_data)
    
    # Armazene os resultados da análise no S3
    s3_file_name_result = f'raw/tmdb/json/{year}/{month}/{day}/tmdb_result.json'
    s3.put_object(Bucket=s3_bucket_name, Key=s3_file_name_result, Body=json.dumps(analysis_result))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Dados do TMDB foram consumidos e a análise foi armazenada no S3 com sucesso!')
    }

from collections import defaultdict

def analyze_tmdb_data(tmdb_data):
    # Realize a análise dos dados do TMDB para encontrar o filme com a maior média por década
    # e registre o número de votos desse filme
    # Por exemplo, dividir os dados em décadas, encontrar o filme com a maior média por década e o número de votos
    # Retorne o resultado da análise
    
    # Crie um dicionário para armazenar os filmes com a maior média por década
    best_movies_by_decade = defaultdict(lambda: {'title': '', 'vote_average': 0, 'vote_count': 0, 'release_year': 0})
    
    for movie in tmdb_data['results']:
        release_year = int(movie['release_date'][:4])
        # Encontre a década do filme
        decade = release_year // 10 * 10
        if movie['vote_average'] > best_movies_by_decade[decade]['vote_average']:
            best_movies_by_decade[decade] = {
                'title': movie['title'],
                'vote_average': movie['vote_average'],
                'vote_count': movie['vote_count'],
                'release_year': release_year
            }
    
    result = list(best_movies_by_decade.values())
    
    return result
