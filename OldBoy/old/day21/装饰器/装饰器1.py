#在原有的模块上增加另一个功能模块，如果直接修改原函数代码，则违反了 封闭-开放 原则

login_state = False

def login():
    global login_state
    if False == login_state:
        id = input('please input ID:')
        passwd = input('please input passwd:')

        if id == 'admin' and passwd == 'admin123':
            print('Welcome', id)
            login_state = True
        else:
            print('Wrong id or passwd')
    else:
        print('you have logined!')


def home():
    print("---首页----")

def beijing():
    print("----北京----")

def shanghai():
    login()
    print("----上海----")

def hangzhou():
    login()
    print("----杭州----")


hangzhou()
shanghai()