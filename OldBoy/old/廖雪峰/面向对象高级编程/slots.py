from types import MethodType
def set_age(self, age):
    self.age = age
    print(self.age())

class Student(object):
    pass

def set_age(self, age):
    self.age = age
    print(self.age)


class Animal(object):
    __slots__ = ('name', 'age')

class SmallAnimal(Animal):
    __slots__ = ('height', 'sex')

stu1 = Student()
stu1.name = 'xiaoming'
print(stu1.name)
stu2 = Student()

#给student 创建一个方法，但这里不是在class中创建而是创建了一个链接把外部的set_age 方法用链接到Student内
#给实例绑定一个方法,对其他实例不起作用
#只有当方法在class中，其他实例才能共享此方法
stu1.set_age = MethodType(set_age, stu1)
stu1.set_age(100)
#stu2.set_age(19)

a = Animal()
a.name = 'qq'
a.age = 8
#a.sex = 'nan'

b = SmallAnimal()
b.sex = 'nv'
b.age = 10






