'''
作者:lg
日期:2019/12/17
文件描述:
缺陷：
'''

# web框架本质
# 与CS架构不同,浏览器与服务器形成了BS架构,浏览器就是客户端
# 用到的网络传输原理也是socket

# 我们可以这样理解：所有的Web应用本质上就是一个socket服务端，而用户的浏览器就是一个socket客户端。 这样我们就可以自己实现Web框架了。
# 浏览器发请求 --> HTTP协议 --> 服务端接收请求 --> 服务端返回响应 --> 服务端把HTML文件内容发给浏览器 --> 浏览器渲染页面

import socket

sk = socket.socket()

sk.bind(("127.0.0.1", 8080))
sk.listen(5)

conn, addr = sk.accept()
ret = conn.recv(1024)
conn.send(b'HTTP/1.1 200 OK\r\n\r\n')

conn.send(b'<h1>Hello World!</h1>')
conn.close()
