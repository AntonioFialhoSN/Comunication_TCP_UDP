import socket

# Definir informações do servidor
host = '192.168.0.37'  # Endereço IP do servidor
port = 12345       # Porta para escutar as conexões

# Criar um objeto de socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular o socket ao endereço e porta
server_socket.bind((host, port))

# Colocar o socket em modo de escuta
server_socket.listen(1)
print('Servidor TCP esperando por conexões...')

# Aguardar por uma conexão do cliente
client_socket, client_address = server_socket.accept()

print('Conexão estabelecida com', client_address)

# Receber dados do cliente
data = client_socket.recv(1024).decode()
print('Dados recebidos do cliente:', data)

# Enviar uma resposta ao cliente
response = 'Olá, cliente! Recebi sua mensagem.'
client_socket.send(response.encode())

# Fechar a conexão com o cliente
client_socket.close()

# Fechar o socket do servidor
server_socket.close()