# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

students = int(input())
colunas = namedtuple('colunas', input())
total = 0

for i in range(students):
    col = colunas(* input().split())
    total += int(col.MARKS)

    
print(total/students)