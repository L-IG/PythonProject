'''
作者:lg
日期:2020/1/4
文件描述:
缺陷：
'''

# python之使用set对列表去重，并保持列表原来顺序（转）
mylist = [5, 5, 5, 5, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
mylist_tmp = list(set(mylist))
print(mylist_tmp)  # [1, 2, 3, 4, 5]

# 不打乱顺序的方法
new_mylist = []
for i in mylist:
    if i not in new_mylist:
        new_mylist.append(i)
print(new_mylist)  # [5, 1, 2, 3, 4]

# 更简洁的方法
mylist = [5, 5, 5, 5, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
mylist_tmp = list(set(mylist))
mylist_tmp.sort(key=mylist.index)
print('mylist_tmp', mylist_tmp)  # mylist_tmp [5, 1, 2, 3, 4]
