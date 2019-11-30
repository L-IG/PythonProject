'''
作者:lg
日期:2019/11/30
文件描述:手机客户端,需要的时候向服务器请一个标准的时间
缺陷：
'''
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)

format_str = '%Y-%m-%d %H:%M:%S'.encode('utf-8')

sk.sendto(format_str, ip_port)
msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
