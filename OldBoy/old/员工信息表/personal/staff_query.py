from tabulate import tabulate
import os

STAFF_DB = "staff.db"

def load_db():
    db = {         #存放员工的数据结构
        'id':[],
        'name':[],
        'age':[],
        'phone':[],
        'dept':[],
        'enrolled_date':[]
    }

    with open(STAFF_DB,'r',encoding='utf-8') as f:
        for line in f:
            db['id'].append(line.strip().split(',')[0])
            db['name'].append(line.strip().split(',')[1])
            db['age'].append(line.strip().split(',')[2])
            db['phone'].append(line.strip().split(',')[3])
            db['dept'].append(line.strip().split(',')[4])
            db['enrolled_date'].append(line.strip().split(',')[5])

    return db

def save_db():
    print(STAFF_DATA)
    with open('%s.new'%(STAFF_DB), 'w', encoding='utf-8') as f:
        STAFF_TMP = []
        for index, id in enumerate(STAFF_DATA['id']):
            STAFF_TMP = []
            for k in STAFF_DATA:
                STAFF_TMP.append(STAFF_DATA[k][index])
            print(','.join(STAFF_TMP))
            f.write(','.join(STAFF_TMP)+'\r')
    os.replace('%s.new'%(STAFF_DB),STAFF_DB)


def syntax_find(field, matched_data):
    print(field)           #eg. find id,phone from staff_table
    if '*' not in field:
        head_tmp = field.split('from')[0].split('find')[1].strip().split(',')
    else:
        head_tmp = ['id','name','age','phone','dept','enrolled_date']
    list = []
    for index,value in enumerate(matched_data[head_tmp[0].strip()]):
        list_tmp = []
        for key_clause in head_tmp:
            list_tmp.append(matched_data[key_clause][index])
        list.append(list_tmp)
    print(tabulate(list,headers=head_tmp))

def syntax_add(staff_info):
    staff_list = [i.strip() for i in staff_info.split(',')]
    print(STAFF_DATA)

    for i in STAFF_DATA['phone']:
        if i == staff_list[2]:
            print('ERR:the same telephone!')
            return
    old_id = int(STAFF_DATA['id'][-1])
    STAFF_DATA['id'].append(str(old_id + 1))
    STAFF_DATA['name'].append(staff_list[0])
    STAFF_DATA['age'].append(staff_list[1])
    STAFF_DATA['phone'].append(staff_list[2])
    STAFF_DATA['dept'].append(staff_list[3])
    STAFF_DATA['enrolled_date'].append(staff_list[4])
    save_db()


def syntax_update(query_clause, matched_data):
    filed = query_clause.split('set')[1].strip()
    filed_key = filed.split('=')[0].strip()  #eg age
    filed_value = filed.split('=')[1].strip() #eg 30
    print('filed_key:',filed_key)
    print('filed_value:',filed_value)

    # 修改列表里的值的方法 ：通过取下标方式，不可以通过修改迭代变量
    # for index,list_value in enumerate(matched_data[filed_key]):
    #     matched_data[filed_key][index] = filed_value
    # print(matched_data)

    for index1,id in enumerate(matched_data['id']):
        STAFF_DATA[filed_key][index1] = filed_value
    save_db()

def syntax_detele(query_clause, matched_data):
    id_list = []
    for i in matched_data['id']:
        id_list.append(STAFF_DATA['id'].index(i))
    id_list = id_list[::-1]            #此处应该把列表倒置，因为列表每删掉前一个元素，后一个元素索引会变化
    print(id_list)

    for k in STAFF_DATA:
        for n in id_list:
            STAFF_DATA[k].pop(n)

    new_len = len(STAFF_DATA['id'])
    STAFF_DATA['id'] = []
    STAFF_DATA['id'] = [str(i) for i in range(new_len)]           #range()更像是c语言的for循环，而不是迭代
    save_db()


def op_gt(q_name,q_condtion):
    match_data = {  # 存放员工的数据结构
        'id': [],
        'name': [],
        'age': [],
        'phone': [],
        'dept': [],
        'enrolled_date': []
    }

    for id,clause in enumerate(STAFF_DATA[q_name]): #eg. 0 22, 1 23, 2 40
        #print(id,clause)
        if clause > q_condtion:
            match_data['id'].append(STAFF_DATA['id'][id])
            match_data['name'].append(STAFF_DATA['name'][id])
            match_data['age'].append(STAFF_DATA['age'][id])
            match_data['phone'].append(STAFF_DATA['phone'][id])
            match_data['dept'].append(STAFF_DATA['dept'][id])
            match_data['enrolled_date'].append(STAFF_DATA['enrolled_date'][id])
    return  match_data

def op_lt(q_name,q_condtion):
    pass
def op_eq(q_name,q_condtion):
    match_data = {  # 存放员工的数据结构
        'id': [],
        'name': [],
        'age': [],
        'phone': [],
        'dept': [],
        'enrolled_date': []
    }

    for id, clause in enumerate(STAFF_DATA[q_name]):  # eg. 0 22, 1 23, 2 40
        # print(id,clause)
        if clause == q_condtion:
            match_data['id'].append(STAFF_DATA['id'][id])
            match_data['name'].append(STAFF_DATA['name'][id])
            match_data['age'].append(STAFF_DATA['age'][id])
            match_data['phone'].append(STAFF_DATA['phone'][id])
            match_data['dept'].append(STAFF_DATA['dept'][id])
            match_data['enrolled_date'].append(STAFF_DATA['enrolled_date'][id])
    return match_data
def op_like(q_name,q_condtion):
    pass

def syntax_where(condition):
    operators = { #字典元素后面可以是任意元素，包括函数名 eg. oprators['>']
        '>':op_gt,
        '<':op_lt,
        '=':op_eq,
        'like':op_like
    }

    for key,value in operators.items():
        if key in condition:
            q_name = condition.split(key)[0].strip()
            q_condtion = condition.split(key)[1].strip()
            filter_data = value(q_name,q_condtion)
            return filter_data

def syntax_parser(cmd):
    syntax_list = {
        'find':syntax_find,
        'update':syntax_update,
        'add':syntax_add,
        'delete':syntax_detele
    }

    flag_clause = cmd.split()[0].strip()   #eg. find update delete

    if 'add' not in cmd:
        if 'where' in cmd:
            filed = cmd.split('where')[0].strip()     #eg update staff_table set age = 30   find id,phone from staff_table
            conditon = cmd.split('where')[1].strip()  #eg id > 22, age = 25

            filter_data = syntax_where(conditon)
        else:
            filed = cmd
            filter_data = STAFF_DATA

        syntax_list[flag_clause](filed,filter_data)


    if 'add' in cmd:
        staff_info = cmd.split('staff_table')[1].strip()
        syntax_list[flag_clause](staff_info)


def main():
    while True:
        cmd = input('please input SQL:').strip()
        if not cmd: continue
        syntax_parser(cmd)

STAFF_DATA = load_db()
main()