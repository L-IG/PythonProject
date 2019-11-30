'''
作者:lg
日期:2019/8/31
文件描述:使用while循环输入1 2 3 4 5 6 8 9 10
缺陷：
'''

count = 0
while count < 10:
    count += 1
    if count == 7:
        continue    # continue结束本次循环
    print(count)


# 练习
# 求1-100的所有数之和
sum1 = 0
count = 1
while count <= 100:
    sum1 += count
    count += 1
print(sum1)

# 输出1-100内所有奇数
count = 1
while count <= 100:
    if count % 2 == 1:
        print(count)
    count += 1

# 输出1-100内所有偶数
count = 1
while count <= 100:
    if count % 2 == 0:
        print(count)
    count += 1

# 求1-2+3-4+5-6...+99
count = 1
sum1 = 0
while count <= 99:
    if count % 2 == 0:
        sum1 -= count
    else:
        sum1 += count
    count += 1
print(sum1)
