'''
作者:lg
日期:2019/12/13
文件描述:
缺陷：
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# max_overflow:和数据库保持的最大连接数,连接池
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/sqlalchemy_test", max_overflow=5)

Base = declarative_base()


# 创建用户类型表
class UserType(Base):
    __tablename__ = 'usertype'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32), nullable=True, index=True)


# 创建用户表
class Users(Base):
    __tablename__ = 'users'  # 表名字
    # 本质还是在init函数里面
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=True, default='alex', index=True)
    email = Column(String(16), unique=True)
    # 外键写法，注意真正的表名和类名的区别，usertype
    user_type = Column(Integer, ForeignKey('usertype.id'))

    # 如果有联合的需求，单独在这写，联合索引,联合唯一
    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_n_ex', 'name', 'email')
    )


def init_db():
    # create_all:找到所有是表名的类,在数据里里创建响应的表
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


# init_db()
# drop_db()

Session = sessionmaker(bind=engine)
session = Session()

# 类-表
# 对象-行

# 增加
# 增加一个
# obj1 = UserType(title='普通用户')
# session.add(obj1)

# 增加多个
# obj1 = UserType(title='尊贵用户')
# obj2 = UserType(title='黄金用户')
# obj3 = UserType(title='白金用户')
# obj_list = [
#     obj1, obj2, obj3
# ]
# session.add_all(obj_list)


# 查询
print(session.query(UserType))
# SQLalchemy转化的sql语句:
# SELECT usertype.id AS usertype_id, usertype.title AS usertype_title  FROM usertype

# all查询所有 相当于 *
# user_typr_list = session.query(UserType).all()
# for el in user_typr_list:
#     print(el.id,el.title)

# filter 查询满足条件的元素 相当于where
# user_typr_list = session.query(UserType).filter(UserType.id > 2)
# for el in user_typr_list:
#     print(el.id,el.title)

# 查询 部分字段
# user_typr_list = session.query(UserType.title).filter(UserType.id > 2)
# for el in user_typr_list:
#     print(el.title)

# 删除
# user_typr_list = session.query(UserType.title).filter(UserType.id > 2).delete()


# 修改
# user_typr_list = session.query(UserType.title).filter(UserType.id > 0).\
#     update({'title':'黑金用户'})

# 在字符串基础上相加
# user_typr_list = session.query(UserType.title).filter(UserType.id > 0). \
#     update({'title': UserType.title + 'VIP'}, synchronize_session=False)


# 在原数字上相加
user_typr_list = session.query(UserType.title).filter(UserType.id > 0). \
    update({'id': UserType.id + 100}, synchronize_session='evaluate')

session.commit()
session.close()

# 其他
# 　条件
# filter:表达式,filter_by:表示条件,相当于与传入一个字典
# ret = session.query(Users).filter_by(name='alex').all()
# ret = session.query(Users).filter(Users.id > 1, Users.name == 'eric').all()
# ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'eric').all()
# ret = session.query(Users).filter(Users.id.in_([1,3,4])).all()
# ret = session.query(Users).filter(~Users.id.in_([1,3,4])).all()
# ret = session.query(Users).filter(Users.id.in_(session.query(Users.id).filter_by(name='eric'))).all()

# from sqlalchemy import and_, or_
# ret = session.query(Users).filter(and_(Users.id > 3, Users.name == 'eric')).all()
# ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric')).all()
# ret = session.query(Users).filter(
#     or_(
#         Users.id < 2,
#         and_(Users.name == 'eric', Users.id > 3),
#         Users.extra != ""
#     )).all()


# 通配符
# ret = session.query(Users).filter(Users.name.like('e%')).all()
# ret = session.query(Users).filter(~Users.name.like('e%')).all()

# 限制
# ret = session.query(Users)[1:2]

# 排序
# ret = session.query(Users).order_by(Users.name.desc()).all()
# ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()

# 分组
# from sqlalchemy.sql import func
#
# ret = session.query(Users).group_by(Users.extra).all()
# ret = session.query(
#     func.max(Users.id),
#     func.sum(Users.id),
#     func.min(Users.id)).group_by(Users.name).all()
#
# ret = session.query(
#     func.max(Users.id),
#     func.sum(Users.id),
#     func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) >2).all()

# 连表
# ret = session.query(Users, Favor) # 笛卡尔积,两张表不加条件
# ret = session.query(Users, Favor).filter(Users.id == Favor.nid).all()
# ret = session.query(Person).join(Favor).all()# innner join
# ret = session.query(Person).join(Favor, isouter=True).all()# left join

# 组合
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union(q2).all()
#
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union_all(q2).all()

# 子查询!!!!!
# 1.
# select * from b where id in (select id from tb2)

# 2.
# select * from (select * from tb) as B
# subquery():要加上,指明它是一个子查询语句!!!
# q1 = session.query(UserType).filter(UserType.id > 0).subquery()
# result = session.query(q1).all()
# print(result)

# 3.
# select
#   id ,
#   (select * from users where users.user_type_id=usertype.id)
# from usertype;


# as_scalar:表名这依然是一个SQL语句,而不是已经转化为一个表了!!!

# session.query(UserType,session.query(Users).filter(Users.id == 1).subquery())
# session.query(UserType,Users)
# result = session.query(UserType.id,session.query(Users).as_scalar())
# print(result)
# result = session.query(UserType.id,session.query(Users).filter(Users.user_type_id==UserType.id).as_scalar())
# print(result)


# 表示当循环到某个用户类型后,拿着用户类型的ID去另一个表里遍历一遍条件相等的数据行!!!
# print(row.id,row.title,session.query(Users).filter(Users.user_type_id == row.id).all())
