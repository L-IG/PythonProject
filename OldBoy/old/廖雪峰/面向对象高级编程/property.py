class  Student(object):
    #def get_score(self):
    @property
    def get_score(self):
        return self.__score

    #def set_score(self, score):
    @get_score.setter
    def set_score(self, score):
        if not isinstance(score, int):
            raise  ValueError("score must be a inter!")
        if score < 0 or score > 100:
            raise ValueError("超出范围！")
        self.__score = score



stu1 = Student()
#stu1.set_score(101)
#stu1.set_score('111')
stu1.score = 99
print(stu1.score)
#stu1.score




