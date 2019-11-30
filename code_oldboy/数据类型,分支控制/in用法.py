'''
作者:lg
日期:2019/8/31
文件描述:输入一个广告用语，根据内容判断是否合法
缺陷：
'''

str1 = input('请输入广告语：')

if '最' in str1 or '第一' in str1 or '稀缺' in str1 or '国家级' in str1:
    print('不合法')
else:
    print('合法')

# 错误写法：
# if '最' or '第一' or '稀缺' or '国家级' in str1:
#     print("不合法")
# 无论str1是什么，该结果永远是'最'
