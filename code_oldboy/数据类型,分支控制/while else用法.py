'''
作者:lg
日期:2019/8/31
文件描述:while else的用法
缺陷：
'''

# 正常用法
count = 0
while count < 10:
    count += 1
    print(count)
else:
    print('进入else分支，证明while循环全部执行完毕')


# 带break的情况
count = 0
while count < 10:
    count += 1
    print(count)
    if count == 6:
        break       # 当执行了break后，不再执行else语句了，说明循环被打断了，没有执行完整
else:
    print('进入else分支，证明while循环全部执行完毕')