
def deractor(func):
    def inner(*args, **kwargs):
        print('begin call')
        result = func(*args, **kwargs)
        print('end call')
        return result
    return inner

@deractor
def now():
    print('2018-9-8')

print(now())