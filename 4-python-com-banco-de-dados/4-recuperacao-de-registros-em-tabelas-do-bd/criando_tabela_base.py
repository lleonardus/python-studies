import sqlite3 as connector
from config import BANCO_NOME

connection = None
cursor = None

try:
    connection = connector.connect(BANCO_NOME)
    cursor = connection.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Pessoa (
        cpf INTEGER NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        oculos BOOLEAN NOT NULL,
        PRIMARY KEY(cpf) 
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Marca (
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        sigla CHARACTER(2) NOT NULL,
        PRIMARY KEY(id)
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Veiculo (
     placa CHARACTER(7) NOT NULL,
     ano INTEGER NOT NULL,
     motor REAL NOT NULL,
     cor TEXT NOT NULL,
     proprietario INTEGER NOT NULL,
     marca INTEGER NOT NULL,
     PRIMARY KEY (placa),
     FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
     FOREIGN KEY(marca) REFERENCES Marca(id)
    );
    """
    )

    connection.commit()
except connector.DatabaseError as e:
    print(f"Aconteceu um erro no banco!\n{e}")
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
