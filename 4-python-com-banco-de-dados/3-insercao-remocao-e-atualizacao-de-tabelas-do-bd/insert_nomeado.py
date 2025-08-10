import sqlite3 as connector
from config import BANCO_NOME
from modelo import Pessoa

cursor = None
connection = None

try:
    connection = connector.connect(BANCO_NOME)
    cursor = connection.cursor()

    pessoa = Pessoa(
        cpf=20000000099,
        nome="José",
        nascimento="1990-02-28",
        oculos=False,
    )

    # Definição de um comando com query parameter
    comando = """INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (:cpf,
        :nome, :nascimento, :oculos);"""

    # Também seria possível usar a função vars pra gerar um dicionário baseado
    # no objeto pessoa: cursor.execute(comando, vars(pessoa))
    cursor.execute(
        comando,
        {
            "cpf": pessoa.cpf,
            "nome": pessoa.nome,
            "nascimento": pessoa.nascimento,
            "oculos": pessoa.oculos,
        },
    )

    connection.commit()
except connector.DatabaseError as e:
    print(f"Aconteceu um erro no banco!\n{e}")
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
