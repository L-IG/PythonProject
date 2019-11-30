'''
作者:lg
日期:2019/9/10
文件描述:老男孩第一次试题
缺陷：
'''

# 1
# 变量名有字母,数字,下划线组成,其中变量不能以受罪开头

# 2
# 一字节等于8位,程序里常用两个16进制数表示一个字节,\xe4

# 3
# '二哥'用utf-8时,占3个字节,gbk占两个字节

# 4
# 字符串的常见功能:startwith,endwith,upper,lower,isupper,islower,join,split,strip,isdigit,isalnum,index,find,count

# 5
# 数字:0,字符串:'',列表:[],元组:(),字典:{}

# 6
# py2:xrange,内存里的编码格式默认以什么打开就是什么,
# py3:range,内存里的编码被转化为unicode,

# 7
li = [1, 3, 2, 'a', 4, 'b', 5, 'c']
l3 = li[::2]
print(l3)
l4 = li[1:6:2]
print(l4)
l5 = li[-1:]
print(l5)
l6 = li[-3:-8:-2]
print(l6)

# 8(a)
lis = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
lis[0][1][2]['k1'][0] = lis[0][1][2]['k1'][0].upper()
lis[0][1][2]['k1'][0] = 'TT'

lis[0][1][2]['k1'][1] = '100'
print(lis[0][1][2]['k1'][1])

lis[0][1][2]['k1'][2] = 101
print(lis[0][1][2]['k1'][2])

# 8(b)
dic = {'K1': 'V1', 'K2': ['alex', 'sb'], (1, 2, 3, 4, 5): {'K3': ['2', 100, 'wer']}}
dic['K2'].append('23')
dic['K2'].insert(0, 'a')
dic[(1, 2, 3, 4, 5)].setdefault('K4', 'V4')
dic[(1, 2, 3, 4, 5)].setdefault((1, 2, 3), 'ok')
dic[(1, 2, 3, 4, 5)]['K3'][2] = 'qq'
print(dic)

# 9
print(int('9999'))
print(str(1213))

print(int(True))
print(int(False))
print(bool(1))
print(bool(0))

print(bool(''))
print(bool(' '))
print(str(True))
print(str(False))

print('---'.join(['a', 'b', 'c', '123']))
# 注意:join参数序列里不能有整形数字,必须是str
print('a---b---c---123'.split('---'))

# 10
print(''.join(['alex', 'wusir', 'rain']))
print('*'.join(['alex', 'wusir', 'rain']))

print('alexwusiralex'.split('l', 1))
print('alex wusir'.split(' ', 1))

s = 'alex'
s1 = ''
for i in s:
    tmp = i + '_'
    s1 += tmp
print(s1[0:-1])

# 分别使用while 和for 循环打印 1-2+3-4+5......+99
count = 1
sum1 = 0
while count < 100:
    if count % 2 == 0:
        sum1 -= count
    else:
        sum1 += count
    count += 1
print(sum1)

sum2 = 0
for i in range(1, 100):
    if i % 2 == 0:
        sum2 -= i
    else:
        sum2 += i
print('sum2', sum2)

# 12
for i in range(100, -1, -1):
    print(i, end=' ')
print('\n')

# 13
user_input = 'p1w2e4t6u8o'
count = 0
for index, value in enumerate(user_input):
    if index % 2 == 1:
        if value.isdigit():
            count += 1
print(count)

# 15
li = ['tai b ai', 'al  e xC', 'A  bc', 'e  gon', 'Riti an', 'Wu s ir', 'a q  c']

for i, el in enumerate(li):
    if ' ' in el:
        li[i] = el.replace(' ', '')
print(li)

l = []
for el in li:
    if (el.startswith('A') or el.startswith('a')) and el.endswith('c'):
        l.append(el)
print(l)

# 16
user_input = '6+ 9+ 18+  2+ 10'
num = user_input.split('+')
print(num)
sum1 = 0
for i in num:
    sum1 += int(i.strip())
print(sum1)
dic1 = {'最终计算结果': None}
dic1.setdefault('最终计算结果', sum1)

# 17
user_list = [
    {'username': 'barry', 'password': '1234'},
    {'username': 'alex', 'password': 'asdf'},
]
board = ['张三', '李四', '王二麻子']
while True:
    list1 = {}
    username = input('请输入用户名或退出Q:').strip()
    if 'Q' == username.upper():
        break
    password = input('请输入用密码:').strip()
    if username in board:
        username = '*' * len(username)
    if username and password:
        list1.setdefault('username', username)
        list1.setdefault('password', password)
        print('成功添加一名员工:',end=' ')
        print(list1)
    user_list.append(list1)

print('user_list', user_list)
