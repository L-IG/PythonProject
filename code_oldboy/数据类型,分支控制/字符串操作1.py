'''
作者:lg
日期:2019/8/31
文件描述:字符串常见方法
缺陷：
'''

# 切记，字符串是不可变对象，任何操作对原字符串都没有影响，都是生成新的字符串了

# 1、大小写转来转去

s1 = "python"

# 第一个字母变成大写
ret1 = s1.capitalize()
print(ret1)

# ⼤⼩写的转换
ret = s1.lower()  # 全部转换成⼩写
print(ret)
ret = s1.upper()  # 全部转换成⼤写
print(ret)

# 应用于验证码
# verify_code = 'aBcDe'
# user_code = input('请输入验证码：')
# if verify_code.upper() == user_code.upper():
#     print('验证码正确')
# else:
#     print('验证码错误')

# ⼤⼩写互相转换
ret = 'PyAthON'.swapcase()
print(ret)

# 每个被特殊字符隔开的字⺟⾸字⺟⼤写(中文也算特殊字符)
s3 = "alex eggon,taibai*yinwang_麻花藤"
ret = s3.title()  # Alex Eggon,Taibai*Yinwang_麻花藤
print(ret)

# 2、切来切去
# 居中
s5 = "周杰伦"
ret = s5.center(10, "*")  # 拉⻓成10, 把原字符串放中间.其余位置补*
print(ret)

# 去空格
s7 = '  alex wusir haha  '
ret = s7.strip()  # 去掉左右两端的空格
print(ret)

ret = s7.lstrip()  # 去掉左边空格
print(ret)
ret = s7.rstrip()  # 去掉右边空格
print(ret)

s7 = "abcdefgabc"
print(s7.strip("abc"))  # defg也可以指定去掉的元素,

# 字符串替换
s8 = "sylar_alex_taibai_wusir_eggon"
ret = s8.replace('alex', '⾦⻆⼤王')  # 把alex替换成⾦⻆⼤王
print(ret)  # sylar_⾦⻆⼤王_taibai_wusir_eggon

ret = s8.replace('i', 'SB', 2)  # 把i替换成SB, 替换2个，不指定则默认全部替换
print(ret)  # sylar_alex_taSBbaSB_wusir_eggon

# 字符串切割
s9 = "alex,wusir,sylar,taibai,eggon"
lst = s9.split(",")  # 字符串切割, 根据,进⾏切割
print(lst)

s10 = """诗⼈
学者
感叹号
渣渣"""
print(s10.split("\n"))  # ⽤\n切割

s11 = "银王哈哈银王呵呵银王吼吼银王"
lst = s11.split("银王")  # ['', '哈哈', '呵呵', '吼吼', ''] 如果切割符在左右两端. 那么⼀定会出现空字符串.深坑请留意
print(lst)

# 3、格式化输出
s12 = "我叫%s, 今年%d岁了, 我喜欢%s" % ('sylar', 18, '周杰伦')  # 之前的写法
print(s12)
s12 = "我叫{}, 今年{}岁了, 我喜欢{}".format("周杰伦", 28, "周润发")  # 按位置格式化
print(s12)
s12 = "我叫{0}, 今年{2}岁了, 我喜欢{1}".format("周杰伦", "周润发", 28)  # 指定位置
print(s12)
s12 = "我叫{name}, 今年{age}岁了, 我喜欢{singer}".format(name="周杰伦", singer="周润发", age=28)  # 指定关键字
print(s12)

# 4、查找
# ***查找的方法一般都可以从字符串左右两个方向开始,还可以用start和end参数指定方法查找的范围
s13 = "我叫sylar, 我喜欢python, java, c等编程语⾔."
ret1 = s13.startswith("sylar")  # 判断是否以sylar开头
print(ret1)
ret2 = s13.startswith("我叫sylar")  # 判断是否以我叫sylar开头
print(ret2)
ret3 = s13.endswith("语⾔")  # 是否以'语⾔'结尾
print(ret3)
ret4 = s13.endswith("语⾔.")  # 是否以'语⾔.'结尾
print(ret4)
ret7 = s13.count("a")  # 查找"a"出现的次数
print(ret7)
ret5 = s13.find("sylar")  # 查找'sylar'出现的位置，默认是从左到右找，并且找到第一个就停止
print(ret5)
ret6 = s13.find("tory")  # 查找'tory'的位置, 如果没有返回-1，因为0是有索引的
print(ret6)
ret7 = s13.find("a", 8, 22)  # 切⽚找
print(ret7)
ret8 = s13.index("sylar")  # 与find功能一样，求索引位置. 注意. 如果找不到索引. 程序会报错
print(ret8)

# 5、条件判断
# 条件判断
s14 = "123.16"
s15 = "abc"
s16 = "_abc!@"
# 是否由字⺟和数字组成
print(s14.isalnum())
print(s15.isalnum())
print(s16.isalnum())
# 是否由字⺟组成
print(s14.isalpha())
print(s15.isalpha())
print(s16.isalpha())
# 是否由数字组成, 不包括⼩数点
print(s14.isdigit())

# 有一种特殊用法，校验一个用户输入的字符串是不是都是数字，然后再调用int方法，不然直接对字母调用会报错
user_input = input('请输入一个数字：')
if user_input.isdigit():
    user_num = int(user_input)

print(s14.isdecimal())
print(s14.isnumeric())  # 这个⽐较⽜B. 中⽂都识别.
print(s15.isdigit())
print(s16.isdigit())

# 练习. ⽤算法判断某⼀个字符串是否是⼩数
s17 = "-123.12"
s17 = s17.replace("-", "")  # 替换掉负号
if s17.isdigit():
    print("是整数")
else:
    if s17.count(".") == 1 and not s17.startswith(".") and not s17.endswith("."):
        print("是⼩数")
    else:
        print("不是⼩数")

#  遍历字符串
s19 = "⼤家好, 我是VUE, 前端的⼩朋友们. 你们好么?"
# 1、while循环
# 利用length方法进行遍历操作在其他编程语言比较常见
index = 0
while index < len(s19):
    print(s19[index])
    index = index + 1

# 2、for循环
for c in s19:
    print(c)

# join方法
# join参数是一个可迭代对象
s = 'abcd'.join('一二三四')
print(s)

# join可以将列表--->字符串
s = 'ddfg'.join(['啊', '是的', '是'])
print(s)

# split可以将字符串--->列表
l = s.split('ddfg')
print(l)