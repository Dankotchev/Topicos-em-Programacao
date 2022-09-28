create database bd_trabalho_python;
use bd_trabalho_python;

CREATE TABLE cliente (
    idCliente   INT AUTO_INCREMENT,
    nome        VARCHAR (60),
    cpf         VARCHAR(16)
    endereco    VARCHAR(60),
    telefone    VARCHAR(18),
    email       VARCHAR(100),
    cidade      VARCHAR(60),
    uf          VARCHAR(2),
    cep         VARCHAR(18),
    PRIMARY KEY (idCliente)
);

CREATE TABLE venda (
    idVenda         INT AUTO_INCREMENT,
    data            DATE,
    valortotal      DECIMAL(10,2),
    idCliente       INT NOT NULL,
    PRIMARY KEY (idVenda),
    FOREIGN KEY (idCliente) REFERENCES cliente (idCliente)
);

CREATE TABLE produto (
    idProduto       INT AUTO_INCREMENT PRIMARY KEY,
    nome            VARCHAR(60),
    quantidade      INT,
    valor           DECIMAL(10,2)
);

CREATE TABLE item_venda(
    idVenda         INT NOT NULL,
    idProduto       INT NOT NULL,
    quantidade      INT NOT NULL,
    valor           DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (idVenda, idProduto),
    FOREIGN KEY (idVenda)   REFERENCES venda (idVenda),
    FOREIGN KEY (idProduto) REFERENCES produto (idProduto)
);