'''
作者:lg
日期:2019/11/18
文件描述:
缺陷：
'''


# class A(object):pass   # 父类，基类，超类
# class B:pass   # 父类，基类，超类
# class A_son(A,B):pass # 子类，派生类
# class AB_son(A):pass # 子类，派生类
# 一个类 可以被多个类继承
# 一个类 可以继承多个父类  —— python里
# print(A_son.__bases__)
# print(AB_son.__bases__)
# print(A.__bases__)  # python3 -新式类# 没有继承父类默认继承object
# class Animal:
#     def __init__(self,name,aggr,hp):
#         self.name = name
#         self.aggr = aggr
#         self.hp = hp
#         self.func()
#     def func(self):
#         print(123)
# #
# class Dog(Animal):
#     def func(self):
#         print(456)
#     def bite(self,person):
#         person.hp -= self.aggr
# d = Dog()

class Animal(object):
    def __init__(self, name, aggr, hp):
        print('in Animal')
        self.name = name
        self.aggr = aggr
        self.hp = hp

        self.eat()

    def eat(self):
        print('Animal eat!')


class Dog(Animal):
    # 注意:在init之前就已经创建了空字典self
    def eat(self):
        print('Dog eat!')


class Jin(Animal):
    pass


alex = Dog('alex', 100, 1000)


# 1,实例化时会执行__init__方法
# 2,在自己类里面没找到_init__方法,就会去父类里面去找,找到了就执行

# print(alex.name)


class Animal(object):
    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp

    def eat(self):
        self.hp += 100


class Person(Animal):
    def __init__(self, name, aggr, hp, sex):
        super().__init__(name, aggr, hp)
        super(Person, self).__init__(name, aggr, hp)
        # super也是指向自己的父类,默认传递(类名,类的对象)两个参数,在类里面也可以不传递
        self.sex = sex  # 派生属性


class Dog(Animal):
    def __init__(self, name, aggr, hp, kind):
        Animal.__init__(self, name, aggr, hp)
        self.kind = kind  # 派生属性

    def eat(self):  # 派生方法
        Animal.eat(self)
        self.teeth = 2


jin = Dog('Jin', 100, 100, '狗子')
print(jin.name)

# 父类中没有的属性 在子类中出现 叫做派生属性
# 父类中没有的方法 在子类中出现 叫做派生方法
# 只要是子类的对象调用，子类中有的名字 一定用子类的，子类中没有才找父类的，如果父类也没有报错
# 如果父类 子类都有 用子类的
# 如果还想用父类的，单独调用父类的:
#       父类名.方法名 需要自己传self参数(这个self参数是属于当前类创建的)
#       super().方法名 不需要自己传self
# super也是指向自己的父类,默认传递(类名,类的对象)两个参数,在类里面也可以不传递
super(Dog, jin)
# super也可以在类外面使用,但是需要写名类名与对象

# 组合与继承的区别:
# 有 和 是
# 相似代码,功能



