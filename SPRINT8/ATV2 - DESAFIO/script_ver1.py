import boto3
import json
import pandas as pd

# Configuração das credenciais diretamente no script
aws_access_key_id = '-'
aws_secret_access_key = '-'

# Configuração do cliente S3 da AWS com as credenciais
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
# Configuração do cliente S3 da AWS
s3 = boto3.client('s3')

# Nome do bucket da AWS e nome do arquivo JSON
bucket_name = 'compass.desafio'
json_file_name = 'prt-uty-nfd.json'

# Nome do arquivo de saída para salvar os resultados
output_file_name = 'analise-filmes.csv'

# Baixa o arquivo JSON do S3
s3.download_file(bucket_name, json_file_name, json_file_name)

# Lê o arquivo JSON
with open(json_file_name, 'r') as json_file:
    data = json.load(json_file)

# Cria um DataFrame do Pandas para facilitar a análise dos dados
df = pd.DataFrame(data)

# Exemplo de análise: contar a participação dos artistas nos filmes
artist_participation = df['artist'].value_counts()

# Salvar os resultados em um arquivo CSV
artist_participation.to_csv(output_file_name)

print("Análise concluída. Resultados salvos em", output_file_name)
