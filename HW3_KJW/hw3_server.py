import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2021))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    while True:
        data = client.recv(1024)
        if data == 'q':
            break

        cal = data.decode()
        parts = cal.split()
        if parts[1] == '+':
            result = int(parts[0]) + int(parts[2])
        elif parts[1] == '-':
            result = int(parts[0]) - int(parts[2])
        elif parts[1] == '*':
            result = int(parts[0]) * int(parts[2])
        elif parts[1] == '/':
            result = int(parts[0]) / int(parts[2])
        
        result2 = (f'{result:.1f}')
        # client.send(result.to_bytes(4, 'big'))
        client.send(result2.encode())
    client.close()
s.close()