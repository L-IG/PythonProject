'''
作者:lg
日期:2019/11/2
文件描述:
缺陷：
'''


# 练习一：在终端输出如下信息
#
# 小明，10岁，男，上山去砍柴
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山去砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健

class People():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def mountain(self):
        print(f'{self.name},{self.age}岁,{self.sex},上山去砍柴')

    def drive(self):
        print(f'{self.name},{self.age}岁,{self.sex},开车去东北')

    def favor(self):
        print(f'{self.name},{self.age}岁,{self.sex},最爱大保健')


xiaoming = People('小明', 10, '男')
laoli = People('老李', 90, '男')
xiaoming.mountain()
xiaoming.drive()
xiaoming.favor()
laoli.mountain()
laoli.drive()
laoli.favor()


# 正方形(r) 周长和面积

class Zhengfangxing():
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2

    def perimeter(self):
        return 4 * self.r


z = Zhengfangxing(10)


# print(z.area())   100
# print(z.perimeter())  40

class Person():
    def __init__(self, name, ki, hp):
        self.name = name
        self.hp = hp
        self.ki = ki

    def attack(self, dog):
        dog.hp -= self.ki
        print(f'{self.name}攻击了{dog.name},{dog.name}还剩{dog.hp}血')


class Dog():
    def __init__(self, name, ki, hp):
        self.name = name
        self.hp = hp
        self.ki = ki

    def bite(self, person):
        person.hp -= self.ki
        print(f'{self.name}攻击了{person.name},{person.name}还剩{person.hp}血')


alex = Person('alex', 1, 100)
dd = Dog('Jin', 90, 1000)
# alex.attack(dd) alex攻击了Jin,Jin还剩999血
# dd.bite(alex)   Jin攻击了alex,alex还剩10血
