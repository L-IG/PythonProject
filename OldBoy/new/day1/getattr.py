class Student(object):
    def __init__(self,name):
        self.name = name

    def __getattr__(self, item):
        print("not exsit")

stu1 = Student('xiaoming')
print(stu1.name)