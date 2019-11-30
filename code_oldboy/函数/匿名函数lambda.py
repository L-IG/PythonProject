'''
作者:lg
日期:2019/10/2
文件描述:
缺陷：
'''

# lambda函数的格式:
# 函数名 = lambda关键字 参数 : 返回值
add_f = lambda a, b: a + b
print(add_f)


# 把一般函数用lambda方法写:
def add(x, y):
    return x + y


add_func = lambda x, y: x + y

# 例题:按照字典的Value值进行排序
# 注意:max方法按照Key的assci码值排序,并且只返回Key值!!
dic1 = {'k1': 10, 'k2': 100, 'k3': 30}
print(max(dic1))  # 打印结果: k3
# 用lambda函数简写:
print(max(dic1, key=lambda x: dic1[x]))  # 打印结果: k2

# lambda函数一般是和其他函数联合一起的使用!!!!!
# 通常与内置函数 min,max,sorted,map,filter一起用
# min,max,sorted 中有关键词参数Key,map,filter第一个参数都是传函数名变量的
ret1 = sorted([1, -2, 3, 4, -5, 6], key=lambda i: i ** 2)
print('ret1 = ', ret1)
ret = map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6])
print('ret = ', list(ret))  # 打印结果:[1, 4, 9, 16, 25, 36]

# 例2:
# 现有两个元组
t1 = (('a'), ('b'))
t2 = (('c'), ('d'))
t = (t1, t2)
# 请使用python中匿名函数生成列表 l = [{'a': 'c'}, {'b': 'd'}] !!!!!

# 问题:怎么用lambda把列表变成字典!!!!!
# 第一种:dict方法
# print('dic = ', dict([[12], [43]])) 会报错!!!!
# ValueError: dictionary update sequence element #0 has length 1; 2 is required(#0 表示 可迭代对象 中的 某个元素 的下标为0的参数)
# 原因:dict方法需满足两个苛刻条件:只接受一个可迭代对象(可以写成一个元素,要这样写((12, 2), )用逗号隔开),可迭代对象中的每个元素必须只有两个元素!!!!!
# print('dic = ', dict(((12, 2),)))
# 官方解释:
#                 d = {}
#                 for i in z:
#                     d[i[0]] = i[1]
#                 print(d)

# 第二种:直接返回字典形式的格式 return {l[0]: l[1]}   (不用新建一个空字典,再往里面填值)
# l = ['key', 10]
# def l_to_dic(l):
#     return {l[0]: l[1]}
# print(l_to_dic(l))
# 打印结果: {'key': 10}

z = zip(t1, t2)

# 第一种写法(利用dict方法):
# ret = map(lambda x: dict((x,)), z)
# print(list(ret))

# 第二种写法
ret = map(lambda x: {x[0]: x[1]}, z)
print(list(ret))


# 例3
def multipliers():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers()])

# lambda函数的一个特性:!!!!!
# 如果lambda含有一个变量,并且没有被立即执行的,这个变量的值以最后一次被修改的值为准
l2 = []
for i in range(100):
    l2.append(lambda: i)
print(l2[0]())
print(l2[1]())
