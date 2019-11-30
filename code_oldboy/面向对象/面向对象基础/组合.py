'''
作者:lg
日期:2019/11/3
文件描述:
缺陷：
'''


class Person():
    def __init__(self, name, aggr, hp, price):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.price = price

    def attack(self, dog):
        dog.hp -= self.aggr
        print(f'{self.name}攻击了{dog.name},{dog.name}还剩{dog.hp}血')

    def get_weapon(self, weapen):
        if self.price >= weapen.price:
            self.price -= weapen.price
            self.weapen = weapen
            self.aggr += weapen.aggr
        else:
            print('余额不足,请充值!')


class Dog():
    def __init__(self, name, aggr, hp):
        self.name = name
        self.hp = hp
        self.aggr = aggr

    def bite(self, person):
        person.hp -= self.aggr
        print(f'{self.name}攻击了{person.name},{person.name}还剩{person.hp}血')


class Weapon():
    def __init__(self, name, aggr, njd, price):
        self.name = name
        self.aggr = aggr
        self.njd = njd
        self.price = price

    def hand_eighteen(self, obj):
        obj.hp -= self.aggr * 2


alex = Person('alex', 1, 100, 1000)
Jin = Dog('Jin', 90, 1000)
alex.attack(Jin)
Jin.bite(alex)

w = Weapon('打狗棒', 100, 3, 998)
alex.get_weapon(w)
print(alex.aggr)
alex.weapen.hand_eighteen(Jin)
print(Jin.hp)

# 组合:
# 对象的一个属性是另一个对象
# 组合表示什么对象有什么对象,其中一个包含另外一个


# 圆
# 圆环
import math


class Cirle():
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r


class Ring():
    def __init__(self, R, r):
        self.R = Cirle(R)  # 这里圆环的R直接赋值成一个圆的对象
        self.r = Cirle(r)

    def area(self):
        return self.R.area() - self.r.area()

    def perimeter(self):
        return self.R.perimeter() + self.r.perimeter()


R1 = Ring(10, 5)
print(R1.perimeter())
print(R1.area())


# 老师
# 生日
# 老师拥有生日
class Teacher():
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday


class Birth():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


b1 = Birth('1993', '12', '09')
t1 = Teacher('egon', b1)
print(t1.birthday.year)
print(t1.birthday.month)
print(t1.birthday.day)
