'''
作者:lg
日期:2019/9/2
文件描述:元组和列表编程练习
缺陷：
'''

li = ['alex', 'WuSir', 'ritian', 'barry', 'wenzhou']

print(len(li))

li.append('seven')
print(li)

li.insert(0, 'Tony')
print(li)

li[1] = 'Ketty'
print(li)

l2 = [1, 'a', 3, 4, 'heart']
# 迭代添加
li.extend(l2)
print(li)

s = 'qwert'
li.extend(s)
print(li)

ret_item = li.pop(1)
print(ret_item)
print(li)

del li[1:4]
print(li)

li.reverse()
print(li)

c = li.count('alex')
print(c)

# 用切片实现每个功能
li = [1, 3, 2, 'a', 4, 'b', 5, 'c']

l1 = li[:3]
print(l1)

l2 = li[3:6]
print(l2)

l3 = li[::2]
print(l3)

l4 = li[1:6:2]
print(l4)

l5 = li[-1:]
print(l5)

l6 = li[-3:-8:-2]
print(l6)

# 嵌套列表练习
lis = [2, 3, 'k', ['qwe', 20, ['k1', ['tt', 3, '1']], 89], 'ab', 'adv']
lis[3][2][1][0] = lis[3][2][1][0].upper()
print(lis)

# 拼接
li = ['alex', 'eric', 'rain']
ret = '_'.join(li)
print('ret', ret)

# 通用方法
li = ['alex', 'eric', 'rain']
s = ''
count = 0
while count < len(li):
    if count == len(li) - 1:
        s += li[count]
        count += 1
        continue
    li[count] += '_'
    s += li[count]
    count += 1
print('s', s)

#
li = ['alex', 'WuSir', 'ritian', 'barry', 'wenzhou']
for i in range(len(li)):
    print(i)

#
li = []
for i in range(100):
    if i % 2 == 0:
        li.append(i)
print(li)

li = []
for i in range(50):
    if i % 3 == 0:
        li.append(i)
print(li)

# 用range倒序打印100~1   错误写法
# for i in range(0, 101, -1):
#     print(i)

# 正确写法
for i in range(100, 0, -1):
    print(i)

#
l = []
for i in range(100, 9, -1):
    if i % 2 == 0:
        l.append(i)
print(l)
for i in l:
    if i % 4 != 0:
        l.remove(i)
print(l)

#
l = []
for i in range(1, 31):
    l.append(i)
for i in l:
    if i % 3 == 0:
        l[l.index(i)] = '*'
print(l)

l = []
for i in range(1, 31):
    l.append(i)
for index, item in enumerate(l):
    if item % 3 == 0:
        l[index] = '*'
print(l)

# 11
li = ['TaiBai', 'ale xC', 'Ab c', 'egon', 'ri tian', 'Wu sir', '  aqc ']
l = []
for i, ele in enumerate(li):
    ele = ele.replace(' ', '')
    if (ele.startswith('A') or ele.startswith('a')) and ele.endswith('c'):
        l.append(ele)
print(l)

# 12
# li = ['土豆丝', '西红柿', '苹果', '梨子', '香蕉']
# l_lst = []
# str_user = input('请输入:').strip()
# for el in li:
#     if el in str_user:
#         str_user = str_user.replace(el, '*' * len(el))
# print(str_user)

# 13
li = [1, 3, 4, 'alex', [3, 7, 8, 'TaiBai', 5, 'RiTian']]

# 错误写法
# type的返回值是类名

# for el in li:
#     if type(el) == 'list':
#        for i in el:
#            print(i)
#     print(el)

# 正确写法
for el in li:
    if type(el) == list:
        for i in el:
            print(i)
    else:
        print(el)

# 14
li = ['张三_45', '李四_78', '小明_90', '小红_100', '紫荆_89']

count = 0
for el in li:
    name, score = el.strip().split('_')
    score = int(score)
    count += score
aVg = count / len(li)
print(aVg)

