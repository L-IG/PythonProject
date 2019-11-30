'''
作者:lg
日期:2019/9/6
文件描述:综合练习
缺陷：
'''

# 接受10个分数,每次输入的数字必须是在5~10之间
# l = []
# count = 0
# while count < 10:
#     user_input = input('请输入分数').strip()
#     if user_input.isdigit():
#         if 10 >= int(user_input) >= 5:
#             print('分数OK')
#             l.append(int(user_input))
#         else:
#             print('分数不在范围')
#             continue
#     else:
#         print('不是数字')
#         continue
#     count += 1
# sum = 0
# for i in l:
#     sum += i
# print(sum / 10)

# 电影投票
# lst = ['复仇者联盟', '解救吾先生', '美国往事', '西西里的美丽传说']
# # dic = {'复仇者联盟': '', '解救吾先生': '', '美国往事': '', '西西里的美丽传说': ''}
# dic = {}
# for el in lst:
#     user_input = input('请给电影打分: {}'.format(el)).strip()
#     if user_input.isdigit():
#         dic.setdefault(el, user_input)
#     else:
#         print('不是数字')
#         continue
# print(dic)

# 念数字
# 缺陷:对输入没有校验
# dic = {
#     '-': 'fu',
#     '0': 'ling',
#     '1': 'yi',
#     '2': 'er',
#     '3': 'san',
#     '4': 'si',
#     '5': 'wu',
#     '6': 'liu',
#     '7': 'qi',
#     '8': 'ba',
#     '9': 'jiu',
#     '.': 'dian'
# }
# user_input = input('请输入数字:').strip()
# l = []
# for el in user_input:
#     l.append(dic[el])
# print(l)
# Snum = ''
# if '-' in user_input:
#     _, user_input = user_input.split('-')
#     if '.' in user_input:
#         user_input, Snum = user_input.split('.')
# else:
#     if '.' in user_input:
#         user_input, Snum = user_input.split('.')
# print('整数部分', user_input)
# print('小数部分', Snum)

# 车牌区域划分
# 结果:{'黑龙江':2, '北京':1,...}
# setdefault-->一次很精妙的用法   !!!!!
# setdefault-->此次用作计数作用,代码走两个分支,没有出现过的key,Value赋初值0,出现过Key,Value就迭加
cars = ['鲁A324343', '鲁A324273', '京H232334', '黑K232424', '黑K232424', '黑M2332424', '沪S2131233', '沪S2131233']
localS = {'沪': '上海', '黑': '黑龙江', '鲁': '山东', '京': '北京'}
dic2 = {}
for el in cars:
    ret_province = localS.setdefault(el[0])
    dic2.setdefault(ret_province, 0)  # setdefault作用-->给每个Key赋一个初值,或字符串,或整型数字
    dic2[ret_province] = dic2[ret_province] + 1
print(dic2)

# 如果没有想到setdefault的好处,只能用下面这种笨方法了
# dic2 = {}
# l = []
# for el in cars:
#     ret_province = localS.setdefault(el[0])
#     l.append(ret_province)
#     dic2.setdefault(ret_province,0)
# print(dic2)
# print(l)
# for i in l:
#     dic2[i] += 1
# print(dic2)


#
zhubo = {'卢本伟': 122000, '冯提莫': 18999, '金老板': 99999, '吴老板': 2500000, 'alex': 126}
count = 0
for el in zhubo.values():
    count += el
avg = count / len(zhubo)
print('平均值', avg)
l1 = []
for k, v in zhubo.items():
    if v < avg:
        l1.append(k)
print(l1)
del zhubo['卢本伟']
print(zhubo)