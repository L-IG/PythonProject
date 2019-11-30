f_txt = open('余额.txt','r')

while f_txt.read().strip().isdigit():
    print(int(f_txt.read().strip()))
    print(int(f_txt.read().strip()))