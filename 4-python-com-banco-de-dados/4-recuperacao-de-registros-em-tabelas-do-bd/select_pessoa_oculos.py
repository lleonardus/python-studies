import sqlite3 as connector
from config import BANCO_NOME
from modelo import Pessoa
from datetime import date

cursor = None
connection = None

try:
    # Convertendo byte (0, 1) para booleano. Vai ajudar a converter a coluna oculos
    connector.register_converter("BOOLEAN", lambda x: int(x) == 1)

    # Converte os tipos do sqlite para os tipos do Python
    connection = connector.connect(BANCO_NOME, detect_types=connector.PARSE_DECLTYPES)
    cursor = connection.cursor()

    comando = """SELECT * FROM Pessoa WHERE oculos=:oculos"""

    cursor.execute(comando, {"oculos": True})

    # Lista de tuplas do tipo Pessoa. Funciona apenas porque podemos garantir
    # que a ordem das colunas da tabela é a mesma ordem da classe!
    registros: list[tuple[int, str, str | date, bool]] = cursor.fetchall()

    for registro in registros:
        # Foi utilizado o operador * do Python. Esse operador “desempacota” um iterável,
        # passando cada elemento como um argumento para uma função ou construtor.
        pessoa = Pessoa(*registro)
        print("cpf: ", type(pessoa.cpf), pessoa.cpf)
        print("nome: ", type(pessoa.nome), pessoa.nome)
        print("nascimento: ", type(pessoa.nascimento), pessoa.nascimento)
        print("oculos: ", type(pessoa.oculos), pessoa.oculos)

    connection.commit()
except connector.DatabaseError as e:
    print(f"Aconteceu um erro no banco!\n{e}")
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
