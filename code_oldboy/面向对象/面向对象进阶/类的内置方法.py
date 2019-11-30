'''
作者:lg
日期:2019/11/24
文件描述:
缺陷：
'''


class A(object):
    def __str__(self):
        # 规定必须返回一个字符串
        return '调用__str__'

    def __repr__(self):
        return '调用__repr__'


a = A()
print(str(a))
# 打印结果:<__main__.A object at 0x000001FCD88CE0F0>,是这个对象的内存地址
# 解析:当前类A中没有实现str方法,所有就去object中找,object会打印这个对象的内存地址
# 为什么int类的对象不会?
# 因为int类中实现了str方法
print(int.__str__)  # <slot wrapper '__str__' of 'int' objects>

l = [1, 2, 3]
print(l)  # [1, 2, 3]
# 列表类对str方法做了定制,不再打印一个内存地址了

print('----->%s' % (a))  # ----->HAHAHA


# %s str() 直接打印 三者都是调用str方法!!

# %s str() 直接打印 三者都是调用str方法!!
# %r repr()  实际上都是走的__repr__
# repr 是str的备胎，但str不能做repr的备胎

# print(obj)/'%s'%obj/str(obj)的时候，实际上是内部调用了obj.__str__方法，如果str方法有，那么他返回的必定是一个字符串
# 如果没有__str__方法，会先找本类中的__repr__方法，再没有再找父类中的__str__。
# repr(),只会找__repr__,如果没有找父类的

# 内置的方法有很多
# 不一定全都在object中
class Classes:
    def __init__(self, name):
        self.name = name
        self.student = []

    def __len__(self):
        # 这里有个很迷惑人的地方:方法里面在调用len方法为什么不会陷入循环?
        # 因为 len(self.student) 表示self.student在调用该方法,而不是这个类的对象去调用这个方法!!!
        return len(self.student)

    def __str__(self):
        return 'classes'


py_s9 = Classes('python全栈9期')
py_s9.student.append('二哥')
py_s9.student.append('泰哥')
print(len(py_s9))
print(py_s9)


# __del__
# 析构函数:并不是直接删除某个变量,而是在这个变量被删除前做一些收尾工作
# 哪些情况会删除这些变量?del方法,或者程序结束;
# 哪些收尾工作要做?删除文件句柄前,把文件给关了


# __call__
class A(object):
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        self.__init__(*args, **kwargs)
        print('__call__')


a = A()()
# 当一个对象实例化时,左边加括号a(),就是在调用父类的__call__方法
# 联想:类是一个对象,类实例化过程也是调用了父类的__call__方法,该方法里肯定调用了__init__方法

# 对象通过字典的形式去访问方法:
# __getitem__,__setitem__,__delitem__
dic = {'k': 'v'}
dic['k'] = 'v'


class Foo():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __delattr__(self, item):
        # del alex.name 点方式删除实际上通过这个方法
        print('__delattr__')
        # del self.__dict__[item]


alex = Foo('alex', 18, 'nan')
print(alex['name'])
alex['GG'] = 'gg'
print(alex['GG'])
del alex['GG']
del alex.name  # object 原生支持  __delattr__


# __init__ 初始化方法->给对象赋值
# __new__  构造方法 : 创建一个对象->self,分配内存空间的过程


class A(object):
    def __init__(self):
        print('in __init__')
        pass

    # 这里传入cls参数,因为此刻还没有self出现
    def __new__(cls, *args, **kwargs):
        print('in __new__')
        # 这里借助父类object类的new方法来为类A创建一个对象
        return object.__new__(A)


a1 = A()
a2 = A()
print(a1, a2)


# 设计模式
# 23种
# 单例模式
# 一个类 始终 只有 一个 实例
# 当你第一次实例化这个类的时候 就创建一个实例化的对象
# 当你之后再来实例化的时候 就用之前创建的对象

class AA(object):
    __isinstance = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance:
            cls.__isinstance = object.__new__(cls)
        return cls.__isinstance


a1 = AA('xiaoming', 20)
print(a1.__dict__)
a2 = AA('HeShuai', 19)
print(a1.__dict__)


# __eq__
class A(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


a1 = A('ming')
a3 = A('ming')
# 直接比较是内存地址比较,如果想比较属性,则必须重写__eq__方法
print(a1 == a3)  # False


# __hash__
class A():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        # 参数不能是数字
        return hash(self.name + str(self.age))


a1 = A('alex', 18)
a3 = A('alex', 18)
print(hash(a1))
print(hash(a3))
# -9223371909308636763
# 127546139014
# 继承object类的hash方法并不是准确的
# 需要重写


# 内置方法的进阶用法
from collections import namedtuple
import json
from random import choice
from random import shuffle

Card = namedtuple('Card', ['rank', 'suit'])


# 命名元组:创建一种只有属性,没有方法的类
# c = Card('2', '红心')
# print(c)


class FranchDerk(object):
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = ['红心', '方块', '梅花', '黑桃']

    def __init__(self):
        # 类里的静态属性必须借助类名才能访问
        self._cards = [Card(rank, suit) for rank in FranchDerk.ranks for suit in FranchDerk.suits]

    # 错误写法:字典是无序的,并不能通过下标去访问
    # def __getitem__(self, item):
    #     return self.__dict__[item]

    def __getitem__(self, item):
        return self._cards[item]

    # 打乱顺序需要这个方法,shuffle根据列表的下标来打乱
    def __setitem__(self, key, value):
        self._cards[key] = value

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return json.dumps(self._cards, ensure_ascii=False)


deck = FranchDerk()
print(deck[4])
# 抽牌
print(choice(deck))
# 洗牌
shuffle(deck)
print(deck)
print(deck[:5])


# 100个人,名字和性别一样,但是年龄不一样,需要做一个去重
class Person(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.sex == other.sex

    def __hash__(self):
        # return hash(self.name + self.sex)
        # 并不用实现hash的具体方法,只有有hash方法就可以
        return 1


p1 = Person('xiaoming', '男', 19)
p2 = Person('xiaoming', '男', 22)

# 无法直接用去重函数
# set对于对象来说,会直接用==号比较两边的值,需要重写eq函数
print(set((p1, p2)))
