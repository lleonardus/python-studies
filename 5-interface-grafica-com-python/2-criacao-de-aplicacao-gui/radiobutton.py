import tkinter as tk
from tkinter import messagebox


def submit_callback():
    nome = nome_entry.get()
    email = email_entry.get()
    linguagem_preferida = linguagem_var.get()

    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Linguagem Preferida: {linguagem_preferida}")

    messagebox.showinfo(
        title="Dados Submetidos",
        message=f"Nome: {nome}\nEmail: {email}\nLinguagem Preferida: {linguagem_preferida}",
    )


root = tk.Tk()
root.title("Formulário de Inscrição")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)
nome_label = tk.Label(frame, text="Nome:")
nome_label.grid(row=0, column=0, sticky="e")

email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)
email_label = tk.Label(frame, text="Email:")
email_label.grid(row=1, column=0, sticky="e")

# Variável para armazenar a escolha de linguagem
linguagem_var = tk.StringVar(value="Python")

python_radio = tk.Radiobutton(
    frame, text="Python", variable=linguagem_var, value="Python"
)
python_radio.grid(row=2, column=0)


java_radio = tk.Radiobutton(frame, text="Java", variable=linguagem_var, value="Java")
java_radio.grid(row=2, column=1)


submit_button = tk.Button(frame, text="Submeter", command=submit_callback)
submit_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
