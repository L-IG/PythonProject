class Foo():

    name = 'xiaoming'

    def __init__(self,age):
        self.age = age

s1 = Foo(18)

print(s1.age)

print(s1.__dict__)

# s1.name = 'hhh'
# print(s1.__dict__)

del s1.name
print(s1.__dict__)