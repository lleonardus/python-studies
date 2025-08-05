import os

# ABRINDO UM ARQUIVO

# Abrindo arquivo usando caminho relativo
file = open(file="file.txt", mode="r", encoding="utf-8")

# Mostando caminho absoluto do arquivo
print(os.path.abspath(file.name))

# Mostando caminho relativo do arquivo
print(os.path.relpath(file.name))

# Printando o arquivo, que é um objeto do tipo TextIOWrapper
print(file)

# Alguns atributos do arquivo
print("Nome do arquivo:", file.name)
print("Modo do arquivo:", file.mode)
print("Arquivo fechado?", file.closed)

# Fechando arquivo
file.close()

print("Arquivo fechado?", file.closed)
