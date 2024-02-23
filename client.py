import socket

def enviar_senha(senha):
    HOST = 'IP do cliente'
    PORT = 'PORTA do cliente'      
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(senha.encode('utf-8'))

if __name__ == "__main__":
    senha = input("")
    enviar_senha(senha)
