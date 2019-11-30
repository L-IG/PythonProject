flag_count = 0
f_state = open('锁定状态.txt','r')
if '1' == f_state.read():
    print('已经被锁定了')
    f_state.close()
    exit()

while True:
    id_input = input('please input id:').strip()
    passwd_input = input('please input passwd:').strip()
    flag_count += 1
    with open('用户密码表.txt', 'r') as f:
        while True:
            l_info = f.readline().split()
            if [] == l_info:
                print('wrong id or passwd!')
                f.close()
                break

            id_txt = l_info[0]
            passwd_txt = l_info[1]

            if id_txt == id_input and passwd_input == passwd_txt:
                print('Welcome,', id_txt)
                exit()
    if 3 == flag_count:
        print('you have input 3 times!')
        f_lock = open('锁定状态.txt','w')
        f_lock.write('1')
        f_lock.close()
        break







