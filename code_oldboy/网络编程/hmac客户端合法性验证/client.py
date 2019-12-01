'''
作者:lg
日期:2019/12/1
文件描述:
缺陷：
'''

import socket
import hmac
sk = socket.socket()
sk.connect(('127.0.0.1',8090))

recv = sk.recv(1024)
# 用和server端相同的手法对这个字符串进行摘要
secret_key = b'egg'  # 密钥
hmac_obj = hmac.new(secret_key,recv)
ret = hmac_obj.digest()
sk.send(ret)
msg = sk.recv(1024)
if msg:
    print(msg.decode('utf-8'))
    while True:
        inp = input('>>>')
        sk.send(inp.encode('utf-8'))
        msg = sk.recv(1024)
        print(msg.decode('utf-8'))
sk.close()