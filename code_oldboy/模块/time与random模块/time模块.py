'''
作者:lg
日期:2019/10/20
文件描述:
缺陷：
'''

# 表示时间的三种方式

# 时间戳:给计算机看的
# 时间字符串: 给人看的
# 时间元组: 用作计算

# 在Python中，通常有这三种方式来表示时间：时间戳、元组(struct_time)、格式化的时间字符串：
# (1)时间戳(timestamp) ：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。

# (2)格式化的时间字符串(Format String)： ‘1999-12-06’
# 日期格式化符号
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

# (3)元组(struct_time) ：struct_time元组共有9个元素共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天等）
# 索引（Index）	属性（Attribute）	值（Values）
# 0	            tm_year（年）	    比如2011
# 1	            tm_mon（月）	        1 - 12
# 2	            tm_mday（日）	    1 - 31
# 3	            tm_hour（时）	    0 - 23
# 4	            tm_min（分）	        0 - 59
# 5	            tm_sec（秒）	        0 - 60
# 6	            tm_wday（weekday）	0 - 6（0表示周一）
# 7	            tm_yday（一年中的第几天）	1 - 366
# 8	            tm_isdst（是否是夏令时）	默认为0

import time

# 时间戳
print(time.time())  # 1571567217.2562428

# 时间字符串
print(time.strftime('%Y-%m-%d'))  # 2019-10-20

# 时间元组
print(time.localtime())
# 默认参数是当前时间戳,可以自己传入一个时间戳参数!!
# 结果 : time.struct_time(tm_year=2019, tm_mon=10, tm_mday=20, tm_hour=18, tm_min=47, tm_sec=42, tm_wday=6, tm_yday=293, tm_isdst=0)

# 时间戳-->结构化时间(时间元组)
time.gmtime()  # UTC时间，与英国伦敦当地时间一致
time.localtime()  # 当地时间。例如我们现在在北京执行这个方法：与UTC时间相差8小时，UTC时间+8小时 = 北京时间

# 结构化时间(时间元组)-->时间戳　
# time.mktime

time_tuple = time.localtime()
ret = time.mktime(time_tuple)
print(ret)  # 1571568995.0

# 结构化时间-->字符串时间
# time.strftime("格式定义","结构化时间")  结构化时间参数(第二个参数)若不传，则显示当前时间!!!!
# 第二个参数不传
print(time.strftime('%Y-%m-%d %X'))  # 2019-10-20 19:00:02
# 第二个参数传递
t_tupel = time.gmtime()
print(time.strftime('%X', t_tupel))  # 11:02:27

# 字符串时间-->结构化时间
# time.strptime(时间字符串,字符串对应格式)
print(time.strptime('2019-10-20', '%Y-%m-%d'))
# time.struct_time(tm_year=2019, tm_mon=10, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=293, tm_isdst=-1)


# 结构化时间 --> %a %b %d %H:%M:%S %Y串(时间字符串)
# time.asctime(结构化时间) 如果不传参数(默认传当前时间元组)，直接返回当前时间的格式化串
print(time.asctime())  # Sun Oct 20 19:14:12 2019
print(time.asctime(time.gmtime(1500000000)))  # Fri Jul 14 02:40:00 2017

# 时间戳 --> %a %b %d %H:%M:%S %Y串(时间字符串)
# time.ctime(时间戳)  如果不传参数，直接返回当前时间的格式化串
print(time.ctime())  # Sun Oct 20 19:17:50 2019
print(time.ctime(2000000000))  # Wed May 18 11:33:20 2033

# 计算时间差,求两个时间差了几年几月几时几分
true_time = time.mktime(time.strptime('2017-09-11 08:30:00', '%Y-%m-%d %H:%M:%S'))
time_now = time.mktime(time.strptime('2017-09-12 11:00:00', '%Y-%m-%d %H:%M:%S'))
dif_time = time_now - true_time
print(dif_time)  # 95400.0
ret = time.gmtime(dif_time)
print(ret)

# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=2, tm_hour=10, tm_min=30, tm_sec=0, tm_wday=4, tm_yday=2, tm_isdst=0)
# 时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
print(f'过去了{ret.tm_year - 1970}年{ret.tm_mon - 1}月{ret.tm_mday - 1}日{ret.tm_hour}时{ret.tm_min}分{ret.tm_sec}秒')
