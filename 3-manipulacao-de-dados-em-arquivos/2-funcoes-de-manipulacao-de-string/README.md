# Funções de Manipulação de String

## `str.strip([chars])`

Retorna uma cópia da string com os caracterers da frente e de trás removidos. O
argumentos chars é uma string que serve para especificar o conjunto de
caracteres que será removido. Quando nenhum argumento é passado, o
comnportamento padrão da função é remover os espaços do começo e do final da
string.

```python

string = '      www.example.com         '
string2= 'comwwwexample.www.google.com'

print(string.strip()) # 'www.example.com'
print(string.strip('cmowz. ')) # 'example' =>  'www.' e '.com' foram removidos
print(string.strip('cmowz ')) # '.example.' =>  'www' e 'com' foram removidos
print(string.strip('cowz. ')) # 'example.com' => 'www.' foi removido
print(string2.strip('cmowz. ')) # 'example.www.google' =>  '.com' e 'comwww' foram removidos

```

Note que apenas as combinações no começo da string e no final foram removidas. O
scaracters são removidos do começo até chegarem em um caracter que não está
contido em chars. O mesmo comportamento acontece na remoção dos caracteres do
final.

## ` str.count(sub[, start[, end]])`

Retorna o número de ocorrências de uma string dentro de um intervalo opcional.

```python
string = 'spam, spam, spam'


print(f"string.count('') => {string.count('')}") #17
print(f"string.count('spam') => {string.count('spam')}") #3
print(f"string.count('spam, 5') => {string.count('spam', 5)}") #2
print(f"string.count('spam, 5, 10') => {string.count('spam', 5, 10)}") #1

```

## `str.split(sep=None, maxsplit=-1)`

Retorna uma lista de palavras dentro da string, utilizando sep como delimitador.
O parâmetro maxsplit serve para setar o número máximo de vezes que a string pode
ser dividida

```python

print('1,2,3'.split(',')) # ['1', '2', '3']
print('1,2,3'.split(',', maxsplit=1)) # ['1', '2,3']
print('1,2,,3,'.split(',')) # ['1', '2', '', '3', '']
print('1<>2<>3<4'.split('<>')) # ['1', '2', '3<4']

```

## `str.join(iterable)`

Retorna uma string que é a concatenação das strings em um iterable. O separador
é a string que provê o método

```python
print(", ".join(['Java', 'TypeScript', 'Python'])) # Java, TypeScript, Python

```

Fontes:

- https://docs.python.org/3/library/stdtypes.html#str.strip
- https://docs.python.org/3/library/stdtypes.html#str.count
- https://docs.python.org/3/library/stdtypes.html#str.split
- https://docs.python.org/3/library/stdtypes.html#str.join
