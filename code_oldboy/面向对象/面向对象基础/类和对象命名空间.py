'''
作者:lg
日期:2019/11/2
文件描述:
缺陷：
'''


class Course():
    language = 'Chinese'
    hobbies = ['pingpong']

    def __init__(self, teacher, course, period):
        self.teacher = teacher
        self.course = course
        self.period = period

    def func(self):
        pass


py = Course('egon', 'python', '6 months')
go = Course('alex', 'go', '1 month')

# Course 类命名空间:
# language
# __init__
# func

# py 对象命名空间:
# 类对象指针,这个该对象指向创建它的类,并且是单线联系,从对象可以找到类,从类找不到对象!!!
# 通过类创建的对象是兄弟关系,所有对象共享类命名空间的属性和方法
# teacher
# course
# period

# 对象的一个特性:当通过对象访问某个属性,如果对象命名空间里没有,就会去类命名空间里找!!!!!

py.language = 'English'
# 对于不可变的属性
# 无法通过对象去修改类的静态属性,这个语句实际上是为对象自己创建一个属性
# 并且以后对象只能访问自己的属性,而不能去访问类的属性,因为对象在自己空间找到了就不会去类里面找

# 对于可变属性,如列表,字典
# 可以通过对象去修改
# 原因分析:类静态属性是一个内存地址,该地址是没变的,但是它指向的内存空间里的值变了
go.hobbies[0] = 'basketball'
print(Course.__dict__)  # 'hobbies': ['basketball']


# 模拟人生举例
class person():
    money = 0

    def work(self):
        person.money += 1000


mother = person()
father = person()
mother.work()
father.work()
print(person.__dict__['money'])


# 创建一个类,每实例化一个对象就计数
# 最终所有的对象共享这个数据

class Foo():
    count = 0

    def __init__(self):
        Foo.count += 1


f1 = Foo()
f2 = Foo()
f3 = Foo()
print(Foo.count)


# 绑定方法
def func(): pass


class F():
    def func(self):
        pass


f = F()
print(func)
print(F.func)
print(f.func)

# 普通函数:
# <function func at 0x00000235B588F158>
# 类方法:
# <function F.func at 0x00000235B588F488>
# f对象的绑定方法:
# <bound method F.func of <__main__.F object at 0x00000235B58994A8>>

# 当对象调用类里面的方法,即方法和对象绑定了(有self参数的那个)


# 联想包的导入原理:
# 导入包时类似于类的实例化过程,产生一个对象
# 执行包里面的__init__文件
# import time
# time.time()
# 模块的调用,类似于对象实例化,对象调用类方法
