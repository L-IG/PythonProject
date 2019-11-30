# def range2(n):
#     count =0
#     while count < n:
#         print('count',count)
#         count += 1
#         sign = yield count
#         print('-------sign',sign)
#     return 333
#
# new_range = range2(3)
# n1 = next(new_range)
#
# print('do sth else')
# new_range.send('stop!')

#yield关键字的另外一种使用形式：表达式形式的yield


def eater(name):
    print('%s 准备开始吃饭啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s 吃了 %s' % (name,food))
        food_list.append(food)
        if '鸡蛋' == food:
            print(food_list)

g=eater('egon')
g.send(None) #对于表达式形式的yield，在使用时，第一次必须传None，g.send(None)等同于next(g)
g.send('蒸羊羔')
g.send('蒸鹿茸')
g.send('蒸熊掌')
g.send('烧素鸭')
g.send('鸡蛋')
g.send('烧素鸭')
g.close()
# g.send('烧素鹅')
# g.send('烧鹿尾')