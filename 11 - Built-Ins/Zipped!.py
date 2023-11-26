'''
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5
'''
n, x = map(int, input().split())

# n = qtd alunos 5
# x = qtd notas 3

notas = []

# montando as listas com as notas
for a in range(x):
    notas.append(input().split(sep=' '))
    
notas_inteiros = [[float(item) for item in sublist] for sublist in notas]

a = list(zip(*notas_inteiros))

for i in range(n):
    print(sum(a[i]) / len(a[i]))