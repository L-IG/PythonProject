#第一种：每当从屏幕接受一个参数，都去完整的读一次文本文件来比较
#第二种：只读一次文本文件，存到内存里，然后再与屏幕接受的参数比较
import os

def change_per_info(*args):
    #print(args) 表示用户想要修改的参数
    #print(L_all[args[0]]) 表示文本里本来的参数
    L_all[args[0]][2] = args[1]
    L_all[args[0]][3] = args[2]
    L_all[args[0]][4] = args[3]
    new_line = ' '.join(L_all[args[0]]) + '\n'

    f_old = open('personnal_info.txt','r')
    f_new = open('personnal_info.txt.new','w')
    for line in f_old:
        if L_all[args[0]][1] in line:
            f_new.write(new_line)
        else:
            f_new.write(line)
    f_old.close()
    f_new.close()
    os.replace('personnal_info.txt.new', 'personnal_info.txt')
    print('修改成功！')

L_all = []
flag_count = 0
with open('personnal_info.txt') as f:
    for line in f:
         L_all.append(line.strip().split())

while True:
    name = input('please input name:')
    passwd = input('please input passwd:')

    for index,L_part in enumerate(L_all):
        if name == L_part[0] and passwd == L_part[1]:
            print(index,"Welcome!")
            while True:
                print('1.修改个人信息')
                print('2.打印个人信息')
                print('3.修改密码')
                choice = input('please choice the number:').strip()
                if choice.isdigit():
                    if int(choice) == 1:
                        print('1.修改age')
                        print('2.修改position')
                        print('3.修改department')
                        choice1 = input('please choice the number:').strip()
                        if choice.isdigit():
                            if int(choice) == 1:
                                age_change = input('please input age:')
                                change_per_info(index,age_change, L_part[3], L_part[4])
                            if int(choice) == 2:
                                position_change = input('please input position:')
                                change_per_info(index,L_part[2],position_change,L_part[4])
                            if int(choice) == 3:
                                department_change = input('please input :')
                                change_per_info(index,L_part[2],L_part[3],department_change)
    if flag_count == 3:
        print('you have input three wrong')
        exit()
    flag_count += 1
