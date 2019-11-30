def create_resource(conf):
    print('from version.py: ',conf)



#绝对导入
# from glance.cmd import manage
# manage.main()

#相对导入
from ..cmd import manage
manage.main()