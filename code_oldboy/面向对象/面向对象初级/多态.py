'''
作者:lg
日期:2019/11/23
文件描述:
缺陷：
'''


class Pay_Ment():
    def pay(self, money):
        pass


class Wechat(Pay_Ment):
    def pay(self, money):
        print(f'用Wechat付了{money}元钱')


class Ali(Pay_Ment):
    def pay(self, money):
        print(f'用Ali付了{money}元钱')

# 对应其他类型的语言,需要通过继承同一个父类来让数据类型保持相同!!
# def pay(Pay_Ment obj, int money):
# obj.pay(money)

# 多态:表示一个事务的多种形态,动物有鸟,人,老虎等多种形态,文件有word文档,程序,进程等多种形态


# 强类型语言  多态
# 比如java,想要用多个不同类型的对象想要调用同一个方法,因为强类型语言的限制,所以必须通过继承一个相同的父类,
# 来让子类的对象拥有相同的'数据类型',从而可以调用同一个方法

# python 语言    鸭子类型
# 因为是动态强类型语言,不需要通过来自父类的继承这个步骤,不同的对象只要拥有该方法就可直接调用,不关心数据类型


# python 动态强类型的语言
# 鸭子类型
# list tuple
# 不崇尚根据继承所得来的相似!!!!!
# 我只是自己实现我自己的代码就可以了。
# 如果两个类刚好相似，并不产生父类的子类的兄弟关系，而是鸭子类型
# list tuple 这种相似，是自己写代码的时候约束的，而不是通过父类约束的
# 优点 ： 松耦合 每个相似的类之间都没有影响
# 缺点 ： 太随意了,只能靠自觉


# 接口类和抽象类 在python当中的应用点并不是非常必要
# 因为python内置数据类型list,tuple这么相似都不是继承父类的方法,各自实现各自的
