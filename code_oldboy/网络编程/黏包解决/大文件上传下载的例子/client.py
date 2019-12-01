'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket
import subprocess
import struct
import hashlib

md5 = hashlib.md5()

FILE_NAME = 'client.mp4'

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

ret = sk.recv(4)
file_zie = struct.unpack('i', ret)[0]
current_size = file_zie

while True:
    if current_size <= 4096:
        content = sk.recv(current_size)
        with open(FILE_NAME, 'ab') as f:
            f.write(content)
            md5.update(content)
        break

    current_size -= 4096
    content = sk.recv(4096)
    with open(FILE_NAME, 'ab') as f:
        f.write(content)
        md5.update(content)

hash_num = md5.hexdigest()
ret = sk.recv(1024).decode('utf-8')
print('hash_num', ret)
sk.close()
