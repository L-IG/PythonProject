'''
作者:lg
日期:2019/11/4
文件描述:
缺陷：
策略:1,每当去文件里读取对象时,都先把公共列表清空,保持列表里的元素不重复,并且都是最新,实时的
    2,当查看,修改文件里的对象时都需要去文件里重新读取,再加载到列表里,新添加则不需要
'''

# 管理员
# 管理员不应该有班级属性,因为管理员可以管理所有班级

import pickle
from conf import config
from core import Teacher
from core import Student
from core import Main

BATH_PATH = config.BASE_PATH  # 配置文件db所在目录
TEACHER_PATH = config.TEACHER_OBJ_PATH  # 老师对象存储的路径
COURSES_PATH = config.COURSES_OBJ_PATH  # 课程对象存储的路径
CLASSES_PATH = config.CLASSES_OBJ_PATH  # 班级对象存储的路径

COURSES_LIST = []
STUDENTS_LIST = []
# STUDENTS_LIST_TMP = []  # 因为当学生对象未被分配班级时,不会存入班级的文件里,所以需要提醒用户是否放弃未被编辑的
TEACHER_LIST = []
CLASSES_LIST = []


def load_obj_db(file, list_obj):
    '''
    读出文件里对象,存到列表'list_obj'里
    :param file:
    :return:
    '''
    list_obj.clear()  # 先清空公共列表的元素,防止多次加载会造成列表元素对象重复出现,
    # 注意:清空要用clear,不能用赋值语句,不然变量就不是全局列表变量的值了,而是新值
    with open(file, 'rb') as f:
        while True:
            try:
                c_obj = pickle.load(f)
                list_obj.append(c_obj)
            except EOFError:
                break
    print('成功读取文件对象到内存!')


def save_obj_db(file, list_obj):
    '''
    :param file:
    :param list_obj:
    :return:
    '''
    with open(file, 'wb') as f:
        for obj in list_obj:
            pickle.dump(obj, f)
    print('成功写入文件!')


