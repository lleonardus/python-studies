import sqlite3 as connector

connection = None
cursor = None

try:
    # Abertura de conexão e aquisição de cursor
    connection = connector.connect("./meu_banco.db")
    cursor = connection.cursor()

    command = """
    CREATE TABLE Pessoa (
        cpf INTEGER NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        oculos BOOLEAN NOT NULL,
        primary key (cpf) 
    );
    """

    # Executando comando
    cursor.execute(command)

    # Efetivação do comando
    connection.commit()
except connector.DatabaseError as err:
    print(f"Erro do banco de dados: {err}")
finally:
    # Fechamento das conexões
    if connection is not None and cursor is not None:
        cursor.close()
        connection.close()
