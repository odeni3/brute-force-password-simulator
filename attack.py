import tkinter as tk
from tkinter import messagebox
import random
import string
import threading
import time
import sys

caracteres = string.ascii_lowercase + string.digits  #letras minúsculas e dígitos
click_count = 0

def gerar_senha():
    """gera uma senha de 5 caractere."""
    return ''.join(random.choices(caracteres, k=5))

def atacar(senha_alvo, status_label):
    """simula um ataque de força bruta"""
    inicio_tempo = time.time()
    tentativas = 0
    while True:
        senha_gerada = gerar_senha()
        tentativas += 1
        if senha_gerada == senha_alvo:
            tempo_decorrido = time.time() - inicio_tempo
            messagebox.showinfo("Password Found", f'Password Found: {senha_gerada}\nAttempts required: {tentativas}\nElapsed time: {tempo_decorrido:.2f} seconds')
            break

def iniciar_ataque(senha_alvo):
    """inicia o ataque de força bruta."""
    global click_count 
    senha_alvo = senha_alvo.strip()
    if len(senha_alvo) != 5 or not senha_alvo.isalnum() or not senha_alvo.islower():
        messagebox.showerror("Error", "The target password must contain exactly 5 characters, all lowercase letters and/or digits.")
        return
    
    click_count += 1  
    click_count_label.config(text=f"Number of searches: {click_count}")
    
    entrada.config(state="disabled")
    
    t = threading.Thread(target=atacar, args=(senha_alvo, status_label))
    t.start()

    atualizar_temporizador(status_label)

def atualizar_temporizador(status_label):
    def update_timer():
        if ataque_em_andamento:
            tempo_decorrido = time.time() - inicio_tempo
            status_label.config(text=f"Looking for the password...\nElapsed time: {tempo_decorrido:.2f} seconds")
            status_label.after(1000, update_timer)

    global inicio_tempo
    global ataque_em_andamento
    inicio_tempo = time.time()
    ataque_em_andamento = True
    update_timer()

#janela principal
root = tk.Tk()
root.title("Brute force attack")

root.geometry("300x200")
root.resizable(False, False)

largura_janela = root.winfo_reqwidth()
altura_janela = root.winfo_reqheight()
posicao_x = int((root.winfo_screenwidth() / 2) - (largura_janela / 2))
posicao_y = int((root.winfo_screenheight() / 2) - (altura_janela / 2))
root.geometry(f"+{posicao_x}+{posicao_y}")

entrada_label = tk.Label(root, text="Target password:")
entrada = tk.Entry(root)
iniciar_button = tk.Button(root, text="Start Attack", command=lambda: iniciar_ataque(sys.argv[1]))
status_label = tk.Label(root, text="")
click_count_label = tk.Label(root, text=f"Number of searches: {click_count}")

entrada_label.pack()
entrada.pack()
iniciar_button.pack()
status_label.pack()
click_count_label.pack()

root.mainloop()
