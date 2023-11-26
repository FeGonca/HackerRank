# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations

s, k = map(str, input().split())

for i in list(permutations(sorted(s),int(k))):
    print(''.join(i))