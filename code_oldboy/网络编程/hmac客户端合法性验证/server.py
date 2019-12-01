'''
作者:lg
日期:2019/12/1
文件描述:
缺陷：
'''

import os
import socket
import hmac


def check_client(conn):
    secret_key = b'egg'  # 密钥
    send_str = os.urandom(32)
    conn.send(send_str)
    hmac_obj = hmac.new(secret_key, send_str)
    secret_ret = hmac_obj.digest()  # bytes类型
    if conn.recv(1024) == secret_ret:
        print('合法的客户端')
        return True
    else:
        print('非法的客户端')
        return False


sk = socket.socket()
sk.bind(('127.0.0.1', 8090))
sk.listen()

conn, addr = sk.accept()
ret = check_client(conn)
while ret:
    inp = input('>>>')
    conn.send(inp.encode('utf-8'))
    msg = conn.recv(1024)
    print(msg.decode('utf-8'))
conn.close()
sk.close()
