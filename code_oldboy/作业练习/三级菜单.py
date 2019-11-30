'''
作者:lg
日期:2019/11/2
文件描述:
缺陷：
'''

# 递归方法

menu = {
    '北京': {
        '朝阳': {
            '国贸': {},
            'CICC': {},
            'HP': {},
            '渣打银行': {},
            'CCTV': {},
        },
        '望京': {
            '陌陌': {},
            '奔驰': {},
            '360': {},
        },
        '三里屯': {
            '优衣库': {},
            'apple': {},
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '阿泰包子': {},
            },
            '天通苑': {
                '链家': {},
                '我爱我家': {},
            },
            '回龙观': {},
        },
        '海淀': {
            '五道口': {
                '谷歌': {},
                '网易': {},
                'sohu': {},
                '快手': {},
            },
            '中关村': {
                'youku': {},
                'Iqiyi': {},
                '汽车之家': {},
                '新东方': {},
                'QQ': {},
            },

        },
    },
    '上海': {
        '浦东': {
            '陆家嘴': {
                'CICC': {},
                '高盛': {},
                '摩根': {},
            },
        },
        '闵行': {},
        '静安': {},
    },
    '山东': {
        '济南': {},
        '德州': {
            '乐陵': {
                '丁务镇': {},
                '城区': {},
            },
            '平原': {},
        },
        '青岛': {},
    },
    '青藏': {}
}


# '北京': 即是一个字典的Key值,又是一个字典的名字,字典包含着字典这样的数据结构

def ChoseeKey(dict):
    while True:
        for k in dict: print(k)
        user_k = input('请输入菜单名,b返回上一级菜单,q退出程序:')
        if user_k == 'b' or user_k == 'q': return user_k
        if dict.get(user_k) and dict[user_k]:
            ret = ChoseeKey(dict[user_k])
            if 'q' == ret:
                return ret
        elif not dict.get(user_k) or not dict[user_k]:
            continue


# ChoseeKey(menu)


# 堆栈方法:

menu_tmp = menu
l = []
while True:
    print('l', l)
    for k in menu_tmp: print(k)
    user_k = input('请输入菜单名,b返回上一级菜单,q退出程序:')
    if user_k == 'b':
        try:
            menu_tmp = l.pop()
        except IndexError:
            break
    elif menu_tmp.get(user_k) and menu_tmp[user_k]:
        l.append(menu_tmp)
        menu_tmp = menu_tmp[user_k]

    elif not menu_tmp.get(user_k) or not menu_tmp[user_k]:
        continue

# 列表是一个栈结构
# l.append()  # 入栈(从列表尾部插入)
# l.pop()  # 出栈(从列表尾部弹出)
