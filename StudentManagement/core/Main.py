'''
作者:lg
日期:2019/11/4
文件描述:
缺陷：
'''

from core import Manager
from core import Teacher
from core import Student
from conf import config

USER_INFO_LIST = []
USER_INFO_PATH = config.USER_INFO_PATH
IDENTIFY_FUNC = {
    'manager': Manager.manager_main
}


# IDENTIFY = {
#     'teacher': 'teacher'
# }


def load_info_db():
    '''
    加载unserinfo信息(账号,密码,身份)到内存
    :return:
    '''
    l_tmp = []
    with open(USER_INFO_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            l_tmp = line.split(',')
            USER_INFO_LIST.append(l_tmp)


def save_info_db(info):
    '''
    把内存中的登录信息保存到配置文件
    :param info: 账号,密码,身份
    :return:
    '''
    with open(USER_INFO_PATH, 'a', encoding='utf-8') as f:
        f.write(info)
        f.write('\n')


def login():
    '''
    登录功能,根据用户输入判断用户身份类型,进入到不同的视图
    :return:
    '''
    load_info_db()
    print('请输入用户名和密码:')
    username = input('用户名:')
    userpasswd = input('密码:')
    for el in USER_INFO_LIST:
        if username == el[0] and userpasswd == el[1]:
            print('登录成功!')
            print('您的身份是%s' % (el[2]))
            IDENTIFY_FUNC[el[2]](username)


def main():
    login()
