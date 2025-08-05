string = "  www.example.com   "
string2 = "comwwwexample.www.google.com"

print(f"Operações de split com a string '{string}':")
print(f"string.strip() => {string.strip()}")
print(f"string.strip('cmowz. ') => '{string.strip('cmowz. ')}'")
print(f"string.strip('cmowz ') => '{string.strip('cmowz ')}'")
print(f"string.strip('cowz. ') => '{string.strip('cowz. ')}'")
print(f"string.strip('cowz. ') => '{string.strip('cowz. ')}'")
print(f"Operações de split com a string '{string2}':")
print(f"string2.strip('cmowz. ') => '{string2.strip('cmowz. ')}'")

print("\n")


string = "spam, spam, spam"

print(f"Operações de count com a string '{string}':")
print(f"string.count('') => {string.count('')}")
print(f"string.count('spam') => {string.count('spam')}")
print(f"string.count('spam, 5') => {string.count('spam', 5)}")
print(f"string.count('spam, 5, 10') => {string.count('spam', 5, 10)}")

print("\n")


print(f"Operações de split:")

print(f"'1,2,3'.split(',') => {'1,2,3'.split(',')}")
print(f"'1,2,3'.split(',', maxsplit=1) => {'1,2,3'.split(',', maxsplit=1)}")
print(f"'1,2,,3,'.split(',') => {'1,2,,3,'.split(',')}")
print(f"'1<>2<>3<4'.split('<>') => {'1<>2<>3<4'.split('<>')}")
