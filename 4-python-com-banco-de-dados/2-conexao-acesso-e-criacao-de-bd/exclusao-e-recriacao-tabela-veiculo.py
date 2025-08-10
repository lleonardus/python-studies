import sqlite3 as connector

connection = None
cursor = None

try:
    connection = connector.connect("./meu_banco.db")
    cursor = connection.cursor()

    command1 = """
    DROP TABLE IF EXISTS Veiculo;
    """

    cursor.execute(command1)

    command2 = """
    CREATE TABLE Veiculo(
     placa CHARACTER(7) NOT NULL,
     ano INTEGER NOT NULL,
     cor TEXT NOT NULL,
     motor REAL NOT NULL,
     proprietario INTEGER NOT NULL,
     marca INTEGER NOT NULL,
     PRIMARY KEY (placa),
     FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
     FOREIGN KEY(marca) REFERENCES Marca(id)
     );

    """

    cursor.execute(command2)
    connection.commit()

except connector.DatabaseError as err:
    print(f"Erro no banco de dados -> {err}")
finally:
    if connection is not None and cursor is not None:
        cursor.close()
        connection.close()
