'''
作者:lg
日期:2019/10/1
文件描述:
缺陷：
'''

L = range(100)
# 取第一到第三个元素
l1 = L[:3]
print(l1)  # 结果:range(0, 3),依然是生成器,需要把值取出来
l1 = list(L[:3])
# 最好不要使用 list(range(100))[:3]

# 把L复制给L1用
L1 = L[:]


# 注意:L1是新列表,不是赋值操作,是浅拷贝!!!!!


# 可变参数作为默认参数时 !!!!!
# 默认参数的列表会一直存在,当做是 默认列表
def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('HHHH', [])
list4 = extendList('a')

print(list1)
print(list2)
print(list3)
print(list4)

# 当不传参数时,默认参数会一直使用同一个列表

# 如何判断一个变量是不是字符串(两个方法)
a = 'abcd'
print(isinstance(a, str))
print(type(a) == str)

# 如何得到列表的交集与差集
a = [1, 2, 3]
b = [2, 3, 4]
print(set(a) & set(b))
print(set(a) - set(b))

# 写代码
# 1
d = {'a': 1, 'b': 2, 'c': 3}
# 建议不要使用item方法来取出value,因为value很大,浪费内存

# 2
l1 = [1, 2, 3, 4, 5, 89, 4, 2, 7, 19, 90]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)
# 通过集合是可以去重的,但是,转成set后就无序了

# 通过用新列表方式
new_l = []
for el in l1:
    if el not in new_l:
        new_l.append(el)
l1 = new_l
print(l1)

# 用map来处理字符串列表,把列表中所有人都变成sb,比如alex_sb
name = ['alex', 'wupeiqi', 'yuanhao', 'nazha']


def func(el):
    el = el + '_sb'
    return el


map_ret = map(func, name)
print(list(map_ret))
map_ret1 = map(lambda x: x + '_sb', name)
print(list(map_ret1))

# 用filter处理数字列表,将所有的偶数帅选出来
num = [1, 3, 5, 6, 8, 9]


def func1(n):
    return n % 2 == 0


filter_ret = filter(func1, num)
print(list(filter_ret))

# 随意写一个20多行的文件,运行程序,现将内容读到内存中,再用列表存储
# 接受用户输入页码,每页5条,仅输出当前页码(用户输入)的内容

FILENAME = 'txt\python真题.txt'
with open(FILENAME, encoding='utf-8') as f:
    l_content = f.readlines()

pages, mod = divmod(len(l_content), 5)
if mod != 0:
    pages += 1
print(f'\033[31m总共{pages}页!\033[0m')
page_num = int(input('请输入页码:').strip())
if page_num > pages or page_num <= 0:
    print('\033[31m输入有误!\033[0m')
elif page_num == pages:
    for i in range((pages - 1) * 5, (pages - 1) * 5 + mod):
        print(l_content[i])
else:
    for i in range(5 * page_num - 5, 5 * page_num):
        print(l_content[i].strip())

# 分析:
# 1 1~5
# 2 6~10
# 3 11~15
# 4 16~20
# 5 21~23
# 规律 range(5i-4,5i+1)
# 列表:range(5i-5,5i)

# 6.如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
# 6.1.计算购买每支股票的总价
# 6.2.用filter过滤出，单价大于100的股票有哪些
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

map_ret = map(lambda s: s['shares'] * s['price'], portfolio)
# print(list(map_ret))

filter_ret = filter(lambda x: x['price'] > 100, portfolio)
# print(list(filter_ret))
