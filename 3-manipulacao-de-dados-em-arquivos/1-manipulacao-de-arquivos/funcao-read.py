with open(file="file.txt", mode="r", encoding="utf-8") as file:
    content = file.read()
    print(
        f"Tipo de conteúdo:{type(content)}\n",
    )
    print("Conteúdo retornado pelo read:\n")
    print(content)
