import socket
sk = socket.socket()

sk.connect(('127.0.0.1',8080))


sk.send(b'hello')    #和别人说话，必须传一个byte类型，因为网流络只接受 二进制 形式

ret = sk.recv(1024)
print(ret)


sk.close()