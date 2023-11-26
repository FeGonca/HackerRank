from itertools import combinations

n = 4
s = 'a a c d'.split()
k = 2

c = combinations(''.join(s), k)

total_comb = 0
comb_certas = 0

for i in c:
    total_comb += 1
    if 'a' in i:
        comb_certas += 1

print(round(comb_certas/total_comb,3))