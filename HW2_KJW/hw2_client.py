import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

# 이름 문자열로 송신
sock.send('김정우'.encode())

# 학번 수신
num = sock.recv(1024)
snum = int.from_bytes(num, 'big')
print(snum)

sock.close()
