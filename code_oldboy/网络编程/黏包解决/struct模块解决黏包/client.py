'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket
import subprocess
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    cmd = sk.recv(1024).decode('utf-8').strip()
    if 'q' == cmd:
        break
    res = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE
                           )
    std_out = res.stdout.read()
    std_err = res.stderr.read()
    # 先把要发送的内容长度计算出来,发送过去
    length = len(std_out) + len(std_err)
    length = struct.pack('i', length)
    sk.send(length)

    # 再把内容发送过去,可多次发送,也可以一次行发送
    sk.send(std_out)
    sk.send(std_err)
sk.close()
