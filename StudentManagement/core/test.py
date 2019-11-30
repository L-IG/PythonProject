'''
作者:lg
日期:2019/11/9
文件描述:
缺陷：
'''

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#
# t1 = Student('xiaoming')
# t2 = Student('hua')
#
# t1.classes = 'beijing'
#
# print(hasattr(t1, 'classes'))
# print(hasattr(t2, 'classes'))
# print(getattr(t1, 'classes'))

# LIST_GO = [1, 2, 3, 4, 5]
# print(id(LIST_GO))
#
#
# def func(list1):
#     print(id(list1))
#     list1 = []  # 传列表时,相当于传了一个内存地址,不能再用赋值语句,不然新的变量就不是内存地址的值了!!!!!
#     # 给可变对象传值,都是传地址,只能使用对象所拥有的的'.'方法,不能再进行赋值
#     print(id(LIST_GO))
#     print(id(list1))
#
#
# func(LIST_GO)
# print(LIST_GO)

import pickle
