estoque, qntdTipos = map(int, input().split(" "))
tipos = list(map(int, input().split(" ")))
precos = list(map(int, input().split(" ")))
clientes = int(input())
pedidos = list(map(int, input().split(" ")))
lucro = 0

estoqueTipo = [[] for _ in range(qntdTipos + 1)]

for i in range(estoque):
    tipoObj = tipos[i]
    precoObj = precos[i]
    estoqueTipo[tipoObj].append(precoObj)

for t in range(1, qntdTipos + 1):
    estoqueTipo[t].sort(reverse=True)

for ped in pedidos:
    if ped == 0:
        melhorPreco = float('inf')
        melhorTipo = -1

        for i in range(1, qntdTipos + 1):
            if(estoqueTipo[i]):
                precoAtual = estoqueTipo[i][-1]
                if(precoAtual < melhorPreco):
                    melhorPreco = precoAtual
                    melhorTipo = i
        
        if(melhorTipo != -1):
            precoVendido = estoqueTipo[melhorTipo].pop()
            lucro += precoVendido
    else:
        if(1 <= ped <= qntdTipos and estoqueTipo[ped]):
            precoVendido = estoqueTipo[ped].pop()
            lucro += precoVendido

print(lucro)