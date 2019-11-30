'''
作者:lg
日期:2019/9/21
文件描述:装饰器概念
缺陷：
'''

# 最先的装饰器写法
import time


def func():
    time.sleep(0.1)
    print('hello xi')


def decotor(func):
    def inner():
        time1 = time.time()
        func()
        time2 = time.time()
        print('函数执行了', time2 - time1)

    return inner


func = decotor(func)
func()


# 装饰器的作用:不想修改原函数代码,又想添加新功能
# 开放封闭原则:
# 开放:对扩展功能开放
# 封闭:对修改代码封闭
# 项目已经成型,函数不知道被谁调用了,所以不要轻易修改,即使定义一个新变量,除非重构代码


# 带返回值,带参数的装饰器
def func1(*args, **kwargs):
    time.sleep(0.1)
    print('hello xi')
    return 1111


def decotor1(func1):
    def innner(*args, **kwargs):
        time1 = time.time()
        ret = func1(*args, **kwargs)
        time2 = time.time()
        print('函数执行了', time2 - time1)
        return ret

    return innner


func1 = decotor1(func1)
ret = func1(1, 2, a=19, b=20)
print(ret)


# 为什么要用动态参数
def decotor2(f):
    def innner(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('函数执行了', time2 - time1)
        return ret

    return innner


@decotor2
def func2(a):
    time.sleep(0.1)
    print('hello xi')
    return 1111


@decotor2
def func3(a, b=1):
    time.sleep(0.1)
    print('hello xi')
    return 1111


# 打印被装饰的函数的__name__,__doc__属性
from functools import wraps


def wrapper(f):
    @wraps(f)
    def inner():
        '''
        inner
        :return:ret
        '''
        ret = f
        return ret

    return inner


@wrapper
def say_hi():
    '''
    打印hi
    :return: None
    '''
    print('hi')


print('say_hi', say_hi.__name__)
print(say_hi.__doc__)
