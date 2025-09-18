import tkinter as tk

import cc_functions as cc

# Função que será chamada quando clicar nos botões
def process(action):
    # Captura o texto digitado
    message = entry_text.get("1.0", tk.END).strip()

    # Captura o shift (com fallback para 3 se o usuário não digitar nada)
    try:
        shift = int(entry_shift.get())
    except ValueError:
        shift = 3

    # Decide se vai codificar ou decodificar
    if action == "E":
        result = cc.caesar_cipher(message, shift)
    elif action == "D":
        result = cc.caesar_cipher(message, -shift)
    else:
        result = "Action not supported"

    # Mostra o resultado na área de saída
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)

# ---------------- INTERFACE ----------------

root = tk.Tk()
root.title("Caesar Cipher")

# Caixa de texto para digitar a mensagem
tk.Label(root, text="Mensagem:").pack(anchor="w", padx=5, pady=2)
entry_text = tk.Text(root, height=5, width=40)
entry_text.pack(padx=5, pady=2)

# Campo para digitar o deslocamento (shift)
tk.Label(root, text="Shift:").pack(anchor="w", padx=5, pady=2)
entry_shift = tk.Entry(root)
entry_shift.insert(0, "3")  # valor padrão
entry_shift.pack(padx=5, pady=2)

# Botões para escolher a ação (E = Encrypt, D = Decrypt)
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="Codificar", command=lambda: process("E")).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Decodificar", command=lambda: process("D")).grid(row=0, column=1, padx=5)

# Área de saída para mostrar a mensagem final
tk.Label(root, text="Resultado:").pack(anchor="w", padx=5, pady=2)
output = tk.Text(root, height=5, width=40)
output.pack(padx=5, pady=5)

# Loop principal da interface
root.mainloop()