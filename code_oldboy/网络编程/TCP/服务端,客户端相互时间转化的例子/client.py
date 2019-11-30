'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket
import time

sk = socket.socket()  # 买手机
sk.connect(('127.0.0.1', 8080))  # 拨别人的号码
while True:
    current_time = time.time()
    current_time = str(current_time)
    sk.send(bytes(current_time, encoding='utf-8'))
    ret = sk.recv(1024).decode('utf-8')
    time.sleep(0.1)
sk.close()
