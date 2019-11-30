class Person():
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2

    @property
    def name(self):
        return self.name1 + '*****'        #self.name1 + '*****'  只能修改self.name1，而'*****'是必须加上的

    @name.setter
    def name(self,new_name):
        print('@name.setter')
        self.name1 = new_name

p1 = Person('xiaoming','dabao')
print(p1.name)


p1.name = 'HH'
print(p1.name)