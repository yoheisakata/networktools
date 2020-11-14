import socket

def send_msg(sock, msg):

    total_sent_len = 0
    total_msg_len = len(msg)

    while total_sent_len < total_msg_len:

        sent_len = sock.send(msg[total_sent_len:])
        print(sent_len)

        if sent_len == 0:
            raise RuntimeError('socket connection broken')

        total_sent_len += sent_len

def recv_msg(sock, chunk_len=1024):
    while True:
        received_chunk = sock.recv(chunk_len)
        print(received_chunk)

        if len(received_chunk) == 0:
            break
        yield received_chunk

def main():

    # IPv4 / TCP
    # AF_INET = IPv4
    # SOCK_STREAM = TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to loopback TCP/80
    client_socket.connect(('192.168.0.60', 50007))

    request_text = 'GET /HTTP/1.0\r\n\r\n'

    request_bytes = request_text.encode('ASCII')

    send_msg(client_socket, request_bytes)

    received_bytes = b''.join(recv_msg(client_socket))

    received_text = received_bytes.decode('ASCII')

    #print(received_text)

    client_socket.close()

    

if __name__ == '__main__':
    main()
