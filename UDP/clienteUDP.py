import socket
from conecao import conecao

# informações do servidor
conn = conecao()


# Criar um objeto de socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.AF_INET > metodo para o ipv4
#socket.SOCK_DGRAM > socketd UDP


# Enviar uma mensagem para o servidor
message = 'Olá, servidor!'
client_socket.sendto(message.encode(), (conn.host, conn.port))

# Receber a resposta do servidor
response, server_address = client_socket.recvfrom(1024)
print('Resposta do servidor:', response.decode())

# Fechar o socket do cliente
client_socket.close()