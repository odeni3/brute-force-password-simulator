import socket
import subprocess
from time import sleep

def receber_senha():
    HOST = 'seu IP'
    PORT = 'sua PORTA'   
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Server listening on", HOST + ":" + str(PORT))
        conn, addr = server_socket.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                senha = data.decode('utf-8').strip()
                print("Received data.")
                sleep(2)
                iniciar_ataque(senha)

def iniciar_ataque(senha_alvo):

    senha_alvo = senha_alvo.strip()
    if len(senha_alvo) != 5 or not senha_alvo.isalnum() or not senha_alvo.islower():
        print("A senha alvo deve conter exatamente 5 caracteres, todos em letras minúsculas e/ou dígitos.")
        return
    
    subprocess.run(['python', 'attack.py', senha_alvo])

if __name__ == "__main__":
    receber_senha()
