# def add_end(L=[]):
#     a = 'aaa'
#     print('id(a) ',id(a))
#     # print(id(L))
#     L.append('END')
#     return L
#
# print(add_end())
# print(add_end())


# def add_1(a,b):
#     print(id(a))
#     return a + b
#
# print(add_1(10,20))
# print(add_1(10,20))


# def foo(x,y,z):
#     print(x,y,z)
# foo(*(1,2,3))

# def person(name, age, *args, city, job):
#     print(name, age, city, job)
#
# person('Jack', 24, city='Beijing', job='Engineer')

def counter():
    n = 0
    def incr():
        nonlocal n
        x = n
        n += 1
        return x
    return incr

c = counter()
print(c())
print(c())
print(c())
print(c.__closure__[0].cell_contents)  # 查看闭包的元素