'''
作者:lg
日期:2019/9/22
文件描述:
缺陷:程序退出后CASH_DIC就消失了,需要写到文件里,下一次启动在读出来
'''

from urllib import request
import os

CASH_DIC = {
    '网址': '文件名'
}
FILENAME_COUNT = [0]


def wrapper3(func):
    def inner(url):
        if url in CASH_DIC:
            print("\033[31m网址已经登陆过\033[0m")
            filename = CASH_DIC.setdefault(url)
            with open(filename, 'rb') as f1:
                return f1.read()
        else:
            print("\033[31m网址没有登陆过\033[0m")
            filename = f'{FILENAME_COUNT[0]}.txt'
            CASH_DIC.setdefault(url, filename)
            FILENAME_COUNT[0] += 1
            with open(filename, 'wb') as f2:
                ret = func(url)
                f2.write(ret)
            return ret

    return inner


@wrapper3
def get_web(url):
    ret = request.urlopen(url)
    return ret.read()


print(get_web('https://daohang.qq.com/?fr=hmpage'))
print(get_web('https://daohang.qq.com/'))
print(get_web('https://www.baidu.com/'))
print(get_web('https://daohang.qq.com/?fr=hmpage'))
print(get_web('https://daohang.qq.com/?fr=hmpage'))
