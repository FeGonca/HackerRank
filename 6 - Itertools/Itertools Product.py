# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product
a = list(map(int, '1 2'.split()))
b = list(map(int, '3 4'.split()))

print(*product(a,b))