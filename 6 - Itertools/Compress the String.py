# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

# PreparePythonItertoolsCompress the String!

'''
from itertools import groupby

s = input()

groups = []
uniquekeys = []

strFinal = ''

for k, g in groupby(s):
    groups.append(list(g))
    uniquekeys.append(k)    
    
for i in range(len(uniquekeys)):
    l = len(groups[i])
    x = uniquekeys[i]
    strFinal = strFinal + (f'({l}, {x}) ')

print(strFinal)
'''


from itertools import groupby

s = '1222311'

for k, g in groupby(s):
    a = list(g)
    print(tuple([len(a), int(k)]), end = ' ')

# (1, 1) (3, 2) (1, 3) (2, 1)
