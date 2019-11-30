'''
作者:lg
日期:2019/11/23
文件描述:
缺陷：
'''


# 和面向对象有关的内置方法
class A():
    pass


a = A()


class B(A):
    pass


# 表示第一个参数是否是第二个参数的实例
print(isinstance(a, A))
# 表示第一个参数是否是第二个参数的子类
print(issubclass(B, A))


# 反射 ： 是用字符串类型的名字 去操作 变量
# eval('print(name)')  # 安全隐患
# 反射 就没有安全问题
# hasattr,getattr,setattr,delattr

# 反射在网络传输中用的比较多
# 可以直接通过字符串变量来找到函数名,而不用每来一个字符串都遍历判断一下到底是什么函数

# 反射对象中的属性和方法
# 反射类的属性和方法
class Person():
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eat')

    @classmethod
    def count(cls):
        print('count')


alex = Person('alex', 18)
if hasattr(alex, 'name'):
    ret = getattr(alex, 'name')
    print(ret)
if hasattr(alex, 'eat'):
    ret = getattr(alex, 'eat')
    ret()
if hasattr(Person, 'country'):
    ret = getattr(Person, 'country')
    print(ret)
if hasattr(Person, 'count'):
    ret = getattr(Person, 'count')
    print(ret)


# if hasattr(Person, 'eat'):
#     ret = getattr(Person, 'eat')
#     ret()


# 反射其他模块的属性,反射模块的方法


# 反射自己模块中的命名变量和方法
def my_func():
    print('my func')


import sys

print(sys.modules['__main__'])
# 打印结果:<module '__main__' from 'D:/Python_Project/code_oldboy/面向对象/面向对象进阶/反射.py'>
# 如果当前文件被其他模块导入使用,__name__就不是__main__了,所有最好这样使用:
my_module = sys.modules[__name__]
if hasattr(my_module, 'my_func'):
    getattr(my_module, 'my_func')

# setattr  设置修改变量
# delattr  删除一个变量
