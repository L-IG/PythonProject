'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket

sk = socket.socket()  # 买手机
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 避免重启的时候address already in use
sk.bind(('127.0.0.1', 8080))  # 绑定手机卡

sk.listen()  # 监听,等待别人给我打电话

conn, addr = sk.accept()  # 接收到别人的电话,coon:表示一个连接,addr:来电显示,对方的号码
while True:
    ret = conn.recv(1024).decode('utf-8')
    print(ret)
    if ret == 'bye':
        conn.send(b'bye')
        break
    user_input = input('>>>').encode('utf-8')
    conn.send(user_input)

conn.close()  # 挂电话
sk.close()  # 关手机
