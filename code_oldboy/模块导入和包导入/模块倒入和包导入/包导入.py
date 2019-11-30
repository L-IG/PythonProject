'''
作者:lg
日期:2019/10/29
文件描述:
缺陷：
'''

# 包是多个py文件的组合,放在同一个文件夹里

# 规定:凡是在导入时带点的,点的左边都必须是一个包,不然非法
# 规定:from后导入的模块,必须是一个不能带点的名子,如from a import b.c

# from是一个路径寻找过程,向里层寻找,并不需要关注变量名是否已经被导入到内存了!!!!!
# from glance.api import policy->分析:
# 从glance开始,通过点点的方式一层一层的往里面的目录去寻找,寻找到了policy后,加载到当前命名空间里,所以说from的过程是寻找的过程!!!!!

# import导入包和导入文件的对比:!!!!!
# import导入文件:
# 1,为这个文件创建一个模块空间
# 2,执行这个文件(所有执行语句把变量名导入到当前命名空间的都是导入到包空间了!!!!!)
# 3,把变量名放在模块空间里

# import导入包:
# 1,为这个包创建一个包空间
# 2,执行这个包目录里的__init__文件
# 3,把变量名放在包空间里

# 包的命名空间表现为一个层次结构,关系向里层递进
# glance.api.policy.get()->这句话分析:
# 变量名api加载到glance命名空间了,policy加载到api命名空间了,get加载到policy命名空间了!!!!!

# 一个结论:
# 如果在包里的__init__文件夹里导入了其他模块名,用from...import...或者import,
# 导进来的变量名(注意:不管这个变量名是来自和包的同级目录,或者包里面)此刻都被加载到这个包空间了,
# 后续直接使用'包名.被导入的变量名'使用

# 举例
# __init__文件的内容为:
# (一定要从根目录来导入,就是主执行文件的所在目录!!!!!)
# from glance import api
# from glance.cmd.manage import main
# from glance.api.policy import get
#
# import glance_other.say_hi


# 上一层目录下的一个文件:
# import glance
#
# glance.api
# glance.main()  # from manage.py
# glance.get()  # from policy.py
#
# glance.glance_other.say_hi.say_hello()  # from say_hi
