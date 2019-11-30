'''
作者:lg
日期:2019/9/22
文件描述:
缺陷：1,只完成查询功能
2,为了完成功能,代码写的很冗余
'''

# 测试输入
# select * from usertabel where age = 22
# select id,name from usertabel where age > 22

# insert into usertabel (name,age,telephone,job)values(xiaoming,28,16786573241,teacher)

from tabulate import tabulate

filed_list = ['']
condition_list = []
FILED_NAME = {
    'id': 0,
    'name': 1,
    'age': 2,
    'telephone': 3,
    'job': 4,
}
STAFF_DB = '员工信息.txt'


def load_db():
    '''
    生成器方式返回员工信息
    :return:
    '''
    with open(STAFF_DB, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            staff_list = line.split(',')
            yield staff_list


def con_like(filed_, condition_):
    line_tmp = []
    with open('员工信息.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            filed_l = line.split(',')
            if filed_l[FILED_NAME[filed_]] in condition_:
                line_tmp.append(line)
    return line_tmp


def con_eql(filed_, condition_):
    line_tmp = []
    g = load_db()
    for line in g:
        if line[FILED_NAME[filed_]] == condition_:
            line_tmp.append(line)
    return line_tmp



def con_dayu(filed_, condition_):
    line_tmp = []
    with open('员工信息.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            filed_l = line.split(',')
            if filed_l[FILED_NAME[filed_]] > condition_:
                line_tmp.append(line)
    return line_tmp


def con_xiaoyu(filed_, condition_):
    line_tmp = []
    with open('员工信息.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            filed_l = line.split(',')
            if filed_l[FILED_NAME[filed_]] < condition_:
                line_tmp.append(line)
    return line_tmp


CONDITION_DIC = {
    'like': con_like,
    '=': con_eql,
    '>': con_dayu,
    '<': con_xiaoyu,
}


def input_check():
    user_input = input('请输入语句:').strip()
    return user_input


def where_parse(field):
    print('where_parse', field)
    filed_, condition_, symbol = ('', '', '')
    if 'like' in field:
        symbol = 'like'
        filed_, condition_ = field.split('like')
    elif '>' in field:
        symbol = '>'
        filed_, condition_ = field.split('>')
    elif '<' in field:
        symbol = '<'
        filed_, condition_ = field.split('<')
    elif '=' in field:
        symbol = '='
        filed_, condition_ = field.split('=')
    else:
        print('\033[31m符号错误\033[0m')
    filed_ = filed_.strip()
    condition_ = condition_.strip()
    print('filed_,condition_', filed_, condition_)
    ret = CONDITION_DIC[symbol](filed_, condition_)
    print('\033[31m------\033[0m', ret)
    return ret


QUERY_L = ['id', 'name', 'age', 'telephone', 'job']


def filed_parse(filed):
    filed_c = []
    filed_l = filed.split(',')
    for index, el in enumerate(filed_l):
        filed_l[index] = el.strip()
    for el in filed_l:
        filed_index = filed_l.index(el)
        filed_c.append(filed_index)
    return filed_c


# def str_to_list(ret_c):
#     l_tmp = []
#     for i in ret_c:
#         i_list = i.split(',')
#         l_tmp.append(i_list)
#     return l_tmp


def str_parse(user_input):
    if 'insert' in user_input:
        # 添加新元素
        add_new(user_input)
    elif 'update' in user_input:
        if 'where' in user_input:
            print('\033[31m有where\033[0m')
            filed, condition = user_input.split('where')
            condition = condition.strip()
            ret_c = where_parse(condition)
            # ret_c = str_to_list(ret_c)
            print('\033[31m返回where解析函数\033[0m', ret)

            up_field = user_input.split('set')[1]
            up_field = user_input.split('where')[0].strip()
        else:
            ret_c = []
            up_field = user_input.split('set')[1].strip()
        print(f'\033[31m update_field:{{ {up_field} }}\033[0m')
        update_info(up_field, ret_c)


    else:
        if 'where' in user_input:
            print('\033[31m有where\033[0m')
            filed, condition = user_input.split('where')
            condition = condition.strip()
            ret_c = where_parse(condition)
            # ret_c = str_to_list(ret_c)
            print('\033[31m返回where解析函数\033[0m', ret)
        else:
            ret_c = []

        if '*' in user_input:
            filed_c = ['*']
        else:
            filed = user_input.split('select')[1].strip()
            filed = filed.split('from')[0].strip()
            print(filed)
            filed_c = filed_parse(filed)
        print('\033[31m最终解析结果:\033[0m', ret_c, filed_c)
        input_parse = (ret_c, filed_c)
        # 查询功能
        query(input_parse)


# update usertabel set name = xiaohuang , age = 18 where age = 22
# update usertabel set name = xiaohuang , age = 18
# 修改元素功能
def update_info(up_field, ret_c):
    new_dic = {}
    field_l = up_field.split(',')
    for el in field_l:
        file_k, field_v = el.split('=')
        file_k = file_k.strip()
        file_v = field_v.strip()
        new_dic.setdefault(file_k, field_v)
    print(f'\033[31m new_dic = {new_dic}\033[0m')
    if ret_c == []:
        with open('员工信息.txt', 'r', encoding='utf-8') as f, open('员工信息.txt.bak', 'w', encoding='utf-8') as f1:
            for line in f:
                query_l_tmp = line.split(',')
                for k in new_dic:
                    query_l_tmp[QUERY_L.index(k)] = new_dic[k].strip()
                line = ','.join(query_l_tmp)
                f1.write(line)
            f1.write('\n')
    else:
        pass


def query(input_parse):
    '''
    根据where条件和字段打印查询结果
    :param input_parse[1]:关键字段索引,input_parse[0]:一行数据
    :return:
    '''
    print('input_parse[1]:关键字段索引,input_parse[0]:一行数据', input_parse[0], input_parse[1])
    if '*' in input_parse[1]:
        if input_parse[0]:
            print('\033[31m打印结果为\033[0m', tabulate(input_parse[0]))
        else:
            l_tmp = []
            g = load_db()
            for line in g:
                l_tmp.append(line)
            print('\033[31m打印结果为\033[0m', tabulate(l_tmp))

    else:
        if input_parse[0]:
            p_list = input_parse[0]
        else:
            l_tmp = []
            g = load_db()
            for line in g:
                l_tmp.append(line)
            p_list = l_tmp
        l_tmp = []
        for i in p_list:
            l_tmp_1 = []
            for j in input_parse[1]:
                l_tmp_1.append(i[j])
            l_tmp.append(l_tmp_1)
        print('\033[31m打印结果为\033[0m', tabulate(l_tmp))


# insert into usertabel (name,age,telephone,job) values ( xiaoming , 28 , 16786573241 , teacher )
def add_new(user_input):
    _, field_value = user_input.split('values')
    field_value = field_value.split('(')[1]
    field_value = field_value.split(')')[0].strip()
    value_l = field_value.split(',')
    for index, el in enumerate(value_l):
        value_l[index] = el.strip()
    print('\033[31m添加的新行=\033[0m', value_l)
    value_str = ','.join(value_l)
    count = 0
    with open('员工信息.txt', encoding='utf-8') as f:
        for line in f:
            if line:
                count += 1
    with open('员工信息.txt', 'a', encoding='utf-8') as f1:
        f1.write(f'{count + 1},{value_str}')
        f1.write('\n')


ret = input_check()
input_parse = str_parse(ret)

# 添加新元素功能
