import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    client, addr = s.accept()

    data = client.recv(1024)
    msg = data.decode()
    req = msg.split()[1].replace('/', '')
    
    if req == 'index.html':
        f = open(req, 'r', encoding='utf-8')
        mimeType = 'text/html; charset=utf-8'
        
        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        client.send(b'\r\n')
        data = f.read()
        client.send(data.encode())

    elif req == 'iot.png':
        f = open(req, 'rb')
        mimeType = 'image/png'

        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        client.send(b'\r\n')
        data = f.read()
        client.send(data)

    elif req == 'favicon.ico':
        f = open(req, 'rb')
        mimeType = 'image/x-icon'

        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        client.send(b'\r\n')
        data = f.read()
        client.send(data)

    else:
        client.send(b'HTTP/1.1 404 Not Found\r\n')
        client.send(b'\r\n')
        client.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        client.send(b'<BODY>Not Found</BODY></HTML>')
    client.close()