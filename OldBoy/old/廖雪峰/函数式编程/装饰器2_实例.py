import functools
from inspect import isfunction

def logger(arg=''):
    if type(arg) == str or not arg:
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print(arg + ' begin call')
                fw = fn(*args, **kw)
                print(arg + ' end call')
                return fw
            return wrapper
        return decorator
    if isfunction(arg):
        @functools.wraps(arg)
        def warpper(*args, **kw):
            print('begin call')
            fw = arg(*args, **kw)
            print('end call')
            return fw
        return warpper

@logger('excute')
def a(name):
    return name

@logger
def b(name):
    return name

A = a('Test A')
print(A)
print()
B = b('Test B')
print(B)