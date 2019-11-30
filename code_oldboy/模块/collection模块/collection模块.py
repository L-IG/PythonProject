'''
作者:lg
日期:2019/10/20
文件描述:
缺陷：
'''

# 在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。
# 1.namedtuple: 生成可以使用名字来访问元素内容的tuple
# 2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
# 3.Counter: 计数器，主要用来计数
# 4.OrderedDict: 有序字典
# 5.defaultdict: 带有默认值的字典

# namedtuple
from collections import namedtuple

Point = namedtuple('POINT', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(p.y)

# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
circle = namedtuple('CIRCLE', ['x', 'y', 'r'])
c = circle(0, 0, 20)
print(c)

# queue
import queue

q = queue.Queue()
q.put(10)
q.put(10)
print(q.get())
print(q.get())
# print(q.get()) # 当队列里没有元素时,程序会阻塞在这里
# 对用户来说是越过黑盒子,不用关注它到底是什么,只要了解它到底有什么用就可以了


# deque 双向队列
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque

q = deque(['a', 'b', 'c'])
print(q)  # deque(['a', 'b', 'c'])
q.append('X')
q.appendleft('Y')
print(q)  # deque(['Y', 'a', 'b', 'c', 'X'])
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：

from collections import OrderedDict

d = dict((('a', 1), ('b', 2), ('c', 3)))
print(d)  # dict的Key是无序的

od = OrderedDict((('a', 1), ('b', 2), ('c', 3)))
print(od)  # 有序 OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序


# defaultdict
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66 , 'k2': 小于66}

values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
my_dict = {}
# 第一种:
for val in values:
    if val >= 66:
        if not 'k1' in my_dict:
            my_dict['k1'] = [val]
        else:
            my_dict['k1'].append(val)
    else:
        if not 'k2' in my_dict:
            my_dict['k2'] = [val]
        else:
            my_dict['k2'].append(val)
print(my_dict)

# 第二种:
from collections import defaultdict

values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# 字典里所有的Key新创建就有个默认值,是[]
my_dict = defaultdict([])
for i in values:
    if i >= 66:
        my_dict['k1'].append(i)
    else:
        my_dict['k2'].append(i)
print(my_dict)

dd = defaultdict(lambda: 10)
# defaultdict参数里必须是个函数对象, 可被调用
