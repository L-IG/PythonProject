'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()
while True:
    cmd = input('cmd:').strip()
    conn.send(bytes(cmd, encoding='utf-8'))
    if 'q' == cmd:
        conn.send(b'q')
        break
    # 先接受发送端即将要发送多大的数字
    ret = conn.recv(1024)
    length = struct.unpack('i',ret)[0]

    # 根据接来的数字来决定接受多少内容
    ret = conn.recv(length).decode('gbk')
    print(ret)

conn.close()
sk.close()
