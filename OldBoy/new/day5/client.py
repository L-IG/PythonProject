import socket
port = 7024
sk = socket.socket()
sk.connect(('127.0.0.1',port))

while True:
    msg = input('>>>')
    sk.send(msg.encode('utf-8'))
    if 'q' == msg:
        break
    info = sk.recv(1024).decode('utf-8')
    print(info)

sk.close()