#很重要
#read一般不能放在循环里，read会一直读取文件内容，读完了就会读取空格
#用int前一定要注意 字符串一定不能为空，不能为字母
#if 和 else要一一对应；第一个if条件满足吼，不再执行后面的elif语句，甚至判断语句都不执行
#while循环里，如果有变量赋值的语句，一定要注意

goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},]

flag_buy = 1 # 1：默认读取文件余额直接购买；   0：文件余额为0时，需要重新输入工资
shopping_car = []
user_id = 'admin'
user_passwd = 'admin123'

while True:
    id = input("please input id:")
    passwd = input('please input password:')

    if id == user_id and passwd == user_passwd:
        print('Welcome!')
        f_txt = open('余额.txt', 'r')
        money_txt =  f_txt.read().strip()
        while True:
            if money_txt.isdigit():
                if int(money_txt) == 0:
                    flag_buy = 0
                else:
                    pass
            if flag_buy == 0:    #第一个if条件满足后，不再执行后面的elif语句，甚至判断语句都不执行
                salary = input('please input your salary:')
                if salary.isdigit() == True and int(salary) > 0:
                    salary = int(salary)
                    flag_buy = 1
                else:
                    print('Wrong salary input!')
            if flag_buy == 1:
                while True:
                    print('商品列表'.center(20, '-'))
                    for index, k in enumerate(goods):
                        print('%s.%s  %s' % (index, k['name'], k['price']))
                    money_txt = int(money_txt)
                    print('Now you have %s left' % money_txt)
                    choice = input('what good do you wan to buy? please input number:')
                    if choice.isdigit():
                        if int(choice) >= 0 and int(choice) <= 3:
                            choice = int(choice)
                            if money_txt >= goods[choice]['price']:
                                money_txt -= goods[choice]['price']
                                shopping_car.append(goods[choice])
                            else:
                                print('you have not enough monney!')
                        elif int(choice) < 0 or int(choice) > 3:
                            print('Wrong choice!')
                    elif 'q' == choice:
                        print('you have buy this good:')
                        for index, k in enumerate(shopping_car):
                            print('%s.%s  %s' % (index, k['name'], k['price']))
                        print('you have %s money left!' % (money_txt))
                        f = open('余额.txt', 'w')
                        f.write(str(money_txt))
                        exit()
    else:
        print('Wrong id or password!')


