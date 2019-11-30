class Student(object):
    def __init__(self, name):
        self.name = name#实例属性
    sex = '男' #类属性

stu1 = Student('xiaoming')
stu1.age = 19

s = Student('xiaohua')
print(s.sex)#实例属性继承了父类属性
print(Student.sex) #类属性
s.sex = '女'
print(s.sex)
print(Student.sex)#类属性依然可以通过类名称来访问
del s.sex
print(s.sex)