partidas = int(input())

for i in range(partidas):
    l, a, b = map(int, input().split())
    minimo = 0
    maximo = b - a + 1
    resposta = 0

    while minimo <= maximo:
        tentativa = minimo + (maximo - minimo) // 2
        if(tentativa == 0):
            minimo = tentativa + 1
            continue
            
        termosQntd = tentativa - 1
        soma = 0

        if(termosQntd > 0):
            soma = termosQntd * (2 * a + termosQntd - 1) // 2
        
        if(soma < l):
            resposta = tentativa
            minimo = tentativa + 1
        else:
            maximo = tentativa - 1
    
    print(resposta)