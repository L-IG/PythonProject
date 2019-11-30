'''
作者:lg
日期:2019/9/15
文件描述:
缺陷：
'''


# 什么是闭包:嵌套函数,内部函数引用了外部函数里的变量
def outer():
    a = 10

    def inner():
        print(a)

    print(inner.__closure__)  # 打印结果:(<cell at 0x000002AC72BF6498: int object at 0x000000005E45C7D0>,)


outer()


# 满足条件: 必须是内部函数引用了外部函数的变量


def outter():
    a = 10

    def inner():
        print(a)

    return inner


inn = outter()

# 为什么会有闭包的出现?
# 如果需要使用内部函数,则需要调用outter,先是创建了变量a,函数名inner放在命名空间里,最后再释放
# 如果是频繁调用的话,会增加很多开销.
# 所以,利用闭包,当把内部函数名返回出去时,内部函数引用来自外部函数的变量不会消失,相当于延长了生存周期
# 优点:可以频繁调用内部函数而不增加创建变量的开销
# 缺点:该变量会一直存在着,某些方面会一直占用内存


# 举例
from urllib.request import urlopen


def get_url():
    url_web = 'https://music.163.com/#/my/m/music/playlist?id=145490331'

    def get_web():
        ret = urlopen(url_web).read()
        print(ret)

    return get_web


get_func = get_url()


# get_func()
# get_func()
# get_func()
# 多次调用不增加创建变量的开销


# 闭包中,内层函数来自外层函数的变量会一直存活着
def global_var():
    a = 0
    print('执行了 a = 0,a的内存地址为', id(a))

    def inner():
        nonlocal a
        a += 1
        print('a', a)

    return inner


# 第一种:
ret_func = global_var()
print('ret_func', id(ret_func))
ret_func()
ret_func()
ret_func = global_var()
print('ret_func', id(ret_func))
ret_func()
ret_func()
# 第二种:
ret_func = global_var()
print('ret_func', id(ret_func))
ret_func()
ret_func()
ret_func1 = global_var()
print('ret_func', id(ret_func))
ret_func()
ret_func()


# 为什以下两种结果不一样:
# 第一种:
# 执行了 a = 0,a的内存地址为 1581500048
# ret_func 2124928197496
# a 1
# a 2
# 执行了 a = 0,a的内存地址为 1581500048
# ret_func 2124928197632
# a 1
# a 2


# 第二种:
# 执行了 a = 0,a的内存地址为 1581500048
# ret_func 2124928197496
# a 1
# a 2
# 执行了 a = 0,a的内存地址为 1581500048
# ret_func 2124928197496
# a 3
# a 4


# 原因分析:
# 第一种方法:第一次执行global_var函数时,生成一个新的闭包函数地址,第二次再执行,会生成新的闭包函数地址覆盖掉旧闭包函数
# 即使他们名字是一样的,所以旧的闭包函数里的变量会消失


# 进阶,容易混淆的地方!!!!!
def wrapper2():
    a = 0

    def inner():
        nonlocal a
        a += 1
        print('a', a)

    return inner


f1 = wrapper2()
f1()
f2 = wrapper2()
f1()

f2()
f2()
f2()


# 打印结果:
# a 1
# a 2

# a 1
# a 2
# a 3
# 原因分析:
# 结合上面的例子,互相印证:每次执行wrapper2,得到一个新的闭包空间,f1与f2就各自拥有独立的空间,并且各自有独立的私有变量a,互不影响
# 各自的闭包函数不断被执行,如f1执行多次,都是对自己闭包空间里的a变量作修改


# 浓缩成下面的情景
def print_a():
    a = 0
    print('id', id(a))


print_a()
print_a()


# 打印结果:
# id 1581500048
# id 1581500048


# 所以可以解释为什么下面例子执行结果不在预想结果内
# 解释:say1 与 say2 是两个不同的闭包空间,login_flag也是各自独立,修改自己闭包空间里的login_flag并不影响其它闭包空间
# 结论:因此,不能用这里的变量作为共享区,或者说是通信方式告知其他函数已经认证成功,还是需要'全局变量'作为共享区!!!!!
def wrapper1(func):
    login_flag = False

    def inner():
        nonlocal login_flag
        if login_flag:
            print('已认证')
            ret = func()
            return ret
        else:
            username_in = input('请输入用户名:')
            if 'alex' == username_in:
                print('认证成功!')
                login_flag = True
                ret = func()
                return ret

    return inner


@wrapper1
def say_1():
    print(1)


@wrapper1
def say_2():
    print(2)


say_1()
say_1()
say_2()
