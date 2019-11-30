#方法千万不能与属性同一个名字
#最好是将属性编程私有属性
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


stu1 = Student()
stu1.birth = 100
print(stu1.birth)

#stu1.age = 200
#age没有set方法
print(stu1.age)

