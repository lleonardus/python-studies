CREATE TABLE agenda
(
   id serial NOT NULL,
   nome text NOT NULL,
   telefone char(12) NOT NULL
);

INSERT INTO agenda(nome, telefone)
VALUES ('teste 1', '02199999999');


INSERT INTO agenda(nome, telefone)
VALUES ('teste 2', '02188888888');


CREATE TABLE produto (
    codigo SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL
);
