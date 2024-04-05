import json
import boto3
import pandas as pd
from datetime import datetime

def lambda_handler(event, context):
    s3_bucket_name = 'compass.desafio'
    
    current_datetime = datetime.now()
    year = current_datetime.strftime('%Y')
    month = current_datetime.strftime('%m')
    day = current_datetime.strftime('%d')
    
    s3_key_to_check = 'RAW/LOCAL/CSV/Movies/2023/10/23/movies.csv'

    s3 = boto3.client('s3')

    # Verifica a existência do arquivo no S3

    response = s3.get_object(Bucket=s3_bucket_name, Key=s3_key_to_check)
    df = pd.read_csv(response['Body'], sep='|')
    
    # Filtra apenas os filmes de terror
    terror_movies = df[df['genero'].str.lower().str.contains('Horror')]

    # Nome do arquivo a ser armazenado no S3
    s3_layer = 'raw'
    s3_origin = 'tmdb'
    s3_format = 'json'
    s3_key = f'{s3_layer}/{s3_origin}/{s3_format}/{year}/{month}/{day}/prt-uty-nfd.json'

    # Converter os dados em JSON
    json_data = terror_movies.to_json(orient='records')

    # Armazenar o arquivo JSON no S3
    s3.put_object(Bucket=s3_bucket_name, Key=s3_key, Body=json_data)

    return {
        'statusCode': 200,
        'body': json.dumps('Análise dos filmes de terror realizada e dados armazenados no S3 com sucesso!')
    }