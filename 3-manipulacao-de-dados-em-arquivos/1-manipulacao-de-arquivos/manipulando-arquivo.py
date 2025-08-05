def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")

    frases = []

    while True:
        frase = input("> ")
        if frase.lower() == "sair":
            break
        frases.append(frase)

    with open(file="file.txt", mode="w", encoding="utf-8") as file:
        for frase in frases:
            file.write(f"{frase}\n")

    frases_uppercase = []

    with open(file="file.txt", mode="r", encoding="utf-8") as file:
        for frase in file:
            frases_uppercase.append(frase.strip().upper())

    with open(file="file.txt", mode="w", encoding="utf-8") as file:
        for frase in frases_uppercase:
            file.write(f"{frase}\n")


if __name__ == "__main__":
    main()
