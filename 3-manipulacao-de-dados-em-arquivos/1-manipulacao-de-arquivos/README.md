Fonte:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# `operacoes-basicas.py`

Explorando algumas funções básicas para trabalhar com arquivos

# `funcao-read.py`

`read` é um método de TextIOWrapper que permite ler uma quantidade de dados de
um arquivo. É possível setar essa quantidade com o parâmetro size, e quando
nenhum valor é fornecido, fica entendido que se deve ler o arquivo completo.

# `funcao-readline.py`

Lê uma única linha em um arquivo

# `funcao-readlines.py`

Retorna as linhas de um arquivo na forma de lista. É equivalente a list(file.txt)

# `funcao-write.py`

Escreve uma linha em um arquivo

# `funcao-writelines.py`

Escreve os elementos de uma lista em um arquivo

# `manipulando-arquivo.py`

A ideia é desenvolver um programa em Python que permita a captura de texto via console,
no qual um editor pode inserir trechos de textos recebidos dos autores.
O programa deve salvar esses trechos em um arquivo de texto, ler o arquivo,
converter todo o texto para letras maiúsculas para padronizar a formatação e
finalmente sobrescrever o arquivo original com o texto formatado.
Esse processo facilitará a revisão preliminar antes da edição final.
