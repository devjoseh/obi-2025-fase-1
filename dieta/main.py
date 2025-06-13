## 1 proteina = 4c
## 1 gordura = 9c
## 1 carboidrato = 4c

refeicoes, limite = map(int, input().split(" "))
total = 0

for i in range(1, refeicoes + 1):
    p, g, c = map(int, input().split(" "))
    calc = (p * 4) + (g * 9) + (c * 4)
    total += calc

print(limite - total)