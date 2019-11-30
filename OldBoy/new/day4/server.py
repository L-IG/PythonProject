import  socket
sk = socket.socket()           #创建一个对象  买手机
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT)
sk.bind(('127.0.0.1',8080))    #绑定手机卡  公布手机号码
sk.listen()                     #监听

conn, addr = sk.accept()      #接到别人的电话后   conn：电话连接 addr：别人的电话地址

ret = conn.recv(1024)         #和别人说话，必须传一个byte类型，因为网流络只接受 二进制 形式
print(ret)

conn.send(b'Hi')

conn.close()               #挂电话，关掉这个连接
sk.close()                 #关手机


