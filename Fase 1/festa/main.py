escola = int(input())
supermercado = int(input())
lojinha = int(input())

rota1 = abs(escola - supermercado) + abs(supermercado - lojinha) + abs(lojinha - escola)
rota2 = abs(escola - lojinha) + abs(lojinha - supermercado) + abs(supermercado - escola)

print(min(rota1, rota2))