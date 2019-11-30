

def deractor(*style):
    def outter(func):
        def inner(*args, **kwargs):
            print('begin call',style)
            return func(*args, **kwargs)
        return inner
    return outter

@deractor('style')
def now():
    print('2018-9-8')

@deractor() #这里的“style”是实参
def now_other():
    print('now_other')

now()
now_other()
