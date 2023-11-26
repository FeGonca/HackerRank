if __name__ == '__main__':
    N = int(input())
    lista = []
    
    for i in range(N):
        cmds = list(map(str, input().split()))
                
        if cmds[0] == 'insert':
            lista.insert(int(cmds[1]), int(cmds[2]))
        elif cmds[0] == 'print':
            print(lista)
        elif cmds[0] == 'remove':
            lista.remove(int(cmds[1]))
        elif cmds[0] == 'append':
            lista.append(int(cmds[1]))
        elif cmds[0] == 'sort':
            lista.sort()
        elif cmds[0] == 'pop':
            lista.pop()
        elif cmds[0] == 'reverse':
            lista.reverse()