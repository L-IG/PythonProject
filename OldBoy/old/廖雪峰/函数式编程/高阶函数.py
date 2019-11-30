from collections import Iterable
from collections import Iterator


def f(x):
    return x * x

m = map(f, [1, 2, 3, 4, 5, 6])
print(m)
print(isinstance(m, Iterator))
print(isinstance(m, Iterable))
list(m)


'sdsf'.encode('u')