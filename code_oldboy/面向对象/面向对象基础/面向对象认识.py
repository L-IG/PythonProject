'''
作者:lg
日期:2019/11/2
文件描述:
缺陷：
'''


class Person():
    country = 'CHINA'

    def __init__(self, name, age, hp):
        print(self.__dict__)  # {}
        self.name = name
        self.age = age
        self.hp = hp
        print(self.__dict__)  # {'name': 'alex', 'age': 18, 'hp': 100}

    def walk(self):
        print('hello', self)


alex = Person('alex', 18, 100)

# 对象初始化的过程:

# 类名() 首先会创建一个self空字典,
# 调用__init__方法,类名里的参数会被这里接受,
# 执行__init__方法
# 返回self对象


# 类方法:
# 类名调用方法与对象调用方法的区别:
# 类名调用必须传一个参数,这个参数可以是任意值
# 对象调用方法默认把对象自己传进去了,不用写了
Person.walk('world!')
alex.walk()

# 每一个对象都有属于自己的数据属性,类也有自己的数据属性
# 方法属性是放在类里面的,每一个对象都可以去使用类的方法,但是对象不是存储方法属性的地方(节省空间)!!!

# 对象能做的事：
#   查看属性
#   调用方法
#   __dict__ 对于对象的增删改查操作都可以通过字典的语法进行

# 类名能做的事：
#   实例化
#   调用方法 : 只不过要自己传递self参数
#   调用类中的属性,也就是调用静态属性
#   __dict__ 对于类中的名字只能看 不能操作!!!!!

pipe = Person('alex', 18, 100)
print(Person.__dict__)
print(pipe.__dict__)

# 类属性字典不支持修改,只允许查看!!!
# Person.__dict__['a'] = 'a'  TypeError: 'mappingproxy' object does not support item assignment

