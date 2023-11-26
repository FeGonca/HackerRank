# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, k = map(str, input().split())
s = sorted(s)

for i in range(1, int(k)+1):

    for c in combinations(s, i):
        print(''.join(c))