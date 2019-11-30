'''
作者:lg
日期:2019/9/7
文件描述:综合练习
缺陷：
'''

# 判断一个数是否水是仙花数,三位数,满足条件个十百三个数字的三次方之和等于这个数,如 153 = 1 ** 3 + 5 ** 3 + 3 ** 3
# user_num = input('请输入数字:').strip()
# if user_num.isdigit():
#     if len(user_num) == 3 and not user_num.startswith('0'):
#         if int(user_num[0]) ** 3 + int(user_num[1]) ** 3 + int(user_num[2]) ** 3 == int(user_num):
#             print('这个数字是水仙花数字')
#         else:
#             print('该数字不是水仙花数字')
#     else:
#         print('不是三位数或者以0开头!')
# else:
#     print('不是数字!')

# 冒泡排序
# 数据交换第一种
# a = 10
# b = 20
# # a, b = b, a
# # print(a,b)
# 数据交换第二种
# tmp = a
# a = b
# b = tmp
# print(a, b)

lis = [100, 23, 9, 4, 19, 5, 34, 56, 2, 7, 3, 192]
len1 = len(lis)
for el in range(len1 - 1):  # 如果第一次要比较11个数就可以让12个数当中的一个确定好位置,总共需要11次(最后一个数不需要和其他数字比了)
    for i in range(len1 - el - 1):  # 如果有12个数要比较,当前只需要比较11次即可
        if lis[i] > lis[i + 1]:
            lis[i], lis[i + 1] = lis[i + 1], lis[i]
print(lis)
# 总结规律:
# 每一次循环需要把当前最大的数字移到最右边,那这次循环之后,这个数字已经确定好位置了,相当于整个列表扣掉了一个元素
# 那么整个列表有n个数字的话,需要做这个循环n-1次,就能把整个列表的元素排序完

# 另一种易懂的写法
lis = [100, 23, 9, 4, 19, 5, 34, 56, 2, 7, 3, 192, 89, 59]
len1 = len(lis)
count = 0
for k in range(len1 - 1):  # 需冒泡11次,才能排序完
    for i in range(len1 - 1 - count):  # 让一个数字冒出来
        if lis[i] > lis[i + 1]:
            lis[i], lis[i + 1] = lis[i + 1], lis[i]
    count += 1
print(lis)

# 36 选 7
import random

l = []
while True:
    num = random.randint(1, 36)
    if num not in l:
        l.append(num)
    if len(l) == 7:
        break
print('l', l)

# 用set集合去重的特点
set1 = set()
while len(set1) < 7:
    set1.add(random.randint(1, 36))
print('set1', set1)

# 4
while True:
    user_num = input('请输入收入:').strip()
    if user_num.isdigit():
        user_num = int(user_num)
    else:
        continue
    break
if user_num <= 2000:
    print('免税')
elif 4000 > user_num > 2000:
    user_num = 2000 + (user_num - 2000) * (1 - 0.03)
elif 6000 > user_num > 4000:
    user_num = 2000 + 2000 * (1 - 0.03) + (user_num - 4000) * (1 - 0.05)
elif 10000 > user_num > 6000:
    user_num = 2000 + 2000 * (1 - 0.03) + 2000 * (1 - 0.05) + (user_num - 6000) * (1 - 0.08)
else:
    user_num = 2000 + 2000 * (1 - 0.03) + 2000 * (1 - 0.05) + 4000 * (1 - 0.08) + (user_num - 10000) * (1 - 0.2)
print(user_num)
