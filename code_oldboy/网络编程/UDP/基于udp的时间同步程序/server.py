'''
作者:lg
日期:2019/11/30
文件描述:服务器程序,负责把时间发给手机客户端
缺陷：
'''

import socket
import time
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))  # 即使udp是无连接的,udp服务端也必须起一个服务

msg, addr = sk.recvfrom(1024)
msg = msg.decode('utf-8')
t = time.strftime(msg).encode('utf-8')
print(t)

sk.sendto(t, addr)

sk.close()