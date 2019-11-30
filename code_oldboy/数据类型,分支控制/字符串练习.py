'''
作者:lg
日期:2019/9/1
文件描述:字符串练习
缺陷：
'''

# 使用for循环对s = '321'进行循环，打印内容依次是：‘倒计时3秒’，‘倒计时2秒’,‘倒计时1秒’,‘出发’
s = '321'
for i in s:
    print('倒计时%s秒' % (i))
else:
    print('出发')

# 实现一个加法计算器，例如用户输入字符串 ' 5 + 9 '
# user_input = input('请输入内容：').strip()
# if '+' in user_input:
#     num1, num2 = user_input.split('+')
#     num1 = num1.strip()
#     num2 = num2.strip()
#     if num1.isdigit() and num2.isdigit():
#         num1 = int(num1)
#         num2 = int(num2)
#         print('结果为：',num1 + num2)
#     else:
#         print('输入的不是数字！')
# else:
#     print('没有加号！')


# 实现一个加法(多个数字)计算器，例如用户输入字符串 ' 5 + 9 +11 +1'
# user_input = input('请输入内容：').strip()
# sum = 0
# if '+' in user_input:
#     num_list = user_input.split('+')
#     for num in num_list:
#         num = num.strip()
#         num = int(num)
#         sum += num
# print(sum)


# 计算用户输入的内容中有几个整数
content = 'sghdgs23424uk2g3k24k1jh31'
count = 0
for i in content:
    if i.isdigit():
        count += 1
print(count)

# 复杂流程控制
info1 = '''
A:走大路
B:走小路
C:绕路回家
'''
info2 = '''
A1:公交车
A2:步行
'''
info3 = '''
C1:游戏厅玩一会
C2:网吧玩会
'''
flag = True
# while flag:
#     print(info1)
#     user_input= input('请输入回家方式').strip().upper()
#     if user_input == 'A':
#         print('您选择走大路回家，请继续选择')
#         while True:
#             print(info2)
#             choice = input('请输入回家方式').strip()
#             if choice == 'A1':
#                 print('10分钟到家')
#                 flag = False
#                 break
#             elif choice == 'A2':
#                 print('20分钟到家')
#                 flag = False
#                 break
#             else:
#                 print('请输入正确的数')
#     elif user_input == 'B':
#         print('您选择走小路回家')
#         break
#     elif user_input == 'C':
#         print('您选择绕路回家，请继续选择')
#         while True:
#             print(info3)
#             choice = input('请输入回家方式').strip()
#             if choice == 'C1':
#                 print('一个半小时到家，爸爸在家，拿棍等你')
#                 flag = False
#                 break
#             elif choice == 'C2':
#                 print('两个小时到家，妈妈已做好了准备')
#                 flag = False
#                 break
#             else:
#                 print('请输入正确的数')


# 计算 1- 2 + 3 - 4 ... +99 除了88以外所有数的总和
# 第一种
count = 1
sum = 0
while count < 100:
    if count == 88:
        count += 1
        continue  # 在用continue结束后面代码之前，先把count计数加一
    if count % 2 == 0:
        sum -= count
    else:
        sum += count
    count += 1
print('sum', sum)
# 第二种
count = 0
sum = 0
while count < 99:
    count += 1
    if count == 88:
        continue
    if count % 2 == 0:
        sum -= count
    else:
        sum += count
print('sum', sum)

# 回文判断，考字符串逆序
s = '上海自来水来自海上'
# 1、切片
s1 = s[::-1]
print('s1', s1)
if s1 == s:
    print('是回文句子')
else:
    print('不是回文句子')

# 返回一个字符串中数字，大写字母，小写字母，特殊字符的个数
str1 = 'sdsdADCd12sfds多少f34233sd时代'

digit_num = 0
upper_num = 0
lower_num = 0
other_num = 0
for i in str1:
    if i.isdigit():
        digit_num += 1
    elif i.isupper():
        upper_num += 1
    elif i.islower():
        lower_num += 1
    else:
        other_num += 1
print('digit_num,upper_num,lower_num,other_num', digit_num, upper_num, lower_num, other_num)

