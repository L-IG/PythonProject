'''
作者:lg
日期:2019/8/31
文件描述:and和or的另一种用法：当or两边都是数字时
缺陷：
'''

#  x or y规则：如果x == 0，结果为 y；如果x != 0，结果为x
# 就是判断第一位是不是0
print(1 or 2)
print(2 or 3)
print(0 or 3)
print(0 or 4)

# and的规则与or相反，记一个or就够了,容易混淆
print(1 and 2)
print(2 and 3)
print(0 and 3)
print(0 and 4)

# 先计算and，再计算or
print(1 or 2 and 3)

# 先把True和False计算出来
print(2 > 5 and 3)
print(2 < 1 and 4 > 6 or 3 and 4 > 5 or 6)

# 练习
print(8 or 3 and 4 or 2 and 0 or 9 and 7)
print(8)

print(0 or 2 and 3 and 4 or 6 and 0 or 3)
print(4)

# 'True(False)' 与 '数字' 进行逻辑运算时
# 符合上面规律,True是1,False是0
print(True or 1)
print(1 or True)

print(True and 1)
print(1 and True)

print(False or 1)
print(1 or False)

print(False and 1)
print(1 and False)