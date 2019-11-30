'''
作者:lg
日期:2019/11/23
文件描述:
缺陷：
'''


# property
# 内置装饰器函数 只在面向对象中使用
# 最常见用法:伪装,方法变属性,
# 通常是通过计算的'值',看起来更合理
class Room():
    def __init__(self, width, lenth):
        self.__width = width
        self.__lenth = lenth

    @property
    def area(self):
        return self.__width * self.__lenth


r = Room(100, 100)
print(r.area)


# 被property装饰的新属性area支持被修改!!


# 进阶用法:property和私有属性一起用
# 好处:通过property访问私有属性,别人调用起来像是直接访问的,其实是经过封装的

class Person():
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


p = Person('alex')
# 这里本质还是调用'类的方法'而不是访问'对象的属性'!
print(p.name)

# 赋值语句会触发@name.setter方法,并不是真正去修改对象属性
p.name = 'Jin'


# 一个应用:保护原有的属性,把原有的属性经过别的操作修改后公开出来
class Good():
    discount = 0.8

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * Good.discount

    @price.deleter
    def price(self):
        del self.__price


g = Good('apple', 5)
print(g.price)

# 自动触发@price.deleter方法,因为price本质是方法属性,对象没有权限去删除类里面的方法的!
del g.price
