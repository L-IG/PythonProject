'''
作者:lg
日期:2019/11/20
文件描述:
缺陷：
'''


# python3新式类多继承顺序:
# 广度优先
# 1,大方向是从左到右,主要是对同一级的类
# 2,类的继承本质上是不停地向上找父类!!!!
# 如果能在后面继续找到当前的父类(例如父类A,必须有个关系??接下来要找的类的父类或者祖类也是A,不然就会错过这个类!!!!!),那么就先不找这个父类,后面再找.

# 2.7
# 新式类 继承object类的才是新式类 广度优先
# 经典类 如果你直接创建一个类在2.7中就是经典类 深度优先
# print(D.mro())
# D.mro()

# 单继承 ： 子类有的用子类 子类没有用父类
# 多继承中，我们子类的对象调用一个方法，默认是就近原则，找的顺序是什么？
# 经典类中 深度优先
# 新式类中 广度优先
# python2.7 新式类和经典类共存，新式类要继承object
# python3   只有新式类，默认继承object
# 经典类和新式类还有一个区别  mro方法只在新式类中存在
# super 只在python3中存在
# super的本质 ：不是单纯找父类 而是根据调用者的节点位置的广度优先顺序来的

# super用法举例(多继承,面试题)
class A(object):
    def func(self):
        print('A')


class B(A):
    def func(self):
        # 此时B类的super不是找A,而是根据调用者在节点中的广度优先顺序来找的
        # 注意是调用者!!!!
        # super是实时改变的!!!
        super().func()
        print('B')


class C(A):
    def func(self):
        super().func()
        print('C')


class D(B, C):
    def func(self):
        super().func()
        print('D')


d = D()
d.func()

# 单继承与多继承小结:
# 继承 ： 什么是什么的关系
# 单继承 *****
# 先抽象再继承，几个类之间的相同代码抽象出来，成为父类
# 子类自己没有的名字，就可以使用父类的方法和属性
# 如果子类自己有，一定是先用自己的
# 在类中使用self的时候，一定要看清楚self指向谁
# 多继承 ***
# 新式类和经典类：
# 多继承寻找名字的顺序 ： 新式类广度优先，经典类深度优先
# 新式类中 有一个类名.mro方法，查看广度优先的继承顺序
# python3中 有一个super方法，根据广度优先的继承顺序查找上一个类
