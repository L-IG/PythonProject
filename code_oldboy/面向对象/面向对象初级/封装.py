'''
作者:lg
日期:2019/11/23
文件描述:
缺陷：
'''


# 广义上面向对象的封装 ：代码的保护，面向对象的思想本身就是一种
# 只让自己的对象能调用自己类中的方法

# 狭义上的封装 —— 面向对象的三大特性之一
# 属性 和 方法都藏起来 不让你看见

class Person():
    miyao = 'ABC'  # 私有静态属性

    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex  # 私有属性

    def get_sex(self):
        return self.__sex

    def __get_money(self):  # 私有方法
        print(self.__sex)  # 只要在类的内部使用私有属性，就会自动的带上_类名
        return self.__dict__

    def get(self):  # 正常的方法调用私有的方法
        return self.__get_money()


alex = Person('ALEX', 'male')
print(alex.__dict__)
print(alex._Person__sex)  # _类名__属性名

print(alex.get_sex())
print(alex.get())


# 所有的私有 都是在变量的左边加上双下划綫(在类外面使用__变量名并不是私有方法,只有在类里面才是私有属性!!)
# 对象的私有属性
# 类中的私有方法
# 类中的静态私有属性
# 所有的私有的 都不能在类的外部使用


class Room():
    def __init__(self, name, width, lenth):
        self.name = name
        self.__width = width
        self.__lenth = lenth

    # 对于C++,每一个私有属性都是通过get和set方法和外界交互的
    # 不让外界直接修改,可以更好的保护数据
    def get_lenth(self):
        return self.__lenth

    def set_lenth(self, new_lenth):
        self.__lenth = new_lenth


r = Room('Alex', 100, 60)


class Foo():
    __key = '123'


class Son(Foo):
    pass
    # print(Foo.__key)
    # AttributeError: type object 'Foo' has no attribute '_Son__key'
    # 私有属性在哪个类里面,就会根据哪个类来变形
    # 所以,私有属性不会被子类继承

# 会用到私有的这个概念的场景
# 1.隐藏起一个属性 不想让类的外部调用
# 2.我想保护这个属性，不想让属性随意被改变(入参保护)
# 3.我想保护这个属性，不被子类继承
