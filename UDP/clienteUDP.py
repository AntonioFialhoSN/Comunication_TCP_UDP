import socket

# Definir informações do servidor
host = '192.168.0.37'  # Endereço IP do servidor
port = 12345       # Porta do servidor

# Criar um objeto de socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar uma mensagem para o servidor
message = 'Olá, servidor!'
client_socket.sendto(message.encode(), (host, port))

# Receber a resposta do servidor
response, server_address = client_socket.recvfrom(1024)
print('Resposta do servidor:', response.decode())

# Fechar o socket do cliente
client_socket.close()