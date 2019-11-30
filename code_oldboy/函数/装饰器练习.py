'''
作者:lg
日期:2019/9/21
文件描述:
缺陷：#1 为了解决'认证成功一个后,别的函数就不需要认证了',此时用到了全局变量LOGIN_FLAG,函数变得不安全
'''

# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）,
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
FILENAME = '装饰器练习1.txt'

# 用列表来代替全局变量,函数更安全
FLAG_LIST = [False]


def wrapper1(func):
    def inner():
        if FLAG_LIST[0]:
            ret = func()
            return ret
        else:
            for i in range(3):
                with open(FILENAME, encoding='utf-8') as f:
                    username, password = f.read().strip().split('|')
                username_in = input('请输入用户名:')
                password_in = input('请输入密码:')
                if username_in == username and password_in == password:
                    print('认证成功!')
                    FLAG_LIST[0] = True
                    ret = func()
                    return ret
            else:
                print('已经试了3次机会了')

    return inner


@wrapper1
def say_1():
    print(1)


@wrapper1
def say_2():
    print(2)


say_1()
say_2()

# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
from functools import wraps

FILENAME2 = '装饰器练习2.txt'


def wrapper2(func):
    # @wraps(func)
    def inner(*args, **kwargs):
        with open(FILENAME2, 'a', encoding='utf-8') as f:
            f.write(func.__name__)
            f.write('\n')
        ret = func(*args, **kwargs)
        return ret

    return inner


@wrapper2
def apple():
    print('apple')


@wrapper2
def banana():
    print('banana')


@wrapper2
def orange():
    print('orange')


apple()
banana()
orange()

# 进阶
# 1.编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 2.为题目1编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中

from urllib import request

FILENAME3 = '.txt'


def wrapper3(func):
    def inner(*args, **kwargs):
        with open(FILENAME3, 'rb', ) as f:
            content = f.read()
        if content:
            return content
        else:
            ret = func(*args, **kwargs)
            with  open(FILENAME3, 'wb') as f1:
                # ret = ret.decode('utf-8')  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcb in position 159741: invalid continuation byte
                f1.write(ret)
            return ret

    return inner


@wrapper3
def get_web(url):
    ret = request.urlopen(url)
    return ret.read()


print(get_web('https://daohang.qq.com/?fr=hmpage'))
