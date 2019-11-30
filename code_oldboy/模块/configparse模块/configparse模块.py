'''
作者:lg
日期:2019/11/29
文件描述:
缺陷：
'''

import configparser

# 生成文件
# config = configparser.ConfigParser()
#
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11': 'yes'
#                      }
#
# config['bitbucket.org'] = {'User': 'hg'}
#
# config['topsecret.server.com'] = {'Host Port': '50022', 'ForwardX11': 'no'}
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)


# 查找文件
# config = configparser.ConfigParser()
# print(config.sections())
#
# config.read('example.ini')
# print(config.sections())
# # ['bitbucket.org', 'topsecret.server.com']
#
# print('bytebong.com' in config)
# print('bitbucket.org' in config)
#
# print(config['bitbucket.org']['user'])
# print(config['DEFAULT']['Compression'])
# print(config['topsecret.server.com']['ForwardX11'])
#
# print(config['bitbucket.org'])
# # <Section: bitbucket.org> 返回一个对象
#
# for key in config['bitbucket.org']:
#     print(key)
#
# print(config.options('bitbucket.org'))
# # ['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']
# # 同for循环,找到'bitbucket.org'下所有键
#
# print(config.items('bitbucket.org'))
# # [('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'hg')]
#
# print(config.get('bitbucket.org','compression'))

# 增删改操作
config = configparser.ConfigParser()
config.read('example.ini')
config.add_section('yuan')
config.remove_section('bitbucket.org')
config.remove_option('topsecret.server.com', "forwardx11")

config.set('topsecret.server.com', 'k1', '1111111')
config.set('yuan', 'k2', '22222')
# 此时所有内容都在内存里,必须写到文件才会保存下来
config.write(open('new2.ini', "w"))
