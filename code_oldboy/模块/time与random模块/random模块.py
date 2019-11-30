'''
作者:lg
日期:2019/10/20
文件描述:
缺陷：
'''

import random

print(random.random())  # 大于0且小于1之间的小数
# 0.37902547699621136

print(random.uniform(1, 20))  # 大于1小于100的小数
# 5.974170103864822

print(random.randint(1, 5))  # 大于等于1且小于等于5之间的整数
# 5
print(random.randrange(1, 10, 2))  # 大于等于1且小于10之间的奇数(顾头不顾尾)
# 9

# 随机选择一个返回
print(random.choice([1, 'a', [1, 2]]))  # 参数是一个序列!!!
print(random.choice('abc'))

# 随机选择多个返回，返回的个数为函数的第二个参数
print(random.sample([1, '23', [4, 5]], 2))  # 参数是一个序列!!!
# [1, [4, 5]]
print(random.sample('abcdef', 3))
# ['e', 'c', 'd']

# 打乱列表顺序
item = [1, 3, 5, 7, 9]
random.shuffle(item)
print(item)
# 结果:[9, 1, 3, 5, 7]


# 生成一个4位随机验证码

word_l = []
for i in range(4):
    int_num = random.randint(0, 9)
    int_num = str(int_num)
    word_num = random.randint(65, 90)
    word = chr(word_num)
    choice = random.choice([int_num,word])
    print(choice)
    word_l.append(choice)
print(word_l)
print(''.join(word_l))