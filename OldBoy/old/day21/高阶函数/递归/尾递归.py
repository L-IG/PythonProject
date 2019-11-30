def add(n):
    print(n)
    if n == 900:
        return None
    return add(n + 1)
#放在return语句后面不会被执行
    print(n)
add(1)
