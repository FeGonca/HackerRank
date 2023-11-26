# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

#  myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

x = int(input())
myList = Counter(map(int, input().split()))
n = int(input())

total = 0

for i in range(n):
    size, value = map(int, input().split())
    if myList.get(size):
        total += value
        myList[size] -= 1
        
print(total)