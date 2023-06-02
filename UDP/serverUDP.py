import socket

# Definir informações do servidor
host = '192.168.0.37'  # Endereço IP do servidor
port = 12345       # Porta para escutar as mensagens

# Criar um objeto de socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o socket ao endereço e porta
server_socket.bind((host, port))

print('Servidor UDP esperando por mensagens...')

# Aguardar por mensagens do cliente
while True:
    message, client_address = server_socket.recvfrom(1024)
    print('Mensagem recebida do cliente:', message.decode())

    # Processar a mensagem recebida
    response = 'Olá, cliente! Recebi sua mensagem.'
    server_socket.sendto(response.encode(), client_address)