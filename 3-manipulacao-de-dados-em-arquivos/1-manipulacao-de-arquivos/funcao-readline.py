with open(file="file.txt", mode="r", encoding="utf-8") as file:
    content = file.readline()
    print(
        f"Tipo de conteúdo:{type(content)}\n",
    )
    print("Conteúdo retornado pelo primeiro readline:\n")
    print(content)

    next_content = file.readline()

    print("Conteúdo retornado pelo segundo readline:\n")
    print(next_content)
