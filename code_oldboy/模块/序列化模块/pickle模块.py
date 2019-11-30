'''
作者:lg
日期:2019/10/20
文件描述:
缺陷：
'''

import pickle
import time

# pickle模块提供了四个功能：dumps、dump(序列化，存）、loads（反序列化，读）、load
# （不仅可以序列化字典，列表...可以把python中任意的数据类型序列化）

dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
str_dic = pickle.dumps(dic)
print(str_dic)
# 结果:b'\x80\x03}q\x00(X\x02\x00\x00\x00k1q\x01X\x02\x00\x00\x00v1q\x02X\x02\x00\x00\x00k2q\x03X\x02\x00\x00\x00v2q\x04X\x02\x00\x00\x00k3q\x05X\x02\x00\x00\x00v3q\x06u.'
dic = pickle.loads(str_dic)
print(dic)
# 结果:{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

t1 = time.localtime(1000000000)
t2 = time.localtime(2000000000)

f = open('txtfile/pickle_file.txt', 'wb')
pickle.dump(t1, f)
pickle.dump(t2, f)
f.close()

f1 = open('txtfile/pickle_file.txt', 'rb')
dic1 = pickle.load(f1)
dic2 = pickle.load(f1)
print(
    dic1)  # time.struct_time(tm_year=2001, tm_mon=9, tm_mday=9, tm_hour=9, tm_min=46, tm_sec=40, tm_wday=6, tm_yday=252, tm_isdst=0)
print(
    dic2)  # time.struct_time(tm_year=2033, tm_mon=5, tm_mday=18, tm_hour=11, tm_min=33, tm_sec=20, tm_wday=2, tm_yday=138, tm_isdst=0)
f1.close()
