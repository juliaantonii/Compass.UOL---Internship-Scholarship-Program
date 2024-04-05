import json
import requests
import boto3
from datetime import datetime

def get_movie_details(movie_id, api_key):

    movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'append_to_response': 'revenue,budget',
    }
    
    response = requests.get(movie_url, params=params)

    return response.json()

def lambda_handler(event, context):

    api_key = '-'
    base_url = '-'
    s3_bucket_name = 'compass.desafio'
    
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'include_adult': 'false',
        'include_video': 'false',
        'page': 1
    }
    
    s3_client = boto3.client('s3')
    
    current_date = datetime.utcnow().strftime('%Y/%m/%d')
    s3_prefix = f'RAW/tmdb/json/{current_date}'
    
    current_page = 1
    while True:

        params['page'] = current_page

        response = requests.get(base_url, params=params)
        data = response.json()
        
        if current_page > data['total_pages']:
            break

        chunks = [data['results'][i:i + 100] for i in range(0, len(data['results']), 100)]

        for i, chunk in enumerate(chunks):
            for movie in chunk:
                movie_id = movie.get('id')
                if movie_id:
                    movie_details = get_movie_details(movie_id, api_key)
                    movie['revenue'] = movie_details.get('revenue')
                    movie['budget'] = movie_details.get('budget')

            s3_object_key = f'{s3_prefix}/prt-uty-nfd_{i + 1}.json'
            s3_object_url = f's3://{s3_bucket_name}/{s3_object_key}'

            s3_client.put_object(
                Bucket=s3_bucket_name,
                Key=s3_object_key,
                Body=json.dumps(chunk),
                ContentType='application/json'
            )

        current_page += 1

    return {
        'statusCode': 200,
        'body': json.dumps('Dados salvos no S3 com sucesso!')
    }
