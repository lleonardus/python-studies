import sqlite3 as connector

connection = None
cursor = None

try:
    connection = connector.connect("./meu_banco.db")
    cursor = connection.cursor()

    command = """
    CREATE TABLE Marca(
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        sigla CHARACTER(2) NOT NULL,
        PRIMARY KEY (id)
    );
    """

    cursor.execute(command)
    connection.commit()

except connector.DatabaseError as err:
    print(f"Erro do banco de dados: {err}")
finally:
    if connection is not None and cursor is not None:
        cursor.close()
        connection.close()
