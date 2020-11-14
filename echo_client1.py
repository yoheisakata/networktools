# Echo Client Program

import socket 

HOST = '192.168.0.21'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    while True:
        data = s.recv(2)
        print('leng', len(data))
        print('Received', data)
        if not data: break
    print('DONE')
    s.close()
  
