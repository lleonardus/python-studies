with open(file="file.txt", mode="r", encoding="utf-8") as file:
    content = file.readlines()  # equivalente a list(file)

    print(
        f"Tipo de conteúdo: {type(content)}\n",
    )

    print("Conteúdo retornado pelo readlines:\n")
    print(repr(content))

    print("\nIterando sobre o arquivo: \n")

    for line in content:
        print(repr(line))
