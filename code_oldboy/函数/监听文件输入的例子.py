'''
作者:lg
日期:2019/9/21
文件描述:
缺陷：
'''


# readline特点:!!!!!
# 读到文件末尾不会停下来,会一直读空内容返回回来,没有read的机制

# 第一种,不可以对打印内容进行扩展修改
# def tail(filename):
#     f = open(filename, 'r', encoding='utf-8')
#     while True:
#         line = f.readline().strip()
#         if len(line) > 2:
#             print(line)


# tail('监听文件输入的例子.txt')

# 第二种,生成器写法,可以对打印内容进行扩展修改
def tail_gene(filename):
    f = open(filename, encoding='utf-8')
    while True:
        line = f.readline().strip()
        yield line
        # 此处利用yield返回一个变量,并且不结束函数的特点,如果是return函数就结束了
        # 这里类似于一个range(1000000)的有庞大内容生成器,只不过全是'空字符串'


ta = tail_gene('监听文件输入的例子.txt')

for i in ta:  # 本质上是去找生成器里的yield,一直到执行完所有yield为止
    if i:
        print(i)

