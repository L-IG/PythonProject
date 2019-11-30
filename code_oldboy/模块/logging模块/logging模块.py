'''
作者:lg
日期:2019/11/30
文件描述:
缺陷：
'''

# login  登录
# log 日志
# logging

# 什么叫日志？
# 日志 用来记录用户行为 或者 代码的执行过程
# print

# logging
# 我能够“一键”控制
# 排错的时候需要打印很多细节来帮助我排错
# 严重的错误记录下来
# 有一些用户行为 有没有错都要记录下来

import logging

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

logging.debug('debug message')  # 低级别的 # 排错信息
logging.info('info message')  # 正常信息
logging.warning('warning message')  # 警告信息
logging.error('error message')  # 错误信息
logging.critical('critical message')  # 高级别的 # 严重错误信息

# format格式问题
print('%(key)s' % {'key': 'Value'})
# Value

# basicconfig 简单 能做的事情相对少
# 中文的乱码问题
# 不能同时往文件和屏幕上输出


# 配置log对象 稍微有点复杂 能做的事情相对多
# 好处:高可定制化,解耦
logger = logging.getLogger()
fh = logging.FileHandler('log.log', encoding='utf-8')
sh = logging.StreamHandler()
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
# 文件操作符 和 格式关联
fh.setFormatter(formatter1)
sh.setFormatter(formatter2)
# logger 对象 和 文件操作符 关联
logger.addHandler(fh)
logger.addHandler(sh)

logging.debug('debug message')       # 低级别的 # 排错信息
logging.info('info message')            # 正常信息
logging.warning('警告错误')      # 警告信息
logging.error('error message')          # 错误信息
logging.critical('critical message') # 高级别的 # 严重错误信息
