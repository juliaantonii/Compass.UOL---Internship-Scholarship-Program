CREATE TABLE FatoLocacao (
    idFatoLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    idDataTempo INT,
    qtdDiaria INT,
    valorDiaria DECIMAL(18, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES DimCliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES DimCarro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES DimVendedor(idVendedor),
    FOREIGN KEY (idDataTempo) REFERENCES DimDataTempo(idDataTempo)
);

-- Tabelas de Dimensões
CREATE TABLE DimCliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

CREATE TABLE DimCarro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    chassiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES DimCombustivel(idCombustivel)
);

CREATE TABLE DimVendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

CREATE TABLE DimDataTempo (
    idDataTempo INT PRIMARY KEY,
    dataLocacao DATETIME,
    horaLocacao TIME
);

-- Tabela de Dimensão Adicional (DimCombustivel
CREATE TABLE DimCombustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);