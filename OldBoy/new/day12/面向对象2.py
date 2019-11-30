class A:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
        return False

    def __hash__(self):
        return hash(self.name + self.sex)

a = A('alex','nan',38)
b = A('alex','nan',39)


print(set((a,b)))