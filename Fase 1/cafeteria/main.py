vMinimo = int(input())
vMaximo = int(input())
capacidade = int(input())
dose = int(input())

encontrou = False
qntdLeiteAtual = 0
i = 1

max_doses = capacidade // dose + 1

while i <= max_doses:
    doseTotal = dose * i
    
    if doseTotal >= capacidade:
        break
        
    qntdLeiteAtual = capacidade - doseTotal
    
    if qntdLeiteAtual >= vMinimo and qntdLeiteAtual <= vMaximo:
        encontrou = True
        break
    
    i += 1

if encontrou:
    print("S")
else:
    print("N")
