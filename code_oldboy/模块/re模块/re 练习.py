'''
作者:lg
日期:2019/10/20
文件描述:
缺陷：
'''

import re

ret = re.findall('a', 'eva egon yuan a')  # 返回所有满足匹配条件的结果,放在列表里
print(ret)
# 结果:['a', 'a', 'a']

ret = re.search('a', 'eva egon yuan a').group()
print(ret)
# 结果:a
# 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,
# 该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

ret = re.match('a', 'abc').group()
print(ret)
# 结果:a
# 同search,不过只在字符串开始处进行匹配,其他位置出现并不会匹配

ret = re.split('[a]', 'abcd')
print(ret)
# 先以a分割,再以b分割,迭代分割
# 结果:->['', 'bcd']->['', '', 'cd']

ret = re.sub('\d', 'H', 'eva3egon4yuan4', 2)
print(ret)
# 结果:evaHegonHyuanH
# 将数字替换成'H'，参数1表示只替换1次

ret = re.subn('\d', 'H', 'eva3egon4yuan4', 3)
print(ret)
# 结果:('evaHegonHyuanH', 3)
# 返回一个元组,第一个元素表示最后结果,第二个表示替换的次数

obj = re.compile('\d{3}')  # 将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret = obj.search('abc123eeee')  # 正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())
# 结果:123

ret = re.finditer('\d', 'ds3sy4784a')
print(ret)  # 可迭代对象,<callable_iterator object at 0x0000023C7C770DD8>
for el in ret:
    print(el.group())  # 打印结果需要调用group方法才能返回匹配结果

# 1 findall的优先级查询：
ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
print(ret)
# ['oldboy']
# 分组优先:这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可

ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
print(ret)
# ret:['www.oldboy.com']

# '?'的三种用法
# 量词:匹配0次或一次
# 放在量词后面,表示惰性匹配
# 放在括号里,表示取消分组优先

# 2 split的优先级查询
ret = re.split('\d+', 'eva3egon4yuan')
print(ret)  # ['eva', 'egon', 'yuan']

ret = re.split('(\d+)', 'eva3egon4yuan')
print(ret)  # ['eva', '3', 'egon', '4', 'yuan']
# 这个在某些需要保留匹配部分的使用过程是非常重要的


# 综合练习与扩展
# 1、匹配标签
ret = re.search('<(?P<tag_name>\w+)>\w+</(?P=tag_name)>', '<h1>hello</h1>')
print(ret.group())
print(ret.group('tag_name'))
# 还可以在分组中利用?<name>的形式给分组起名字
# 获取的匹配结果可以直接用group('名字')拿到对应的值
# 后续如果遇到相同的分组字符串,可直接用?P=name来表示相同的匹配内容

# 2、匹配整数
ret = re.findall("\d+", "1-2*(60+(-40.35/5)-(-4*3))")
print(ret)  # 结果:['1', '2', '60', '40', '35', '5', '4', '3']

ret = re.findall("\d+\.\d+|\d+", "1-2*(60+(-40.35/5)-(-4*3))")
# 注意:'|' 当使用'或'符号时,一定要把长的放在前面,不然短的匹配完了就不会匹配长的了
print(ret)
# 结果:['1', '2', '60', '40.35', '5', '4', '3']
# 第一种方法:
ret = filter(lambda el: False if '.' in el else True, ret)
print(list(ret))  # 结果:['1', '2', '60', '5', '4', '3']

# 第二种方法:
ret = re.findall("\d+\.\d+|(\d+)", "1-2*(60+(-40.35/5)-(-4*3))")
print(ret)  # 结果:['1', '2', '60', '', '5', '4', '3']
# 为什么会有''出现:
# 分组优先,整个结果匹配上了,分组里的内容没匹配上,但是又必须去显示分组里的内容,只能显示空字符串了


