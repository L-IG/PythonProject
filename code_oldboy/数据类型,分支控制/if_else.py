"""
作者:lg
日期:2019/8/29
文件描述:用户输入一个分数，根据分数判断用户考试成绩
缺陷：当输入字母时，会报错
"""

INPUT = input('请输入一个分数').strip()

num = int(INPUT)
if num >= 90:
    print('A')
elif 90 > num >= 80:
    print('B')
elif 80 > num >= 70:
    print('C')
elif 70 > num >= 60:
    print('D')
else:
    print('E')
