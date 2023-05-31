import socket
from conecao import conecao

conn = conecao()

# Criar um objeto de socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.SOCK_STREAM >  protocolo TCP


# Estabelecer conexão com o servidor
client_socket.connect((conn.host, conn.port))

# Enviar dados para o servidor
message = 'Olá, servidor!'
client_socket.send(message.encode())

# Receber a resposta do servidor
response = client_socket.recv(1024).decode()
print('Resposta do servidor:', response)

# Fechar a conexão com o servidor
client_socket.close()