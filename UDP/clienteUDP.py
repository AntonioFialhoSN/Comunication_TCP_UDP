#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 12345

int main() {
    struct sockaddr_in server_address;
    int client_socket, bytes_sent;
    char buffer[1024];

    // Criação do socket
    client_socket = socket(AF_INET, SOCK_DGRAM, 0);

    // Configuração do endereço do servidor
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = inet_addr("127.0.0.1");

    // Envio da mensagem para o servidor
    char message[] = "Olá, servidor!";
    sendto(client_socket, message, strlen(message), 0, (struct sockaddr*)&server_address, sizeof(server_address));

    // Recebimento da resposta do servidor
    bytes_sent = recvfrom(client_socket, buffer, sizeof(buffer), 0, NULL, NULL);
    buffer[bytes_sent] = '\0';
    printf("Resposta do servidor: %s\n", buffer);

    // Fechamento do socket
    close(client_socket);

    return 0;
}