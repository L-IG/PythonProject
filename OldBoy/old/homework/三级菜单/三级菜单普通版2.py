menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


while True:
    for k in menu:
        print('第一级:', k)#习惯上把打印放在input前面
    s1 = input('choice1:').strip()
    if not s1: continue #用continue语句来结束后面语句的执行
    if s1 in menu:
        while True:
            for k in menu[s1]:
                print('第二级：', k)
            s2 = input('choice2:').strip()
            if not s2: continue
            if s2 in menu[s1]:
                while True:
                    for k in menu[s1][s2]:
                        print('第三级', k)
                    s3 = input('choice3:').strip()
                    if not s3: continue
                    if s3 in menu[s1][s2]:
                        while True:
                            for k in menu[s1][s2][s3]:
                                print('第四级',k)
                            s4 = input('退出上一级or退出程序:').strip()
                            if 'b' == s4:
                                break
                            elif 'q' == s4:
                                exit()
                    elif 'b' == s3:
                        break
                    elif 'q' == s3:
                        exit()
                    else:
                        print('节点不存在')
            elif 'b' == s2:
                break
            elif 'q' == s2:
                exit()
            else:
                print('节点不存在')
    elif 'b' == s1:
        break
    elif 'q' == s1:
        exit()
    else:
        print('节点不存在')



