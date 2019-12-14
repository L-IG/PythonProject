'''
作者:lg
日期:2019/12/3
文件描述:
缺陷：
'''

import pymysql

user = input("username:")
pwd = input("password:")

conn = pymysql.connect(host="localhost", user='root', password='123456', database="db666")
cursor = conn.cursor()

# 写法1:
# sql = "select * from userinfo where username=%s and password=%s" % (user, pwd)

# 写法2:把参数放到execute函数里,可防止SQL注入
# select * from userinfo where username='alex' or 1==1 -- and password='alex123'
sql = "select * from userinfo where username='%s' and password='%s'"

# 用列表把参数打包
cursor.execute(sql, [user, pwd])
# 当把参数传递到excute函数当做参数时,不需要再给%s 加双引号了,不然会出现如下报错,因为execute已经默认给字符串加上双引号了
# pymysql.err.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'alex'' and password=''alex123''' at line 1")

# 也可以用字典的形式
# cursor.execute(sql,{'u':user,'p':pwd})

# 拿一条
result = cursor.fetchone()

# 拿N条
# result = cursor.fetchall()

cursor.close()
conn.close()
if result:
    print('登录成功')
else:
    print('登录失败')
