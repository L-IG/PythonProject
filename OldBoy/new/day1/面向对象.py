class A(object):
    def __init__(self):
        pass
    def run(self):
        print('A')

class B(object):
    def __init__(self):
        pass

    def run(self):
        print('B')


obj1 = A()
obj2 = B()



def run(obj):
    obj.run()

run(obj1)
run(obj2)