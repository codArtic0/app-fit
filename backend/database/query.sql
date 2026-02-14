CREATE TABLE IF NOT EXISTS usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(25) NOT NULL,
    sexo VARCHAR(1) NOT NULL,
    altura FLOAT NOT NULL,
    idade INT NOT NULL,
    peso FLOAT NOT NULL,
    nivel_atividade INT NOT NULL
);