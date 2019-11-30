'''
作者:lg
日期:2019/9/21
文件描述:
缺陷：
'''

# 迭代器

# 常见可迭代类型
# list,dic,str,set,tuple,f = open(),range(),enumerate
# print(dir([]))   #告诉我列表拥有的所有方法

# ret1 = set(dir([])) & set(dir({})) & set(dir('')) & set(dir(range(10)))
# ret2 = set(dir(int)) & set(dir(bool))
# print(ret1 - ret2)
# 打印结果:{'__len__', '__getitem__', '__iter__', '__contains__'}
# 发现可迭代对象比不可迭代对象多了 __iter__ 方法

# print('__iter__' in dir(int))
# print('__iter__' in dir(bool))
# print('__iter__' in dir(list))
# print('__iter__' in dir(dict))
# print('__iter__' in dir(set))
# print('__iter__' in dir(tuple))
# print('__iter__' in dir(enumerate([])))
# print('__iter__' in dir(range(1)))

# 只要是能被for循环的数据类型 就一定拥有__iter__方法
# print([].__iter__())
# 一个列表执行了__iter__()之后的返回值就是一个迭代器
# print(dir([]))
# print(dir([].__iter__()))
# print(set(dir([].__iter__())) - set(dir([])))
# print([1,'a','bbb'].__iter__().__length_hint__())  #元素个数

# l = [1,2,3]
# iterator = l.__iter__()
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# Iterable  可迭代的    -- > __iter__  #只要含有__iter__方法的都是可迭代的
# [].__iter__() 迭代器  -- > __next__  #通过next就可以从迭代器中一个一个的取值
# 只要含有__iter__方法的都是可迭代的 —— 可迭代协议


# print('__iter__' in dir( [].__iter__()))
# print('__next__' in dir( [].__iter__()))

from collections import Iterable
from collections import Iterator


# print(isinstance([],Iterator))
# print(isinstance([],Iterable))

# class A:
#     # def __iter__(self):pass
#     def __next__(self):pass
#
# a = A()
# print(isinstance(a,Iterator))
# print(isinstance(a,Iterable))


# l = [1,2,3,4]
# for i in l.__iter__():
#     print(i)

# 迭代器的概念
# 迭代器协议 —— 内部含有__next__和__iter__方法的就是迭代器


# 迭代器协议和可迭代协议
# 可以被for循环的都是可迭代的
# 可迭代的内部都有__iter__方法
# 只要是迭代器 一定可迭代
# 可迭代的.__iter__()方法就可以得到一个迭代器
# 迭代器中的__next__()方法可以一个一个的获取值


# for循环其实就是在使用迭代器
# iterator
# 可迭代对象
# 直接给你内存地址
# print([].__iter__())
# print(range(10))

# for
# 只有 是可迭代对象的时候 才能用for
# 当我们遇到一个新的变量，不确定能不能for循环的时候，就判断它是否可迭代

# for i in l:
#     pass
# iterator = l.__iter__()
# iterator.__next__()

# 迭代器的好处：
# 从容器类型中一个一个的取值，会把所有的值都取到。
# 节省内存空间
# 迭代器并不会在内存中再占用一大块内存，
# 而是随着循环 每次生成一个
# 每次next每次给我一个
# range
# f
# l = [1,2,3,45]
# iterator = l.__iter__()
# while True:
#     print(iterator.__next__())


# 用自己的话总结:
# 可迭代对象不一定是迭代器:如列表[1,2,3,4]是可迭代对象,但不是迭代器; [1,2,3,4].__iter__ 返回的对象是迭代器
# 可以使用for循环的必定是迭代器!!!!!
# 迭代器再调用__iter__方法返回的是迭代器本身,[].__iter__().__iter__().__iter__(),
# __iter__方法相当于迭代器协议
# 为什么要用迭代器:!!!!!
# 我想要一个列表,但是别人返回的只是一个变量,就要考虑是不是迭代器了
# 其实就是想知道能不能使用for循环,for循环执行本质就是先调用该变量的iter方法,把它变成迭代器


