'''
作者:lg
日期:2019/10/31
文件描述:
缺陷：
'''

# 为什么要异常处理?
# 当程序发生错误时,让程序不要退出结束,而是忽略这个异常

# 使用try和except就能处理异常
# try是我们需要处理的代码
# except 后面跟一个错误类型 当代码发生错误且错误类型符合的时候 就会执行except中的代码
# except支持多分支
# 有没有一个能处理所有错误的类型 : Exception
# 有了万能的处理机制仍然需要把能预测到的问题单独处理
# 单独处理的所有内容都应该写在万能异常之前
# else : 没有异常的时候执行else中的代码
# finally : 不管代码是否异常，都会执行
# finally 应用场景:
# try里面的内容不管是执行成功还是执行失败,都需要做一些操作,比如关闭文件,关闭数据库等,此时可以把这些语句放在finally中
# finally和return相遇的时候 依然会执行
# 函数里做异常处理用,不管是否异常去做一些收尾工作

try:
    # int('a')
    # name
    [][3]
    1 / 0
    name
except ValueError:
    print('ValueError')
except SyntaxError:
    print('SyntaxError')
except NameError:
    print('NameError')
except IndexError:
    print('IndexError')

# 只有try里面的语句出现异常了,就会走到except里,不会再继续执行try后面的代码
