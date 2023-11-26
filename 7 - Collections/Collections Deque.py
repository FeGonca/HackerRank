# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

n = int(input())
d = deque()

for i in range(n):
    cmd_list = list(map(str, input()))
    if cmd_list[i] == 'append':
        d.append(cmd_list[1])
    elif cmd_list[i] == 'appendleft':
        d.appendleft(cmd_list[1])
    elif cmd_list[i] == 'clear':
        d.clear()
    elif cmd_list[i] == 'extend':
        d.extend(cmd_list[1])
    elif cmd_list[i] == 'extendleft':
        d.extendleft(cmd_list[1])
    elif cmd_list[i] == 'pop':
        d.pop()
    elif cmd_list[i] == 'popleft':
        d.popleft()
    elif cmd_list[i] == 'remove':
        d.remove(cmd_list[1])
    elif cmd_list[i] == 'reverse':
        d.reverse()
    elif cmd_list[i] == 'rotate':
        d.rotate(cmd_list[1])
        
print(*d)        