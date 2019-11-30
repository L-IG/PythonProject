#在原有的模块上增加另一个功能模块，如果直接修改原函数代码，则违反了 封闭-开放 原则
#把原函数当做参数传入新模块里，相当于执行了新模块的代码之后再执行原函数的代码，但是，改变了调用方式，整个工程里其他调用次函数的地方都得修改

login_state = False

def login(fun):
    global login_state
    if False == login_state:
        id = input('please input ID:')
        passwd = input('please input passwd:')

        if id == 'admin' and passwd == 'admin123':
            login_state = True
        else:
            print('Wrong id or passwd')
    else:
        print('you have logined!')
        #fun()
        #if与else对立，走了if分支就不能走else分支，fun（）不能放在此处

    if login_state == True:
        fun()

def home():
    print("---首页----")

def beijing():
    print("----北京----")

def shanghai():
    print("----上海----")

def hangzhou():
    print("----杭州----")

login(hangzhou)
login(shanghai)

#hangzhou = login(hangzhou)
#shanghai = login(shanghai)
#这种修改不会改变调用方式，但是调用时间出了问题
#可以用返回函数，闭包解决这个问题