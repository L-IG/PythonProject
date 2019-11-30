'''
作者:lg
日期:2019/9/4
文件描述:字典编程练习
缺陷：
'''

dic1 = {
    'name': ['alex', 2, 3, 5],
    'job': 'teacher',
    'oldboy': {'alex': ['python1', 'python2', 100]}
}
# 1，将name对应的列表追加⼀个元素’wusir’。
# 2，将name对应的列表中的alex⾸字⺟⼤写。
# 3， oldboy对应的字典加⼀个键值对’⽼男孩’,’linux’。
# 4，将oldboy对应的字典中的alex对应的列表中的python2删除。

# 1
dic1['name'].append('Wusir')
print(dic1)

# 2
dic1['name'][0] = dic1['name'][0].upper()
print(dic1)

# 3
dic1['oldboy'].setdefault('⽼男孩', 'linux')
print(dic1)

# 4
del dic1['oldboy']['alex'][1]
print(dic1)

# 列表可以添加元素
dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11, 22, 33]}

dic['k3'].append(44)
print(dic)

# 有字符串'k:1|k1:2|k2:3|k3:4' 处理成字典{'k':1, 'k1':2,...}
str1 = 'k:1|k1:2|k2:3|k3:4'

dic1 = {}
l_tmp = str1.split('|')
for i in l_tmp:
    k, v = i.split(':')
    dic1.setdefault(k, v)
print(dic1)

# 有如下列表,li = [11,22,33,44,55,66,77,88,99,90],将大于66的值保存在字典第一个key,小于66的存于第二个k
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]

# 千万不能这么写,不然l1,l2永远是一样的--->l1 = l2 = []  !!!!!
l1 = []
l2 = []
for i in li:
    if i > 66:
        l1.append(i)
    else:
        l2.append(i)
dic = {}
dic['k1'] = l1
dic['k2'] = l2
print('dic', dic)

# 商品列表 ,用户输入序号,显示用户选中的商品
goods = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '游艇', 'price': 20},
    {'name': '美女', 'price': 998},
]

l = []
for index, dic in enumerate(goods):
    s = '{} {} {}'.format(index + 1, dic['name'], dic['price'])
    l.append(s)
for i in l:
    print(i)
print(l)
# '1 2 4'
while True:
    user_in = input('请输入序号或直接退出q(Q):').strip()

    if user_in.upper() == 'Q':
        break
    str2 = user_in.split()
    for i in str2:
        if not i.isdigit():
            print('输入有误')
            break
    else:
        l_tmp = []
        for i in str2:
            l_tmp.append(int(i))
        for index, el in enumerate(l):
            if (index + 1) in l_tmp:
                print(l[index])
        break

# 第一种情况: if...else... 即是分支管理,当 if 的条件里有许多变量要判断时,如用到了 for 循环, while 循环
for el in l:
    if el > 0:
        print('当前是OK')
    else:
        print('当前不OK,退出')
        break  # 退出当前循环,并且后面else里代码也不执行!
else:
    print('元素全部满足条件,开始执行else里的语句!')

# 第二种情况: if...else... 即是分支管理,当 if 的条件里只有一个变量要判断时
while True:
    if index < 0:
        print('当前不OK')
        continue
    else:
        print('开始执行else里的语句!')
