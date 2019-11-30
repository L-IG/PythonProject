'''
作者:lg
日期:2019/9/28
文件描述:
缺陷：
'''

# 写生成器实现：有一个文件，从文件里分段读取内容
# readline
# read(10)
# 在读出来的内容前面加上一个'***'，再返回给调用者

FileName = '迭代器,生成器的练习.txt'


def generator():
    with open(FileName, encoding='utf -8') as f:
        while True:
            line = f.readline().strip()
            if line:
                yield f"***{line}"


# g1 = generator()
# for i in g1:
#     print(i)

# 处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕
def gener2(filename, content):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if content in line:
                yield line


g = gener2(FileName, '人民')
for i in g:
    print(i)


# 生成器面试题
# 生成器只要不取值,里面代码就不执行!!!!!
def add(n, i):
    return n + i


def test():
    for i in range(4):
        yield i


g = test()
# for n in [1, 10]:
#     g = (add(n, i) for i in g)

# 分解为下面的code
# 注意:到了最后list方法才执行生成器,n到最后一步才确定具体值
# 但凡遇到for循环套生成器的表达式,都拆开来看!!!!!
n = 1
g = (n + i for i in g)
n = 10
g = (10 + i for i in (10 + i for i in [0, 1, 2, 3]))
print(list(g))


def demo():
    for i in range(4):
        yield i


g = demo()

g1 = (i for i in g)
g2 = (i for i in g1)

print(list(g))
print(list(g1))
print(list(g2))
