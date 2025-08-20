import tkinter as tk
from tkinter import ttk

from repository.produto_repository import ProdutoRepository


bd = ProdutoRepository()
root = tk.Tk()
root.title("Gerenciador de Produtos")


tree = ttk.Treeview(root, columns=("Codigo", "Nome", "Preço"), show="headings")
tree.heading("Codigo", text="Codigo")
tree.heading("Nome", text="Nome")
tree.heading("Preço", text="Preço")
tree.pack()


def carregar_dados():
    registros = bd.get_all()
    for registro in registros:
        tree.insert(
            "",
            "end",
            values=[registro.codigo, registro.nome, f"R$ {registro.preco}"],
        )


carregar_dados()

root.mainloop()
