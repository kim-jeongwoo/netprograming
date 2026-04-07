import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2021))

while True:
    msg = input('계산기(ex. 정수 + 정수): ')
    if msg == 'q':
        break

    sock.send(msg.encode())
    result = sock.recv(1024)
    # print(f'{int.from_bytes(result, 'big'):.1f}')
    print(result.decode())

sock.close()