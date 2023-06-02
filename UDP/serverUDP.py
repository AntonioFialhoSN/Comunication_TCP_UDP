#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 12345

int main() {
    struct sockaddr_in server_address, client_address;
    int server_socket, bytes_received, client_address_length;
    char buffer[1024];

    // Criação do socket
    server_socket = socket(AF_INET, SOCK_DGRAM, 0);

    // Configuração do endereço do servidor
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = INADDR_ANY;

    // Vinculação do socket ao endereço e porta
    bind(server_socket, (struct sockaddr*)&server_address, sizeof(server_address));

    printf("Servidor UDP esperando por mensagens...\n");

    while (1) {
        // Recebimento da mensagem do cliente
        client_address_length = sizeof(client_address);
        bytes_received = recvfrom(server_socket, buffer, sizeof(buffer), 0, (struct sockaddr*)&client_address, &client_address_length);
        buffer[bytes_received] = '\0';
        printf("Mensagem recebida do cliente: %s\n", buffer);

        // Processamento da mensagem recebida
        char response[] = "Olá, cliente! Recebi sua mensagem.";
        sendto(server_socket, response, strlen(response), 0, (struct sockaddr*)&client_address, sizeof(client_address));
    }

    // Fechamento do socket
    close(server_socket);

    return 0;
}