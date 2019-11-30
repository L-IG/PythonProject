'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket

sk = socket.socket()# 买手机
sk.connect(('127.0.0.1', 8080))# 拨别人的号码
sk.send(b'Hi')
ret = sk.recv(1024)
print(ret)

sk.close()