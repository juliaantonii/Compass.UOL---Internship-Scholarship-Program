from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, when, expr

# part 1
# Crie uma sessão Spark
spark = SparkSession.builder \
    .master("local[*]")\
    .appName("Exercicio Intro") \
    .getOrCreate()

# Leia o arquivo CSV
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes.show(5)

# part 2
# Mostre o esquema do DataFrame
df_nomes.printSchema()

# Mostre as 10 primeiras linhas do DataFrame
df_nomes.show(10)

# part 3
# Adicione a coluna "Escolaridade" de forma aleatória
df_nomes = df_nomes.withColumn("Escolaridade", when(rand() <= 0.33, "Fundamental")
                                   .when((rand() > 0.33) & (rand() <= 0.67), "Médio")
                                   .otherwise("Superior"))
df_nomes.show()

# part 4
# Adicione a coluna "Pais" de forma aleatória
paises_sul_america = ["Argentina", "Brasil", "Chile", "Colômbia", "Equador", "Paraguai", "Peru", "Uruguai", "Venezuela", "Bolívia", "Guiana", "Suriname", "Guiana Francesa"]
df_nomes = df_nomes.withColumn("Pais", when(rand() <= 0.1, "Argentina")
                                   .when(rand() <= 0.2, "Brasil")
                                   .when(rand() <= 0.3, "Chile")
                                   .when(rand() <= 0.4, "Colômbia")
                                   .when(rand() <= 0.5, "Equador")
                                   .when(rand() <= 0.6, "Paraguai")
                                   .when(rand() <= 0.7, "Peru")
                                   .when(rand() <= 0.8, "Uruguai")
                                   .when(rand() <= 0.9, "Venezuela")
                                   .otherwise("Bolívia"))

# part 5
# Adicione a coluna "AnoNascimento" de forma aleatória
df_nomes = df_nomes.withColumn("AnoNascimento", expr("int(1945 + rand() * 66)"))

# part 6
# Selecione pessoas que nasceram neste século (a partir de 2000)
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000)
df_select.show(10)

# part 7
# Registre o DataFrame como uma tabela temporária
df_nomes.createOrReplaceTempView("pessoas")

# Execute a consulta SQL para selecionar pessoas que nasceram neste século
query_sql = """
SELECT *
FROM pessoas
WHERE AnoNascimento >= 2000
"""
df_select_sql = spark.sql(query_sql)
df_select_sql.show(10)

# part 8
# Contar o número de Millennials (nascidos entre 1980 e 1994)
df_millennials = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994))
count_millennials = df_millennials.count()
print(f"Número de Millennials: {count_millennials}")

# part 9
# Execute a consulta SQL para contar o número de Millennials
query_millennials = """
SELECT COUNT(*) AS CountMillennials
FROM pessoas
WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994
"""

millennials_count = spark.sql(query_millennials).first()[0]
print(f"Número de Millennials: {millennials_count}")

df_nomes.createOrReplaceTempView("pessoas")

# part 10
# Defina as consultas SQL
queryBoomers = """
SELECT Pais, 'Baby Boomers' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1944 AND AnoNascimento <= 1964
GROUP BY Pais
"""

queryGenX = """
SELECT Pais, 'Geracao X' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1965 AND AnoNascimento <= 1979
GROUP BY Pais
"""

queryMillennials2 = """
SELECT Pais, 'Millennials' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994
GROUP BY Pais
"""

queryGenZ = """
SELECT Pais, 'Geracao Z' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1995 AND AnoNascimento <= 2015
GROUP BY Pais
"""

# Execute as consultas SQL
dfResultado = spark.sql(queryBoomers).union(spark.sql(queryGenX)).union(spark.sql(queryMillennials2)).union(spark.sql(queryGenZ))
dfResultado = dfResultado.orderBy("Pais", "Geracao", "Quantidade")
dfResultado.show()