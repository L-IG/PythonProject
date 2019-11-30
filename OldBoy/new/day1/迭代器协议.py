
class List(list):
    # pass
    # def __init__(self,num):
    #     self.num = num

    def __iter__(self):
        print('执行iter')
        return self

    # def __next__(self):
    #     # self.num += 1
    #     # return self.num
    #     print('执行next')

# a = Foo(10)
# print(a.num)

# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# for i in a:
#     print(i)

b = List('abcd')

print(b)

for i in b:
    print(i)