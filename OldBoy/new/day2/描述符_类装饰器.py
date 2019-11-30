
class LazyProperty():
    def __init__(self,func):
        print('----->')
        self.func = func
        print(func)



class Room():

    def __init__(self,width,lenth):
        self.width = width
        self.lenth = lenth

    @LazyProperty
    def area(self):
        return self.width * self.lenth

r1 = Room(10,10)
