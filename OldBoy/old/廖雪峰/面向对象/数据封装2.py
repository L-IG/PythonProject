class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age
        return self.__age

stu1 = Student("'xiaoming", 18)
#外部无法访问__私有属性
#print(stu1.__name)

print(stu1.get_age())
print(stu1.set_age(15))