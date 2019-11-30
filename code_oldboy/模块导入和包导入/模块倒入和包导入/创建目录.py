'''
作者:lg
日期:2019/10/29
文件描述:
缺陷：
'''

import os

os.makedirs('glance/api')
os.makedirs('glance/cmd')
os.makedirs('glance/db')

l = []
l.append(open('glance/__init__.py', 'w'))
l.append(open('glance/api/__init__.py', 'w'))
l.append(open('glance/api/policy.py', 'w'))
l.append(open('glance/api/versions.py', 'w'))
l.append(open('glance/cmd/__init__.py', 'w'))
l.append(open('glance/cmd/manage.py', 'w'))
l.append(open('glance/db/models.py', 'w'))
l.append(open('glance/db/__init__.py', 'w'))
map(lambda f: f.close(), l)

