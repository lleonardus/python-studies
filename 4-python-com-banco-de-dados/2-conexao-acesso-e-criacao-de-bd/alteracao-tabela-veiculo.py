import sqlite3 as connector

connection = None
cursor = None

try:
    connection = connector.connect("./meu_banco.db")
    cursor = connection.cursor()

    command = """
    ALTER TABLE Veiculo
    ADD motor REAL;
    """

    cursor.execute(command)
    connection.commit()

except connector.DatabaseError as err:
    print(f"Erro no banco de dados -> {err}")
finally:
    if connection is not None and cursor is not None:
        cursor.close()
        connection.close()
