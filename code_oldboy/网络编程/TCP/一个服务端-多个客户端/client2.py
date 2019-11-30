'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket

sk = socket.socket()  # 买手机
sk.connect(('127.0.0.1', 8080))  # 拨别人的号码
while True:
    user_input = input('client2>>>').encode('utf-8')
    sk.send(user_input)
    ret = sk.recv(1024).decode('utf-8')
    print(ret)
    if ret == 'bye':
        # sk.send(b'bye')
        break
sk.close()
