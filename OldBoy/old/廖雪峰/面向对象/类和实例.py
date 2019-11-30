class Student(object):
    def __init__(self, a, b):
        self.name = a
        self.score = b

    def print_score(self):
        print('%s %s' % (self.name,self.score))

def out_print_score(std):
    print('%s %s' % (std.name, std.score))

student1 = Student('xiaoming', 80)

student2 = Student('zhangna', 90)

student1.print_score()
student2.print_score()
print(student1) #有一个具体的地址，是实实在在存在的
print(Student)#没有具体的地址，只是一个抽象

#实例可以自由的绑定一个属性，数据
student1.age = 20

print('-------')
out_print_score(student1) #外部也能访问类的属性

