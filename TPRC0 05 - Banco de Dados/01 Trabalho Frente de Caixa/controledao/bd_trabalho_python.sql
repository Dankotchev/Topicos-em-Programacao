create database bd_trabalho_python;
use bd_trabalho_python;

CREATE TABLE cliente (
    idcliente   INT AUTO_INCREMENT PRIMARY KEY,
    nome        VARCHAR (60),
    endereco    VARCHAR(60),
    telefone    VARCHAR(18),
    email       VARCHAR(100),
    cidade      VARCHAR(60),
    uf          VARCHAR(2),
    cep         VARCHAR(18)
);

CREATE TABLE venda (
    idvenda         INT AUTO_INCREMENT,
    data            DATE,
    valortotal      DECIMAL(10,2),
    idcliente       INT NOT NULL,
    PRIMARY KEY (idvenda),
    FOREIGN KEY (idcliente) REFERENCES cliente (idcliente)
);

CREATE TABLE produto (
    idproduto       INT AUTO_INCREMENT PRIMARY KEY,
    nome            VARCHAR(60),
    quantidade      INT,
    valor           DECIMAL(10,2)
);

CREATE TABLE item_venda(
    idvenda         INT NOT NULL,
    idproduto       INT NOT NULL,
    quantidade      INT NOT NULL,
    valor           DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (idvenda, idproduto),
    FOREIGN KEY (idvenda)   REFERENCES venda (idvenda),
    FOREIGN KEY (idproduto) REFERENCES produto (idproduto)
);