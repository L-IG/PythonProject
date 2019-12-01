'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 避免重启的时候address already in use
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()

# ret1 = conn.recv(2).decode('utf-8')
# ret2 = conn.recv(10).decode('utf-8')
#
# print('ret1', ret1)  # he
# print('ret2', ret2)  # llo,boy


ret1 = conn.recv(20).decode('utf-8')
ret2 = conn.recv(3).decode('utf-8')
ret3 = conn.recv(1024).decode('utf-8')

print('ret1', ret1)
print('ret2', ret2)
print('ret3', ret3)

conn.close()
sk.close()
