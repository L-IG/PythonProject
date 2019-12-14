'''
作者:lg
日期:2019/12/12
文件描述:
缺陷：
'''
import pymysql

conn = pymysql.connect(host="localhost", user='root', password='123456', database="db666")

# 增加:
# cursor = conn.cursor()
#
# sql = 'insert into userinfo(username,password) values (%s,%s) '
#
# # 执行一条语句
# # cursor.execute(sql, ['root', 'root123456'])
# # conn.commit()
#
# # 执行N条语句
# ret = cursor.executemany(sql, [['root1', 'root1'], ['root2', 'root2'], ['root3', 'root3']])
# print(ret)  # 3 受影响的语句
# # 修改后必须提交
# conn.commit()
#
# cursor.close()
# conn.close()


# 查询:
# cursor = conn.cursor()
# sql = "select * from userinfo"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# ((1, 'alex', 'alex123'), (2, 'Jin', 'Jin123'), (3, 'Ming', 'Ming123'), (7, 'root1', 'root1'), (8, 'root2', 'root2'), (9, 'root3', 'root3'), (10, 'root1', 'root1'), (11, 'root2', 'root2'), (12, 'root3', 'root3'))


# fetchone相当于字典的read()每次读一行语句

# 如何返回字典组成的元组?
# cursor = conn.cursor(pymysql.cursors.DictCursor)
# sql = "select * from userinfo"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# [{'id': 1, 'username': 'alex', 'password': 'alex123'}, {'id': 2, 'username': 'Jin', 'password': 'Jin123'}, {'id': 3, 'username': 'Ming', 'password': 'Ming123'}, {'id': 7, 'username': 'root1', 'password': 'root1'}, {'id': 8, 'username': 'root2', 'password': 'root2'}, {'id': 9, 'username': 'root3', 'password': 'root3'}, {'id': 10, 'username': 'root1', 'password': 'root1'}, {'id': 11, 'username': 'root2', 'password': 'root2'}, {'id': 12, 'username': 'root3', 'password': 'root3'}]


# 新插入数据的自增ID
# 有这个需求:如果表的数据ID是自增的,用户就不会知道当前ID是多少了,所有需要代码来给出

cursor = conn.cursor()
sql = 'insert into userinfo(username,password) values (%s,%s) '
cursor.execute(sql, ['root', 'root123456'])
conn.commit()

# 新增加的插入语句:lastrowid表示上一次插入数据库的自增ID
print(cursor.lastrowid)
