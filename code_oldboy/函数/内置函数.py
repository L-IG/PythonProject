'''
作者:lg
日期:2019/10/1
文件描述:python内置函数
缺陷：
'''

# -------------作用域相关
print(locals())  # 返回当前作用域的所用名字
print(globals())  # 返回全局作用域中的所有名字

# global nonlocal是关键词
# global声明一个变量为全局变量,nonlocal在内部函数里声明一个来自外部函数的变量

# ------------迭代器,生成器相关
# 迭代器.__next__()
# next(迭代器)
# 迭代器 = iter(可迭代的)
# 迭代器 = 可迭代的.__iter__()

range(10)
range(1, 11)
print('__next__' in dir(range(1, 11, 2)))
print('__next__' in dir(iter(range(1, 11, 2))))

# ------------其他
# dir:查看一个对象拥有的方法
print(dir([]))

# help:帮助文档!!!!!(封闭环境内开发很重要)
# help(str)

# callable:判断一个变量是否是可调用的,是否是函数名
print(callable([]))

# __import__:import
t = __import__('time')
print(t.time())

# open:文件相关

# id:查看变量内存地址

# hash:对于相同的可hash数据的hash值在一次程序执行过程中总是不变的
# 字典的为什么查找很快?
# 字典的寻址方式:因为Key是可hash的,hash直接作为内存地址,存的即是Value值,因此,dic[Key]能快速查找Value

# 输入,输出
# input()
print(123, 345, 3435, sep='%%', end='\n\n')

# 打印进度条的例子
import time

# for i in range(0, 101, 2):
#     time.sleep(0.1)
#     char_num = i // 2
#     per_str = '\r%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s' % (i, '*' * char_num)
#     print(per_str, end='', flush=True)

# for i in range(0, 101):
#     time.sleep(0.03)
#     print(f'\r国庆节快乐!\n' if i == 100 else f'\r{i}% : {"*" * i}', end='')


# ------------基础数据类型相关
# 复数:complex
a = 5 + 9j
print(a)

# 浮点数:float,小数点可以浮动,在任何语言里都是不精准的,因为二进制转十进制有误差
# 354.123 = 3.54123*10**2 = 35.4123 * 10

# 数据类型的方法有:
# int,bool,float,complex

print(bin(100))
print(oct(100))  # 进制转化
print(hex(100))

print(abs(-5))

print(divmod(7, 2))  # div除法 mod取余
# 结果: (3,1)

print(round(3.14159, 3))  # 保留的小数位数

print(pow(2, 3))  # pow幂运算  == 2**3

# sum()只接受两个参数,第一个参数是一个可迭代对象,第二个参数是从start开始加(注意:这里关键词参数在传参是不能指定)
print(sum([1, 2, 3, 4]))
print(sum([1, 2, 3, 4], 100))

print(min([1, 2, 3, 4]))
print(min(1, 2, 3, 4))
print(min(1, 2, 3, -4))
print(min(1, 2, 3, -4, key=abs))

print(max([1, 2, 3, 4]))
print(max(1, 2, 3, 4))
print(max(1, 2, 3, -4))
print(max(1, 2, 3, -4, key=abs))

# --------------数据结构相关
# list,tuple 在强制数据类型转化时使用

# reversed 列表翻转,生成新列表(迭代器)
# reverse 在原有列表上修改
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)  # 结果:[5, 4, 3, 2, 1]
l1 = [1, 2, 3, 4, 5]
l2 = reversed(l1)
print(l2)
# 打印结果:<list_reverseiterator object at 0x00000230F9FDE4A8>
# 是迭代器,因为这样更节省内存空间

# slice 切片,相当于序列的切片功能
l = (1, 2, 23, 213, 5612, 342, 43)
sli = slice(1, 5, 2)  # 先生成一个切片规则
l2 = l[sli]  # 与切片写法一样 -> l[1:5:2]
print(l2)

# format 作用很多,不仅仅是字符串的方法
print(format('test', '<40'))  # 左对齐
print(format('test', '>40'))  # 右对齐
print(format('test', '^40'))  # 居中对齐

# bytes 把unicode转化为bytes类型
# bytearray # 返回值是一个列表,可以直接修改  ,因此,可以直接对字符串进行修改而不用添加新字符串
print(bytes('你好', encoding='gbk'))
print(bytes('你好', encoding='utf-8'))
print(bytes('我好', encoding='utf-8'))

b_array = bytearray('你好', encoding='utf-8')
print(b_array)
print(b_array[0])
b_array[0] = 0xe6
b_array[1] = 0x88
b_array[2] = 0x91
print(b_array.decode('utf-8'))

# memoryview 方法

# ord,chr
# 把字符按照unicode表的对应数字顺序返回回来
print(ord('A'))
print(ord('a'))
print(chr(100))

# ascii
# 在ascii表中就原封不动转回来,不在就转成unicode码返回
print(ascii('在'))
print(ascii('A'))

# repr
# 原封不动的打印出字符串带双引号的格式
a = '国庆节'
print('hello %s' % a)
print('hello %r' % a)
# 结果:   hello 国庆节
#        hello '国庆节'

# dict,set,frozenset
# frozenset() 可以是集合不可变,因此可作为字典的Key

# ----------重要内置函数

# all 判断一个可迭代对象中是否有False值
# any 判断一个可迭代对象中是否有True值
print(all([1, 2, 3, None, '']))
print(all([1, 2, 3, 1, ' ']))

print(any(['', None, 0]))
print(any(['', None, 1]))

# zip 拉条函数
l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd']
d1 = {'k1': 1, 'k2': 2}
z_obj = zip(l1, l2, d1)
print(z_obj)  # <zip object at 0x00000213B0D97B88>  迭代器
print('__iter__' in dir(z_obj).__iter__())  # true
print('__next__' in dir(z_obj).__iter__())  # true
for el in z_obj:
    print(el)


# 打印结果:
# (1, 'a', 'k1')
# (2, 'b', 'k2')


# map, filter
# filter 不会更改可迭代对象的元素,只会更改总的数量
# map 保持总的数量不变,但是会更改元素的值
def func(a):
    return a > 10


list1 = [1, 45, 35, 8, 12, 90, 6, 3, 14]

ret = filter(func, list1)
print(ret)  # <filter object at 0x000001F7CCE6D1D0>  返回一个迭代器
print(list(ret))  # 打印结果:[45, 35, 12, 90, 14]


def pow_func(a):
    return pow(a, 2)


ret1 = map(pow_func, list1)
print(ret1)  # <map object at 0x000002D5A01817B8> 返回一个迭代器
print(list(ret1))  # 打印结果:[1, 2025, 1225, 64, 144, 8100, 36, 9, 196]

# 例子:求100以内开根号后是整数
import math


def sqrt_func(num):
    if math.sqrt(num) % 1 == 0:
        return True
    else:
        return False


sqrt_ret = filter(sqrt_func, range(1, 101))
print(list(sqrt_ret))

# sort,sorted
l = [1, -4, 6, 5, -10]
l.sort(key=abs)  # 支持经过某种方法处理,过滤后再进行排序!!!!!
print(l)

l1 = [1, -4, 6, 5, -10]
ret = sorted(l1)
print(ret)  # 打印结果:[-10, -4, 1, 5, 6]
# 此处直接返回一个列表,不再返回迭代器了,因为排序需要算法,比较复杂

# 举例:根据序列的长度排序
l = [' ', [1, 2], 'hello world']
l_ret = sorted(l, key=len)
print(l_ret)
