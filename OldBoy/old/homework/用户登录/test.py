#现象：不停地打印的文件的第一行内容
#原因分析：因为每次循环都重新打开了文件，所以读取的都是第一行内容
#解决方法：更换while的位置，只循环readline


# while True:
#     with open('用户密码表.txt', 'r') as f:
#         (id, passwd) = f.readline().split()
#         print(id, passwd)


#'break' outside loop
# with open('用户密码表.txt', 'r') as f:
# #     l_info = f.readline().split()
# #     if [] == l_info:
# #         break
# #     print(l_info)


with open('用户密码表.txt', 'r') as f:
    while True:
        l_info = f.readline().split()
        if [] == l_info:
            break
        print(l_info)


