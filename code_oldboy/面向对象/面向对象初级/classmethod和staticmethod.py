'''
作者:lg
日期:2019/11/23
文件描述:
缺陷：
'''


# method 方法
# staticmathod  静态的方法 ***不依赖类,也不依赖对象,只是个普通方法
# classmethod   类方法    ****依赖类,需要通过类来调用
# 类的操作行为
class Good():
    __discount = 0.8

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * Good.__discount

    # 好处:把一个方法 变成一个类中的方法，这个方法就直接可以被类调用，不需要依托任何对象
    @classmethod
    def change_discount(cls):
        cls.__discount = 0.5


Good.change_discount()


# 当这个方法的操作只涉及静态属性的时候 就应该使用classmethod来装饰这个方法

# java
class Login:
    def __init__(self, name, password):
        self.name = name
        self.pwd = password

    def login(self): pass

    @staticmethod
    def get_usr_pwd():  # 静态方法
        usr = input('用户名 ：')
        pwd = input('密码 ：')
        Login(usr, pwd)


Login.get_usr_pwd()
# 在完全面向对象的程序中，
# 如果一个函数 既和对象没有关系 也和类没有关系 那么就用staticmethod将这个函数变成一个静态方法


# 类方法和静态方法 都是类调用的
# 对象可以调用类方法和静态方法么？   可以   一般情况下 推荐用类名调用
# 类方法 有一个默认参数 cls 代表这个类  cls
# 静态方法 没有默认的参数 就象函数一样
