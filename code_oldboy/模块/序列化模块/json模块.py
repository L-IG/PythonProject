'''
作者:lg
日期:2019/10/20
文件描述:
缺陷：
'''

import json

# 序列化: 数据类型->字符串
# 反序列化: 字符串->数据类型

# 用途:
# 通常在数据存储和网络传输的时候需要做序列化操作

# json *****
# pickle ****
# shelve ***

# json  # 数字  字符串 列表 字典 元组
# 通用的序列化格式
# 只有很少的一部分数据类型能够通过json转化成字符串

# pickle
# 所有的python中的数据类型都可以转化成字符串形式
# pickle序列化的内容只有python能理解
# 且部分反序列化依赖python代码

# shelve
# 序列化句柄
# 使用句柄直接操作，非常方便

# json dumps序列化方法 loads反序列化方法
dic = {'a': 1, 'b': [1, 2, 3], 'c': (5, 6), 'd': {'k1': 'v1'}}
print(type(dic), dic)  # <class 'dict'> {'a': 1, 'b': [1, 2, 3], 'c': (5, 6), 'd': {'k1': 'v1'}}

str_d = json.dumps(dic)
print(type(str_d), str_d)  # <class 'str'> {"a": 1, "b": [1, 2, 3], "c": [5, 6], "d": {"k1": "v1"}}

ret = json.loads(str_d)
print(type(ret), ret)  # <class 'dict'> {'a': 1, 'b': [1, 2, 3], 'c': [5, 6], 'd': {'k1': 'v1'}}

# python与json显示数据的区别:
# python里字符串一般用单引号表示,json都用双引号

dic = {1: "中国", 2: 'b'}
f = open('txtfile/fff.txt', 'w', encoding='utf-8')
json.dump(dic, f)
f.close()

f1 = open('txtfile/fff.txt', 'r', encoding='utf-8')
ret = json.load(f1)
print(ret)

# json每次只能读一行数据,多个json放在同一行就读不了
# json.decoder.JSONDecodeError: Extra data: line 1 column 32 (char 31)

# 多行写入则采用load方法!!!!
l = [{'k': '111'}, {'k2': '222'}, {'k3': '333'}]
f = open('txtfile/file.txt', 'w')
for el in l:
    str_dic = json.dumps(el)
    print(str_dic)
    f.write(str_dic + '\n')

f.close()

f1 = open('txtfile/file.txt', 'r', encoding='utf-8')
l_tmp = []
for i in f1:
    dic = json.loads(i.strip())
    l_tmp.append(dic)
print(l_tmp)  # [{'k': '111'}, {'k2': '222'}, {'k3': '333'}]

