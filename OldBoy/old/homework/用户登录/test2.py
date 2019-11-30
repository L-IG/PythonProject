#对于从文件里读出来的字符串，可以用 strip，split函数操作，变成列表，是序列化的体现
#原因分析：每次k迭代出一行内容，包括换行符，k相当于一个字符串，就具有strip，split方法
with open('用户密码表.txt', 'r') as f:
    for k in f:
        print(k.strip().split())
