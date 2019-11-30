class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

#属性必须是字符串
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
print(getattr(obj, 'x'))
#print(getattr(obj, 'y'))
setattr(obj, 'y', 20)
print(getattr(obj, 'y'))
print(getattr(obj, 'z', 1000))
print(getattr(obj, 'power'))
print(hasattr(obj, 'read'))