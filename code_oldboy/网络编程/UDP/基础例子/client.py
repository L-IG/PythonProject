'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)
sk.sendto(b'hello', ip_port)
msg,addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))