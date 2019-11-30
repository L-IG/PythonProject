'''
作者:lg
日期:2019/9/15
文件描述:
缺陷：
'''


# 写函数,接受任意个数字,求这些数字的和
def sum_func(*args):
    sum1 = 0
    for i in args:
        sum1 += i
    print(sum1)


sum_func(1, 2, 3, 4, 5, 6, 89)


# 2
def func1(l):
    l_tmp = []
    for index, el in enumerate(l):
        if index % 2 == 1:
            l_tmp.append(el)
    return l_tmp


# 从有规律的序列(元组,列表,字符串)里取值,或者奇数,偶数位,可以利用切片步长的特点

l1 = [1, 2, 3, 4, 6]
ret1 = func1(l1)
print('ret1', ret1)
# 对于可变数据类型来说,不需要作为参数传进函数里,因为函数里面可以直接访问并修改,
# 可变数据类型的赋值操作一定要注意,传参过程,这里对于列表来说,就是  '形参 = 实参' 的操作


l2 = (1, 2, 3, 4, 6, 7, 8, 9, 10)
ret2 = func1(l2)
print('ret2', ret2)


# 3
def obj_len(obj):
    if len(obj) > 5:
        print('长度大于5')


obj_len('123')
obj_len([1, 2, 5, 6, 78, 89, 45])
obj_len((1, 2, 5, 6, 78, 89, 45))


# 4
def len_list(l):
    if len(l) > 2:
        return l[0:2]


print(len_list([99, 100, 1, 2, 3, 4, 5]))


# 5

def count1(str):
    num_c = 0
    alpha_c = 0
    black_c = 0
    other_c = 0
    for el in str:
        if el.isdigit():
            num_c += 1
        elif el.isalpha():
            alpha_c += 1
        elif el.isspace():
            black_c += 1
        else:
            other_c += 1
    return (num_c, alpha_c, black_c, other_c)


print(count1('ada123dw hehf 23f汉d%gv '))


# 5 另一种写法
# 可以让其他人 不看函数源码 就能理解 调用函数后返回值的含义,如print,len方法等
# 返回值要明朗,如果有多个需要区分的值就用字典
def count2(str):
    dic = {
        'num_c': 0,
        'alpha_c': 0,
        'space_c': 0,
        'other_c': 0,
    }
    for el in str:
        if el.isdigit():
            dic['num_c'] += 1
        elif el.isalpha():
            dic['alpha_c'] += 1
        elif el.isspace():
            dic['space_c'] += 1
        else:
            dic['other_c'] += 1
    return dic


print(count2('ada123dw hehf 23f汉d%gv '))


# 6
def del_obj(obj):
    if ' ' in obj:
        print('含有空格!')
    else:
        print('不含空格')


del_obj('sd dfdf')
del_obj([1, ' ', 'sd'])
del_obj((1, ' ', 'sd'))


# 7
def del_set(set1):
    set2 = {}
    for k, v in set1.items():
        if len(v) > 2:
            set2.setdefault(k, v[0:2])
    return set2


print(del_set({'K1': 'V1V1', 'K2': [11, 22, 33, 44, 55]}))


# 7 优化写法
def del_set(dic1):
    for k in dic1:
        if len(dic1[k]) > 2:
            dic1[k] = dic1[k][0:2]  # 字典Value可以直接修改
    return dic1


print(del_set({'K1': 'V1V1HA', 'K2': [1, 23, 11, 22, 33, 44, 55]}))


# 8
def cal_num(a, b):
    if a > b:
        return a
    else:
        return b


print(cal_num(1, 19))
print(cal_num(100, 19))


# 8 三元运算方法
def cal_num1(a, b):
    return a if a > b else b


print('cal_num1', cal_num1(99, 90))

# 9
import os


def updata_file(file, data):
    with open(file, 'r', encoding='utf-8') as fr, open(f'{file}.bak', 'w', encoding='utf-8') as fw:
        for line in fr:
            if data in line:
                line = line.replace(data, '')
            fw.write(line)
    os.remove('函数基础练习.txt')
    os.rename('函数基础练习.txt.bak', '函数基础练习.txt')


updata_file('函数基础练习.txt', 'AA')
