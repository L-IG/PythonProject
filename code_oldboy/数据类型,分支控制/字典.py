'''
作者:lg
日期:2019/9/3
文件描述:字典基本属性和操作
缺陷：
'''

# 增加操作
dic = {'黄山': '安徽'}

dic['杭州'] = '浙江'
# 赋值操作, 直接修改Value
dic['杭州'] = '浙江省'

dic.setdefault('上海', '直辖市')
print(dic)
# setdefault 当K已经存在时,不再添加新的Value
# 只设置K时,默认Value值为None
dic.setdefault('上海')
dic.setdefault('上海', '靠近海岸线')
print(dic)

# 删除
dic = {'黄山': '安徽', '杭州': '浙江省', '上海': '直辖市'}

# 返回被删除元素的Value
ret = dic.pop('黄山')
print(ret)
# 删除不存在的元素会报错
# ret = dic.pop('不存在元素')

del dic['上海']
print(dic)

# 随机删除
# ret为元组形式 -> ('上海', '直辖市')
ret = dic.popitem()
print(ret)

# 清空字典
dic.clear()

# 修改
dic1 = {'黄山': '安徽', '杭州': '浙江省', '上海': '直辖市'}
dic2 = {'黄河': '长', '长江': '宽', '黄山': '安徽啊啊'}

# update 把dic2元素更新到dic1中,Key重名则修改为新Value,不重名就新增
dic1.update(dic2)
print('dic1 = ', dic1)

# 查询
dic = {'黄山': '安徽', '杭州': '浙江省', '上海': '直辖市'}
print(dic['黄山'])
# 报错
# print(dic['不存在元素'])


print(dic.get('杭州'))
print(dic.get('不存在元素'))
print(dic.get('不存在元素'), 'new_value')
# setdefault 当Key存在时,不添加新value,根据Key返回value;当Key不存在时,添加新Value,并且
ret = dic.setdefault('黄山', '南方')
print(dic)
print(ret)
ret = dic.setdefault('华山', '南方')
print(dic)
print(ret)

# 字典的方法
dic = {"id": 123, "name": 'sylar', "age": 18, "ok": "科⽐"}
print(dic.keys())
# dict_keys(['id', 'name', 'age', 'ok']) 不⽤管它是什么.当成list来⽤就⾏
for key in dic.keys():
    print(key)

print(dic.values())
# dict_values([123, 'sylar', 18, '科⽐']) ⼀样. 也当list来⽤
for value in dic.values():
    print(value)

print(dic.items())
# dict_items([('id', 123), ('name', 'sylar'), ('age',18), ('ok', '科⽐')]) 这个东⻄也是list. 只不过list中装的是tuple
for key, value in dic.items():  # ?? 这个是解构
    print(key, value)

# 注意:
for k in dic:
    print(k)  # K仅仅为Key

# fromkey:第一个参数可以是可迭代对象,全部是新字典的Key,第二个参数是Vale,并且Key对应的value全部相同
dic = dict.fromkeys(['jay', 'jj'], ['周杰伦', '林俊杰', 1])
print(dic)
dic.get("jay").append("胡⼤")
print(dic)
# 结果 :{'jay': ['周杰伦', '林俊杰', 1, '胡⼤'], 'jj': ['周杰伦', '林俊杰', 1, '胡⼤']}
# 结果分析:当把字典当做value赋值给Key时,涉及到'列表深浅copy'     !!!!!
# 证明:
#         dic1 = dict.fromkeys(['jay', 'jj'], ['周杰伦', '林俊杰', 1])
#         for k,v in dic1.items():
#             print(id(v))
# 结果:      2749843967304
#           2749843967304
# 结论:fromkeys 里如果value是个列表,那么生成的字典的所有Value都是'同一个列表',改变其中一个,其他都会改变


# 删除key中带有'k'的元素
for k in dic:
    if 'k' in k:
        del dic[k]  # dictionary changed size during iteration, 在循环迭代的时候不允许进⾏删除操作
print(dic)

# 面试题
dic = {'a': '123'}
s = dic.fromkeys('王健林', '思聪')  # 会生成新字典
print('s',s)
print('dic', dic)

# 把要删除的元素暂时先保存在⼀个list中, 然后循环list, 再删除
dic = {'k1': 'alex', 'k2': 'wusir', 's1': '⾦⽼板'}
dic_del_list = []
# 删除key中带有'k'的元素
for k in dic:
    if 'k' in k:
        dic_del_list.append(k)
for el in dic_del_list:
    del dic[el]
print(dic)
