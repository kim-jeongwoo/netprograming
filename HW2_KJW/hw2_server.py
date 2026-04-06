import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    
    # 이름 수신
    name = client.recv(1024)
    print(name.decode())

    # 학번 송신
    num = 20211526
    client.send(num.to_bytes(4, 'big'))

    client.close