'''
作者:lg
日期:2019/11/4
文件描述:
缺陷：
'''


class Student(object):
    menu = {'选择班级': '',
            '查看自己信息': ''
            }

    def __init__(self, name):
        self.name = name
