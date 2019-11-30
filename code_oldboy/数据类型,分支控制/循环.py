'''
作者:lg
日期:2019/8/30
文件描述:计算1+2+。。。+100
缺陷：
'''

# for循环
# Sum = 0
# for i in range(101):
#     Sum = Sum + i
# print(Sum)

# while循环
i = 0
sum = 0
while True:
    i += 1
    sum = sum + i
    if i == 100:
        break
print(sum)



