'''
作者:lg
日期:2019/11/22
文件描述:
缺陷：
'''

# 概念来源:
# java ： 面向对象编程
# 设计模式   —— 接口
# 接口类 ： python原生不支持
# 抽象类 ： python原生支持的
# 在python里这两个很类似,在其他语言里则有区别
from abc import abstractmethod, ABCMeta  # 元类 默认的元类 type


class Pay_Ment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass
        # raise NotImplemented


class Wechat(Pay_Ment):
    def pay(self, money):
        print(f'用Wechat付了{money}元钱')


class Ali(Pay_Ment):
    def pay(self, money):
        print(f'用Ali付了{money}元钱')


class QQpay(Pay_Ment):
    def pay(self, money):
        print(f'用QQpay付了{money}元钱')


def pay(obj, money):
    obj.pay(money)


# w1 = Wechat()
# a1 = Ali()
q1 = QQpay()


# pay(w1, 100)
# pay(q1, 100)


# 规范 ：接口类或者抽象类都可以
# 接口类 支持多继承，接口类中的所有的方法都必须不能实现 —— java
# 抽象类 不支持多继承，抽象类中方法可以有一些代码的实现 —— java
# 其实主要目的都是'规范'程序员写代码!!


# 接口类的多继承
# 举例:
class Animal_walk(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class Animal_swim(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class Animal_fly(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Bird(Animal_fly, Animal_walk):
    # 继承了接口类,那么就必须实现接口类里面的方法
    def fly(self):
        pass

    def walk(self):
        pass


class Duck(Animal_swim, Animal_walk):
    # 继承了接口类,那么就必须实现接口类里面的方法
    pass


b = Bird()


# 接口类  刚好满足接口隔离原则 面向对象开发的思想 规范


# 抽象类
# 举例:一切皆文件的思想
class All_file(metaclass=ABCMeta):
    @abstractmethod
    def write(self):  # 定义抽象方法，无需实现功能
        pass

    @abstractmethod
    def read(self):  # 定义抽象方法，无需实现功能
        pass


class Txt(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def write(self):
        pass

    def read(self):
        pass


class Sata(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def write(self):
        pass

    def read(self):
        pass


class Process(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def write(self):
        pass

    def read(self):
        pass


t = Txt()
s = Sata()
p = Process()
t.read()
s.read()
p.read()

# 抽象类 ： 规范
# 一般情况下 单继承 能实现的功能都是一样的，所以在父类中可以有一些简单的基础实现
# 多继承的情况 由于功能比较复杂，所以不容易抽象出相同的功能的具体实现写在父类中


# 抽象类还是接口类 ： 面向对象的开发规范 所有的接口类和抽象类都不能实例化
# java ：
# java里的所有类的继承都是单继承,所以抽象类完美的解决了单继承需求中的规范问题
# 但对于多继承的需求，由于java本身语法的不支持，所以创建了接口Interface这个概念来解决多继承的规范问题

# python
# python中没有接口类  ：
#  python中自带多继承 所以我们直接用class来实现了接口类
# python中支持抽象类  ： 一般情况下 单继承  不能实例化
#  且可以实现python代码

# 相似点:不管是接口类和抽象类都是一种规范化,继承了接口类或者抽象类就必须实现父类里面的方法:
# 不同点:接口类相当于java里面没有多继承用的interface,用作多继承,而抽象类一般用作单继承
