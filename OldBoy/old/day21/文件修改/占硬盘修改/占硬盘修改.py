import os
old_str = '男'
new_str = '女'
f_old_name = '员工表.txt'
f_new_name = '%s.new' % f_old_name

f_old = open(file= f_old_name, mode= 'r+', encoding= 'utf-8')
f_new = open(file= f_new_name, mode= 'w', encoding= 'utf-8')

for line in f_old:
    if old_str in line:
        line = line.replace(old_str, new_str)
    else:
        pass
    f_new.write(line)

f_old.close()
f_new.close()

os.replace(f_new_name, f_old_name)

#os.rename(f_new_name, f_old_name) 文件已经存在则修改不了
#if os.path.isfile(f_old_name) 判断当前目录文件名是否存在


#os.remove(f_old_name)
#os.rename(f_new_name,f_old_name)



