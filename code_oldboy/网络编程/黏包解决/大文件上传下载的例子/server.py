'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket
import struct
import os
import hashlib

md5 = hashlib.md5()

FILE_NAME = 'server.mp4'
FILE_SIZE = os.path.getsize(FILE_NAME)  # 102348060
current_size = FILE_SIZE

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn, addr = sk.accept()

# 先发送文件总内容大小
length = struct.pack('i', FILE_SIZE)
conn.send(length)

# 分段发送文件内容
with open(FILE_NAME, 'rb') as f:
    while True:
        if current_size <= 4096:
            content = f.read(current_size)
            md5.update(content)
            conn.send(content)
            break

        current_size -= 4096
        content = f.read(4096)
        md5.update(content)
        conn.send(content)

hash_num = md5.hexdigest()
conn.send(bytes(str(hash_num), encoding='utf-8'))
print('hash_num', hash_num)
conn.close()
sk.close()
