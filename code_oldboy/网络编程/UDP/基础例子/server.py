'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))  # 即使udp是无连接的,udp服务端也必须起一个服务

msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
sk.sendto(b'bye', addr)

sk.close()