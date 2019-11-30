old_str = '男'
new_str = '女'
f_name = '员工表.txt'

f= open(file= f_name, mode= 'r+', encoding= 'utf-8')
#print(f.read())很愚蠢的写法，每次调用f.read()都会导致文件光标往后移动
f_read = f.read()

#第一种方法 ：f.seek(0)
#注意：这种方法有缺陷，如果内存内容比原文本文件少，会有覆盖不了的地方
f.seek(0)

#第二种方法：注意，从当前光标位置开始往后截断
f.seek(0)
f.truncate()
f.flush()

f_read = f_read.replace(old_str, new_str)
f.write(f_read)
f.close()