# 生成器
# 含有yield关键词的函数都是生成器函数
# yield不能和return共用
# yield只能用在函数体内

# yield作用:让函数运行过程停止在当前位置,并且可以返回一个变量
def generator():
    print('1')
    yield 'a'
    print('2')
    yield 'b'
    print('3')
    yield 'c'


# 执行生成器函数,返回值是一个生成器
gene = generator()
print(gene)  # 打印结果:<generator object generator at 0x000001FEA5E0A830>

print(gene.__next__())
print(gene.__next__())
print(gene.__next__())


# 从生成器中取值的几个方法
# next方法,for循环,数据类型强制转换(如list方法)


# 生成器函数进阶
def genor1():
    print(123)
    yield 1
    print(1243)
    yield 2
    print('hhh')


g1 = genor1()
ret1 = g1.__next__()
ret2 = g1.__next__()


# ret3 = g1.__next__()


# print('hhh')是可以执行的,但是结尾没有yield程序会报错


def genor2():
    print('A')
    yield 1

    print('B')
    ret = yield 2

    print('send_ret', ret)
    print('C')
    yield 3


g2 = genor2()

g2.send(None)
g2.send(None)
g2.send('hello')


# send与next作用一样,但是send会给上一次yield传入一个参数
# 在碰到赋值等号时,注意执行顺序,先执行等号左边的语句,再执行右边的语句!!!!!

# 注意->不成立!!!->第一次使用生成器的时候,需要用next,因为前面没有yield来出让send传一个参数
# TypeError: can't send non-None value to a just-started generator
# 可以使用send(None)
# next底层就是在调用send函数,只是传了一个参数None(必须有一个位置参数)
# 最后一个send不能接受send传参


# 移动平均值的例子
def average():
    count = 0
    avg = 0
    sum = 0
    while True:
        new_num = yield avg
        count += 1
        sum += new_num
        avg = sum / count


a = average()
a.send(None)
print(a.send(10))
print(a.send(20))
print(a.send(30))
print(a.send(40))


# 预激生成器的装饰器

def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.__next__()  # 或者g.send(None)
        return g

    return inner


@init
def average():
    count = 0
    avg = 0
    sum = 0
    while True:
        new_num = yield avg
        count += 1
        sum += new_num
        avg = sum / count


a = average()
print(a.send(1))
print(a.send(3))


# python3 新特性
# yield from

def genor2():
    a = 'abcdefg'
    b = '1234456'
    for el in a:
        yield el
    for el in b:
        yield el


g2 = genor2()


# 可以换成下面写法
def genor2():
    a = 'abcdefg'
    b = '1234456'
    yield from a
    yield from b


ret = genor2()
for i in ret:
    print(i)

# 生成器表达式
g = (i for i in range(100))  # 两边是括号
# 列表推导式
l = [i for i in range(100)]
# 生成器表达式与列表推导式区别:几乎不占用内存,要多个个值就取多少个值

# 其他各种推导式
# [每一个元素或者是和元素相关的操作 for 元素 in 可迭代数据类型]    #遍历之后挨个处理
# [满足条件的元素相关的操作 for 元素 in 可迭代数据类型 if 元素相关的条件]   #筛选功能

# 例1:30以内所有能被3整除的数
l1 = [i for i in range(30) if i % 3 == 0]
print(l1)

# 例2:30以内所有能被3整除的数的平方
l2 = [i ** 2 for i in range(30) if i % 3 == 0]
print(l2)

# 例3:找到嵌套列表中名字含有两个‘e’的所有名字
names = [
    ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
    ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']
]

l3 = [name for l in names for name in l if name.count('e') >= 2]
print(l3)
# 分析:使用递进for循环的方式遍历数据,第一个变量的名字一定要是后面遍历元素的变量名

# 字典推导式
# 例一：将一个字典的key和value对调
mcase = {'a': 10, 'b': 34}
# {10:'a' , 34:'b'}
l3 = {mcase[k]: k for k in mcase}
print(l3)

# 例二：合并大小写对应的value值，将k统一成小写
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# {'a':10+7,'b':34,'z':3}
l4 = {k.lower(): (mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)) for k in mcase}
print(l4)
