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

current_layer = menu
last_layer = []

while True:
    for k in current_layer:
        print('当前菜单:', k)#习惯上把打印放在input前面
    s = input('choice:').strip()
    if not s: continue #用continue语句来结束后面语句的执行
    if s in current_layer:
        last_layer.append(current_layer)
        current_layer = current_layer[s]
    elif 'b' == s:
        if  [] == last_layer:
            print('到顶了')
        else:
            current_layer = last_layer.pop()
    elif 'q' == s:
        exit()
    else:
        print('节点不存在')