class Manager(object):
    def __init__(self, name):
        self.name = name

    def create_teacher(self):
        '''
        输入讲师的姓名
        输入讲师的密码
        将讲师的登录信息写入userinfo文件
        输入讲师所在的学校
        根据三个信息:姓名,身份,学校
        实例化一个讲师对象,用pickle存到对应文件里
        :return:
        '''
        name = input('请输入老师账号:')
        passwd = input('请输入密码:')
        info = f'{name},{passwd},teacher'
        Main.save_info_db(info)
        school = input('请输入学校:')
        t_obj = Teacher.Teacher(name, school)
        with open(TEACHER_PATH, 'ab') as f:
            pickle.dump(t_obj, f)
        print('成功创建讲师账号!')

    def create_courses(self):
        '''
        输入 学科名称,价格,周期
        创建一个课程对象,dump进对应文件
        :return:
        '''
        name = input('请输入科目:')
        price = input('请输入价格:')
        period = input('请输入周期:')
        c = Teacher.Courses(name, period, price)
        with open(COURSES_PATH, 'ab') as f:
            pickle.dump(c, f)
        print('成功创建课程!')

    def show_courses(self):
        '''
        :return:
        '''
        load_obj_db(COURSES_PATH, COURSES_LIST)
        for el in COURSES_LIST:
            print(el.name, el.period, el.price)

    def create_classes(self):
        '''
        输入班级名称
        输入班级所在的学校
        绑定一个学科对象:要先展示所有学科对象,用户选择一个学科,然后与班级所绑定
        创建一个属于这个班级的文件用于存储学生信息,将文件路径保存在班级属性里
        创建一个班级对象,包括班级名称,学校,学科,学生对应的文件路径,dump进对应文件里
        :return:
        '''
        name = input('请输入班级名:')
        school = input('请输入班级所在学校:')
        Manager.show_courses(self)
        choose = int(input('请输入序号:').strip())
        kind = COURSES_LIST[choose]
        students_file_name = f'{name}_file'
        with open(f'{BATH_PATH}/{students_file_name}', 'wb') as F:
            pass
        cl = Teacher.Classes(name, school, kind, students_file_name)
        with open(CLASSES_PATH, 'ab') as f:
            pickle.dump(cl, f)
        print('成功创建班级!')

    def show_classes(self):
        '''
        展示班级对象里的班级名称,学生人数等
        :return:
        '''
        load_obj_db(CLASSES_PATH, CLASSES_LIST)
        for el in CLASSES_LIST:
            print(el.name, el.school, el.kind.name, el.students)

    def show_teacher(self):
        '''
        展示老师对象
        :return:
        '''
        load_obj_db(TEACHER_PATH, TEACHER_LIST)
        for el in TEACHER_LIST:
            print(el.name)

    def create_student(self):
        '''
        输入学生的姓名
        输入学生的密码
        将学生的登录信息写入userinfo文件
        创建学生对象(姓名和讲师空列表),注意:学生对象不存在单独的对应文件里,它放在对应班级的文件里
        :return:
        '''
        name = input('请输入学生账号:')
        passwd = input('请输入密码:')
        info = f'{name},{passwd},student'
        Main.save_info_db(info)
        st = Student.Student(name)
        STUDENTS_LIST.append(st)

    def student_bound_classes(self):
        '''
        管理员为学生绑定班级:
        show所有学生和所有班级
        用户选择绑定
        给学生创建班级属性
        将学生的对象 根据班级属性里学生对象的路径 用此路径把学生对象dump进去
        :return:
        '''
        print('以下学生还未分配班级:')
        for index, el in enumerate(STUDENTS_LIST):
            print(f'{index}:{el.name}')
        print('可选择绑定的班级有:')
        self.show_classes()
        try:
            st_index = int(input('请选择要分配的学生编号:').strip())
        except ValueError:
            print(ValueError)
            return None
        cl = input('请选择要绑定的班级名:').strip()
        students_file_name = f'{cl}_file'
        STUDENTS_LIST[st_index].classes = cl  # 给学生创建班级属性
        with open(f'{BATH_PATH}/{students_file_name}', 'ab') as f:
            pickle.dump(STUDENTS_LIST[st_index], f)
        print('成功存储学生对象!')
        print('成功为班级绑定学生!')

    def teacher_bound_classes(self):
        '''
        管理员为老师绑定班级:
        show所有老师和所有班级,用户选择绑定
        给讲师对象的班级属性列表里加一个新值,为班级对象
        给班级对象的老师属性列表里加一个新值,为老师对象
        这样互相绑定了
        :return:
        '''
        # 先把文件里对象更新到内存中
        load_obj_db(TEACHER_PATH, TEACHER_LIST)
        load_obj_db(CLASSES_PATH, CLASSES_LIST)

        for index1, el1 in enumerate(TEACHER_LIST):
            print(f'{index1}:{el1.name}')
        for index2, el2 in enumerate(CLASSES_LIST):
            print(f'{index2}:{el2.name}')

        t_choose = int(input('请选择教师序号绑定:').strip())
        cl_choose = int(input('请选择班级序号绑定:').strip())
        # 对象全部加载到内存后,在内存中修改,修改完之后存到文件里

        teacher_obj = TEACHER_LIST[t_choose]
        classes_obj = CLASSES_LIST[cl_choose]

        TEACHER_LIST[t_choose].classes.append(classes_obj)
        CLASSES_LIST[cl_choose].teachers.append(teacher_obj)

        # 修改某个对象,需要重新写入全部对象到文件
        save_obj_db(TEACHER_PATH, TEACHER_LIST)
        save_obj_db(CLASSES_PATH, CLASSES_LIST)
        # for el in TEACHER_LIST:
        #     save_obj_db(TEACHER_PATH, el)
        # for el in CLASSES_LIST:
        #     save_obj_db(CLASSES_PATH, el)

        print('互相绑定成功!')

    def students_cmp(self):
        '''
        返回没有被分配班级的学生
        :return:
        '''
        students_not_bound = []
        for el in STUDENTS_LIST:
            if not hasattr(el, 'classes'):
                students_not_bound.append(el)
        return students_not_bound

    menu = {
        '创建讲师账号': 'create_teacher',
        '创建课程': 'create_courses',
        '展示课程': 'show_courses',
        '创建班级': 'create_classes',
        '展示班级': 'show_classes',
        '创建学生账号': 'create_student',
        '给学生分配班级': 'student_bound_classes',
        '展示讲师': 'show_teacher',
        '给讲师分配班级': 'teacher_bound_classes',
        '给讲师分配课程': '',
    }


def manager_main(name):
    while True:
        for k in Manager.menu: print(k)
        m = Manager(name)
        user_choose = input('请选择管理员的功能:').strip()
        try:
            func = Manager.menu[user_choose]
        except KeyError:
            print('功能不存在')
            continue
        Manager.__dict__[func](m)
        choose = input('退出Q or q:')
        if choose == 'q' or choose == 'Q':
            students_not_bound = m.students_cmp()
            if len(students_not_bound):
                print('以下学生还未绑定班级')
                for el in students_not_bound:
                    print(el.name)
            else:
                return
        else:
            continue


if __name__ == '__main__':
    manager_main('alex')
