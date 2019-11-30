'''
作者:lg
日期:2019/11/4
文件描述:
缺陷：
'''


class Classes(object):
    def __init__(self, name, school, kind, students):
        self.name = name  # 班级名
        self.school = school  # 学校
        self.kind = kind  # 科目(courses对象) linux,python,go
        self.students = students  # 一个路径,存放所有学生对象的文件名字
        self.teachers = []


class Courses(object):
    def __init__(self, name, period, price):
        self.name = name  # 课程名
        self.period = period  # 周期
        self.price = price  # 价格


class Teacher(object):
    menu = {'查看自己班级': '',
            '查看自己课程': '',
            '查看自己学生': '',
            }

    def __init__(self, name, school):
        self.name = name  # 名字
        self.school = school  # 学校
        self.classes = []  # 老师拥有的班级

    def query_classes(self):
        pass

    def query_courses(self):
        pass

    def query_students(self):
        pass
