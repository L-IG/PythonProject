'''
作者:lg
日期:2019/12/14
文件描述:
缺陷：
'''

# DB first: 手动创建数据库以及表          -> ORM框架 -> 自动生成类
# code first： 手动创建类、和数据库        -> ORM框架 -> 以及表
# SQLachemy是code first

# 功能
# # 			- 创建数据库表
# # 			- 连接数据库（非SQLAlchemy,pymyql,mysqldb,....）
# # 			- 类转换SQL语句(代码转换为数据库表以及一行行数据)
# # 			- 操作数据行
# # 				增
# # 				删
# # 				改
# # 				查


# SQLAchemy并不会去练数据库,是调用其他模块如果pymsql去连接的,使用SQLAchemy之前,需要安装这些模块
# 这些模块的功能是 DBAPI

# Dialect表示集中数据库MySQL,Oracal,根据配置的不同选择不同的数据库去连接
