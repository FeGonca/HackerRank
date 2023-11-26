if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())    
    # n = 5
    # arr = map(int, str('10 -2 3 4 6').split())
    
    pontos_ordenados = sorted(set(arr), reverse=True)
    print(pontos_ordenados[1])