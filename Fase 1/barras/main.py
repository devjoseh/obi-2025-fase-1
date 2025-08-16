colunas = int(input())
valores = list(map(int, input().split()))
linhas = max(valores)

barras = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        if((linhas - 1 - i) < valores[j]):
            linha.append(1)
        else:
            linha.append(0)
    barras.append(linha)

for linha in barras:
    print(*linha)