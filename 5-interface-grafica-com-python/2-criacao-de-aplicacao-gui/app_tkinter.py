import tkinter as tk


def submit() -> None:
    nome = nome_entry.get()
    email = email_entry.get()

    print(f"Nome: {nome}")
    print(f"Email: {email}")


# Cria janela principal
root = tk.Tk()
root.title("Formulário de Inscrição")

# Cria um frame para conter os widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Campos de entrada

nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

# Button para submit

submit_button = tk.Button(frame, text="Submeter", command=submit)
submit_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()
