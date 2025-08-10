import sqlite3 as connector
from config import BANCO_NOME
from modelo import Pessoa

cursor = None
connection = None

try:
    connection = connector.connect(BANCO_NOME)
    cursor = connection.cursor()

    pessoa = Pessoa(
        cpf=10000000099,
        nome="Maria",
        nascimento="1990-01-31",
        oculos=False,
    )

    # Definição de um comando com query parameter
    comando = (
        """INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);"""
    )

    cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.oculos))

    connection.commit()
except connector.DatabaseError as e:
    print(f"Aconteceu um erro no banco!\n{e}")
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
