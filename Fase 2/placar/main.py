golsPaulo = list(map(int, input().split(" ")))
golsCamila = list(map(int, input().split(" ")))
placar = []
hash = [(0, "A")]
pontuacaoPaulo = 0
pontuacaoCamila = 0

if(golsPaulo[0] == 0 and golsCamila[0] == 0):
    print("0 0")
else:
    j = 0
    for i in range(1, len(golsPaulo)):
        hash.append((golsPaulo[i], "P"))
        j+=1
    
    for i in range(1, len(golsCamila)):
        hash.append((golsCamila[i], "C"))
        j+=1

    hashCronologico = sorted(hash)
    placar.append(f"{pontuacaoPaulo} {pontuacaoCamila}")

    for i in range(1, len(hash)):
        if(hashCronologico[i][1] == "P"):
            pontuacaoPaulo+=1
            placar.append(f"{pontuacaoPaulo} {pontuacaoCamila}")
        else:
            pontuacaoCamila+=1
            placar.append(f"{pontuacaoPaulo} {pontuacaoCamila}")
    
    for i in range(len(placar)):
        print(placar[i])