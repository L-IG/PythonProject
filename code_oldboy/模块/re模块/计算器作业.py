'''
作者:lg
日期:2019/10/13
文件描述:用正则表达式模拟计算器
缺陷：
'''

# 去掉所有的空格
# 加减乘除  括号
# 先算括号里的乘除，再算括号里的加减
# 从括号里取值 == 正则表达式
# ss = '9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14'
# 从一个没有括号的表达式中取 */法  == 正则表达式

# 总体步骤:
# 每次脱去一个括号,计算括号里面的内容,先算乘除再算加减,把结果替换到原来的字符串中,之后,执行一次操作:把'+-'替换成'-','--'替换成'+'
import re


def replace_symbol(str_num):
    str_num = str_num.replace('+-', '-')
    str_num = str_num.replace('--', '+')
    return str_num


def mov_space(str_num):
    '''
    去掉所有的空格
    :param str_num:
    :return:
    '''
    str_num = str_num.replace(' ', '')
    return str_num


def mov_brackets(str_num):
    '''
    脱去括号
    :param str_num:
    :return:
    '''
    while True:
        print('抽取括号操作'.center(50, '-'))
        search_ret = re.search('\([^(]*?\)', str_num)
        if search_ret:
            search_ret = search_ret.group()
            str_ret = search_ret[1:-1]
            print('括号里的字符串(带括号) = ', search_ret)
            print('括号里的字符串(不带括号) = ', str_ret)
            print('原始数字字符串 = ', str_num)
        else:
            # 当没有括号存在时
            str_ret = str_num

        # 计算括号里面的内容(顺序:除法->乘法->减法->加法)
        print('除法'.center(50, '*'))
        print('str_ret = ', str_ret)
        # test
        # str_ret = '9-2*5/3+7/3*99/4*2998+10*568/14'
        while True:
            if '/' not in str_ret:
                break
            div_ret = re.search('(\d+\.\d+|\d+)/(-\d+\.\d+|\d+\.\d+|-\d+|\d+)', str_ret)
            print(div_ret)
            div_ret = div_ret.group()
            a, b = div_ret.split('/')
            ret_replace = float(a) / float(b)
            ret_replace = str(ret_replace)
            print('ret_replace = ', ret_replace)
            str_ret = str_ret.replace(div_ret, ret_replace, 1)
            str_ret = replace_symbol(str_ret)
            print('\033[31mstr_ret =\033[0m', str_ret)

        print('乘法'.center(50, '*'))
        print('str_ret = ', str_ret)
        # test
        # str_ret = '1-2*-1388335.8476190479'
        while True:
            print('乘法进来了')
            if '*' not in str_ret:
                break
            mul_ret = re.search('(\d+\.\d+|\d+)\*(-\d+\.\d+|\d+\.\d+|-\d+|\d+)', str_ret)
            print(mul_ret)
            mul_ret = mul_ret.group()
            a, b = mul_ret.split('*')
            ret_replace = float(a) * float(b)
            ret_replace = str(ret_replace)
            print('ret_replace = ', ret_replace)
            str_ret = str_ret.replace(mul_ret, ret_replace, 1)
            str_ret = replace_symbol(str_ret)
            print('\033[31mstr_ret =\033[0m', str_ret)

        print('减法'.center(50, '*'))
        print('str_ret = ', str_ret)
        # test
        # str_ret = '-6.5-3.5+100'  # 需要做特殊处理
        while True:
            if str_ret.count('-') == 1 and str_ret.startswith('-'):  # 要注意的点
                print('走了')
                break
            print('----')
            if '-' not in str_ret:
                break
            print('----')
            # sub_ret = re.search('(\d+\.\d+|\d+)-(\d+\.\d+|\d+)', str_ret)
            sub_ret = re.search('(-\d+\.\d+|-\d+|\d+\.\d+|\d+)-(\d+\.\d+|\d+)', str_ret)
            print(sub_ret)
            sub_ret = sub_ret.group()
            a, b = sub_ret.rsplit('-', 1)  # 要注意的点

            ret_replace = float(a) - float(b)
            ret_replace = str(ret_replace)
            print('ret_replace = ', ret_replace)
            str_ret = str_ret.replace(sub_ret, ret_replace, 1)
            str_ret = replace_symbol(str_ret)
            print('\033[31mstr_ret =\033[0m', str_ret)

        print('加法'.center(50, '*'))
        print('str_ret = ', str_ret)
        # test
        # str_ret = '-10.5+20.5'
        while True:
            if '+' not in str_ret:
                break
            add_ret = re.search('(-\d+\.\d+|-\d+|\d+\.\d+|\d+)\+(\d+\.\d+|\d+)', str_ret)
            print(add_ret)
            add_ret = add_ret.group()
            a, b = add_ret.split('+')
            ret_replace = float(a) + float(b)
            ret_replace = str(ret_replace)
            print('ret_replace = ', ret_replace)
            str_ret = str_ret.replace(add_ret, ret_replace, 1)
            str_ret = replace_symbol(str_ret)
            print('\033[31mstr_ret =\033[0m', str_ret)

        print('替换括号操作'.center(50, '-'))
        print('str_num = ', str_num)
        print('search_ret = ', search_ret)
        # 计算完整个括号里全部结果再替换原字符串
        if search_ret:
            str_num = str_num.replace(search_ret, str_ret, 1)
        else:
            # 没有括号存在了,并且只剩一个数字
            return str_ret
        print(str_num)

        # 替换字符串之后,最后一次执行加减乘除返回结果
        str_num = replace_symbol(str_num)
        print('str_num = ', str_num)


a = '1 - 2 * ( ( 6 0 -3 0  +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
a = mov_space(a)
# 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
ret = mov_brackets(a)
print(ret)

# 结果:2776672.6952380957
