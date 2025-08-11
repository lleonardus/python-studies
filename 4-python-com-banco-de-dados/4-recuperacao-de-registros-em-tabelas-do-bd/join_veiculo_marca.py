import sqlite3 as connector
from config import BANCO_NOME
from typing import Any
from modelo import Veiculo, Marca

cursor = None
connection = None

try:
    connection = connector.connect(BANCO_NOME)
    cursor = connection.cursor()

    comando = """SELECT * FROM Veiculo JOIN Marca on Veiculo.marca = Marca.id """

    cursor.execute(comando)

    registros: list[tuple[Any, ...]] = cursor.fetchall()

    for registro in registros:
        # Ver modelo.py e criando_tabela_base.py para entender a ordem das colunas
        print(registro)

        # Primeiros 5 dados são do veiculo
        veiculo = Veiculo(*registro[:6])
        # Do dado 6 em diante é da marca
        marca = Marca(*registro[6:])

        print(
            "Placa:",
            veiculo.placa,
            ", Marca:",
            marca.nome,
        )

    connection.commit()
except connector.DatabaseError as e:
    print(f"Aconteceu um erro no banco!\n{e}")
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
