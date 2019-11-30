'''
作者:lg
日期:2019/8/31
文件描述:利用while语句写出猜大小的游戏
缺陷：
'''

# 用户输入的数guess_num，本来存在的数number_act，通过逻辑来让流程走不同的分支处理
number_act = 66
while True:
    guess_num = int(input('请输入一个数字:'))
    if guess_num > number_act:
        print('猜大了')
    elif guess_num < number_act:
        print('猜小了')
    else:
        print('猜对了')
        break

# 升级版
flag= 0
number_act = 66
while True:
    guess_num = int(input('请输入一个数字:'))
    if guess_num > number_act:
        print('猜大了')
    elif guess_num < number_act:
        print('猜小了')
    else:
        print('猜对了')
        break
    flag += 1
    if flag == 3:
        print('猜错3次了')
        break