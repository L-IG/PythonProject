class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    #类里面的方法，提供给外部访问自己数据的接口
    def GetScore(self):
        print(self.name+' is '+str(self.score))

#外部函数访问类里面的数据
def print_score(std):
    print(std.score)

student1 = Student('xiaoming', 99)

#print_score(student1)

student1.GetScore()

student2 = Student('xiaohua', 100)
student2.height = 170

#
#print_score(student1.heitht)
