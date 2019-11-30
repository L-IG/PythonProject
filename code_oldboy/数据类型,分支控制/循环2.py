'''
作者:lg
日期:2019/8/30
文件描述:打印1到100之间的所有奇数
缺陷：
'''

i = 0
while True:
    i += 1
    if i % 2 == 1:
        print(i)
    if i == 100:
        break