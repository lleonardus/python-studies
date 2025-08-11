import sqlite3 as connector
from config import BANCO_NOME
from modelo import Marca, Pessoa, Veiculo

cursor = None
connection = None

pessoa1 = Pessoa(
    cpf=10000000099,
    nome="Maria",
    nascimento="1990-01-31",
    oculos=False,
)

try:
    connection = connector.connect(BANCO_NOME)
    cursor = connection.cursor()

    pessoa1 = Pessoa(
        cpf=10000000099,
        nome="Maria",
        nascimento="1990-01-31",
        oculos=False,
    )

    pessoa2 = Pessoa(
        cpf=20000000099,
        nome="João",
        nascimento="1980-02-28",
        oculos=True,
    )

    pessoa3 = Pessoa(
        cpf=30000000099,
        nome="José",
        nascimento="1992-11-10",
        oculos=False,
    )

    pessoas = [
        (pessoa1.cpf, pessoa1.nome, pessoa1.nascimento, pessoa1.oculos),
        (pessoa2.cpf, pessoa2.nome, pessoa2.nascimento, pessoa2.oculos),
        (pessoa3.cpf, pessoa3.nome, pessoa3.nascimento, pessoa3.oculos),
    ]

    comando = (
        """INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);"""
    )

    comando1 = """
    INSERT INTO marca (nome, sigla) VALUES (:nome, :sigla)
    """

    marca1 = Marca(id=1, nome="Marca A", sigla="MA")
    cursor.execute(comando1, vars(marca1))

    marca1.id = cursor.lastrowid

    marca2 = Marca(id=2, nome="Marca B", sigla="MB")
    cursor.execute(comando1, vars(marca2))

    marca2.id = cursor.lastrowid

    comando2 = """INSERT INTO Veiculo
                VALUES (:placa, :ano, :motor, :cor, :proprietario, :marca);"""

    veiculo1 = Veiculo(
        placa="AAA0001",
        ano=2001,
        motor=1.0,
        cor="Prata",
        proprietario=10000000099,
        marca=marca1.id,
    )
    veiculo2 = Veiculo(
        placa="BAA0002",
        ano=2002,
        motor=1.4,
        cor="Preto",
        proprietario=10000000099,
        marca=marca1.id,
    )
    veiculo3 = Veiculo(
        placa="CAA0003",
        ano=2003,
        motor=2.0,
        cor="Branco",
        proprietario=20000000099,
        marca=marca2.id,
    )
    veiculo4 = Veiculo(
        placa="DAA0004",
        ano=2004,
        motor=2.2,
        cor="Azul",
        proprietario=30000000099,
        marca=marca2.id,
    )

    cursor.execute(comando2, vars(veiculo1))
    cursor.execute(comando2, vars(veiculo2))
    cursor.execute(comando2, vars(veiculo3))
    cursor.execute(comando2, vars(veiculo4))

    cursor.executemany(comando, pessoas)

    connection.commit()
except connector.DatabaseError as e:
    print(f"Aconteceu um erro no banco!\n{e}")
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
