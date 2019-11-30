#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加

class Student(object):
    count = 0
    count = count + 1#类属性只初始化一次，以后再也不执行了
    def __init__(self, name): #而init方法，每次创建一个新实例都会调用此方法
        self.name = name

stu1 = Student('xiaoming')
stu2 = Student("xiaohua")
stu3 = Student("huahua")
