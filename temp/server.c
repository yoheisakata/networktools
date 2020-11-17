#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main()
{

    int sock0;
    struct sockaddr_in addr;
    struct sockaddr_in client;
    int len;
    int count = 1;

    /* ソケットの作成 */
    sock0 = socket(AF_INET, SOCK_STREAM, 0);

    /* ソケットの設定 */
    addr.sin_family = AF_INET;
    addr.sin_port = htons(12345);
    addr.sin_addr.s_addr = INADDR_ANY;
    bind(sock0, (struct sockaddr *)&addr, sizeof(addr));

    /* TCPクライアントからの接続要求を待てる状態にする */
    listen(sock0, 5);

    /* allow connection for 4 times */
    while (count < 5)
    {
        printf("%d\n", count);
        /* TCPクライアントからの接続要求を受け付ける */
        len = sizeof(client);
        int sock = accept(sock0, (struct sockaddr *)&client, &len);

        /* 5文字送信 */
        write(sock, "HELLO", 5);

        /* TCPセッションの終了 */
        close(sock);
        printf("Socket %d closed\n", count);
        count++;
    }
    /* listen するsocketの終了 */
    close(sock0);
    
    return 0;
}
