'''
作者:lg
日期:2019/10/29
文件描述:
缺陷：
'''

# import glance
# 分析:只有glance被加载到内存里,这里要注意:glance如果是包,会执行包里的__init__文件


# import glance.api.policy
# 分析:glance.api.policy作为一个有结构的内存空间,整体被导入到当前命名空间里.注意:使用时,要从最外层的命名空间里开始!!!!!
# glance.api.policy.get()


# from glance.api import policy
# 分析:只有policy被加载到内存了,from只是寻找路径过程,glance不在内存里
# policy.get()


# from glance.api.policy import get
# get()
# 分析:把方法直接导入到当前命名空间里


import glance

glance.api
glance.main()  # from manage.py
glance.get()  # from policy.py

glance.glance_other.say_hi.say_hello()  # from say_hi
