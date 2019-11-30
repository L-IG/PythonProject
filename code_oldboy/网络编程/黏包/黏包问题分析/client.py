'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

import socket

sk = socket.socket()  # 买手机
sk.connect(('127.0.0.1', 8080))

# 第一种情况:发的内容多于收的内容
# sk.send(b'hello,boy')


# 第二种情况:发的内容少于收的内容
# 每次发的内容少于收的内容
sk.send(b'hello,boy')
sk.send(b'hello,boy')
sk.send(b'hello,boy')
sk.send(b'hello,boy')
sk.send(b'hello,boy')
sk.send(b'hello,boy')
sk.send(b'hello,boy')
# 打印结果:
# ret1 hello,boyhello,boyhello,boyhello,boyhello,boyhello,boyhello,boy
# ret2
# ret3
# 因为recv要收的内容很多(1024),而每次发的内容又没这么多,所以直到缓存里存够了1024个字节后才会被recv到!!!
sk.close()

