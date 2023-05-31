import socket

# Definir informações do servidor
host = '192.168.0.37'  # Endereço IP do servidor
port = 12345       # Porta do servidor

# Criar um objeto de socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelecer conexão com o servidor
client_socket.connect((host, port))

# Enviar dados para o servidor
message = 'Olá, servidor!'
client_socket.send(message.encode())

# Receber a resposta do servidor
response = client_socket.recv(1024).decode()
print('Resposta do servidor:', response)

# Fechar a conexão com o servidor
client_socket.close()