# Echo Server Program
import socket 

HOST = ''
PORT = 12345
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(f'{HOST} and {PORT} are used')
    s.listen(1)
    print(f'Started listening.')
    conn, addr = s.accept()
    print ('Connected by', addr)
    with conn:
        while True:
            data = conn.recv(4)
            print (f'Received {data}')
            if not data:
                break
            print (f'Sent {data}')
            conn.sendall(data)

