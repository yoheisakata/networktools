import socket
import threading

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

host = '192.168.0.22'
port = 8080
bind_address = (host, port)

workers = 10

backlog_size = 10
recv_size = 1024


def handle(client_socket):
    remote_addr = client_socket.getpeername()
    
    print('[{}] {} - handle connection, start - {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), threading.current_thread().getName(), remote_addr))
    
    with client_socket:
        while True:
            data = client_socket.recv(recv_size)

            if not data:
                break

            client_socket.send(b'Reply: ' + data)

    print('[{}] {} - handle connection, exit - {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), threading.current_thread().getName(), remote_addr))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    with ThreadPoolExecutor(max_workers = workers) as executor:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(bind_address)
        server_socket.listen(backlog_size)

        print('[{}] Server startup, thread-pool = {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), workers))

        try:
            while True:
                client_socket, addr = server_socket.accept()
                executor.submit(handle, client_socket)
        except KeyboardInterrupt:
            print('[{}] Server stop'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))