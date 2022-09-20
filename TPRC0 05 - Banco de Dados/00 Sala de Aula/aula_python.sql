create database aula_python;
use aula_python;

CREATE TABLE aluno (
    idaluno INT PRIMARY KEY,
    nome VARCHAR(70),
    flag INT,
    enderaco VARCHAR(100),
    nascimento DATE,
    cidade VARCHAR(70),
    uf VARCHAR(2),
    cef VARCHAR(10)
);