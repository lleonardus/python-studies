import sqlite3 as connector
from config import BANCO_NOME
from modelo import Marca, Veiculo

cursor = None
connection = None

try:
    connection = connector.connect(BANCO_NOME)

    # O comando PRAGMA é uma extensão do SQL exclusiva do SQLite, usada para ajustar certos
    # comportamentos internos do banco de dados. Por padrão, o SQLite não aplica a verificação
    # de restrições de chave estrangeira. Isso acontece por razões históricas, já que versões
    # anteriores do SQLite não suportavam chaves estrangeiras. Habilitamos a flag foreign_keys,
    # para garantir que as restrições de chave estrangeiras sejam checadas antes de cada operação.
    connection.execute("PRAGMA foreign_keys = on")

    cursor = connection.cursor()

    # O sqlite cuida da criação de chaves primárias (nesse caso o id da Marca).
    # Como não iremos passar um valor para o id da marca, que é autoincrementado,
    # foi necessário explicitar o nome das colunas no comando INSERT INTO.
    # Caso omitíssemos o nome das colunas, seria gerada uma exceção do tipo OperationalError,
    # com a descrição indicando que a tabela tem 3 colunas, mas apenas dois valores foram fornecidos.
    comando1 = """
    INSERT INTO marca (nome, sigla) VALUES (:nome, :sigla)
    """

    marca1 = Marca(id=1, nome="Marca A", sigla="MA")
    cursor.execute(comando1, vars(marca1))

    # Esse atributo (lastrowid) armazena o id da linha do último registro inserido no banco e está
    # disponível assim que chamamos o método execute do Cursor. O id da linha é o mesmo
    # utilizado para o campo autoincrementado
    marca1.id = cursor.lastrowid

    marca2 = Marca(id=2, nome="Marca B", sigla="MB")
    cursor.execute(comando1, vars(marca2))

    # Esse atributo (lastrowid) armazena o id da linha do último registro inserido no banco e está
    # disponível assim que chamamos o método execute do Cursor. O id da linha é o mesmo
    # utilizado para o campo autoincrementado
    marca2.id = cursor.lastrowid

    # Inserção de dados na tabela Veiculo
    comando2 = """INSERT INTO Veiculo
                VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);"""

    veiculo1 = Veiculo(
        placa="AAA0001",
        ano=2001,
        cor="Prata",
        motor=1.0,
        proprietario=10000000099,
        marca=marca1.id,
    )
    veiculo2 = Veiculo(
        placa="BAA0002",
        ano=2002,
        cor="Preto",
        motor=1.4,
        proprietario=10000000099,
        marca=marca1.id,
    )
    veiculo3 = Veiculo(
        placa="CAA0003",
        ano=2003,
        cor="Branco",
        motor=2.0,
        proprietario=20000000099,
        marca=marca2.id,
    )
    veiculo4 = Veiculo(
        placa="DAA0004",
        ano=2004,
        cor="Azul",
        motor=2.2,
        proprietario=30000000099,
        marca=marca2.id,
    )

    cursor.execute(comando2, vars(veiculo1))
    cursor.execute(comando2, vars(veiculo2))
    cursor.execute(comando2, vars(veiculo3))
    cursor.execute(comando2, vars(veiculo4))

    connection.commit()
except connector.DatabaseError as e:
    print(f"Aconteceu um erro no banco!\n{e}")
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
