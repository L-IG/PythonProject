f = open('hello.txt','rb+')
f.seek(3,0)
f.write(b'777')
f.seek(3,1)
f.write(b'88888')
f.seek(0,2)
f.write(b'22222222')