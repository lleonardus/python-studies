with open(file="file.txt", mode="w", encoding="utf-8") as file:
    file.writelines(
        [
            "Conteúdo da Primeira Linha.\n",
            "Conteúdo da Segunda Linha.\n",
            "Conteúdo da Terceira Linha\n",
        ]
    )
