-- Tabela de Fatos
CREATE TABLE fato_filme (
    id_filme VARCHAR(10) PRIMARY KEY,
    quantidade INT,
    ano_lancamento INT,
    id_pais INT,
    id_genero_filme INT,
    id_avaliacao INT,
    id_artista INT,
    FOREIGN KEY (id_pais) REFERENCES dim_pais(id),
    FOREIGN KEY (id_genero_filme) REFERENCES dim_genero(id),
    FOREIGN KEY (id_avaliacao) REFERENCES dim_avaliacao(id),
    FOREIGN KEY (id_artista) REFERENCES dim_artista(id)
);

-- Tabela de Dimensão para País
CREATE TABLE dim_pais (
    id INT PRIMARY KEY,
    nome VARCHAR(255)
);

-- Tabela de Dimensão para Gênero
CREATE TABLE dim_genero (
    id INT PRIMARY KEY,
    genero VARCHAR(255)
);

-- Tabela de Dimensão para Avaliação
CREATE TABLE dim_avaliacao (
    id INT PRIMARY KEY,
    nota FLOAT,
    popularidade FLOAT,
    n_votos INT
);

-- Tabela de Dimensão para Artista
CREATE TABLE dim_artista (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    nascimento INT,
    sexo VARCHAR(255),
    personagem VARCHAR(255),
    profissao VARCHAR(255)
);

