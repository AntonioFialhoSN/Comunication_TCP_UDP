import socket
from conecao import conecao

# informações do servidor
conn = conecao()


# Criar um objeto de socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.AF_INET > metodo para o ipv4
#socket.SOCK_DGRAM > socketd UDP

# Vincular o socket ao endereço e porta
server_socket.bind((conn.host, conn.port))
print('Servidor UDP esperando por mensagens...')


# Aguardar por mensagens do cliente
while True:
    message, client_address = server_socket.recvfrom(1024)
    print('Mensagem recebida do cliente:', message.decode())

    # Processar a mensagem recebida
    response = 'Olá, cliente! Recebi sua mensagem.'
    server_socket.sendto(response.encode(), client_address)