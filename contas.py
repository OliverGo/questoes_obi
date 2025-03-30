valor_disponivel, farmacia, padaria, acogue = int(input()), int(input()), int(input()), int(input())
l = [farmacia, padaria, acogue]
c = 0
for i in l:
    if valor_disponivel >= i:
        c += 1
        valor_disponivel = valor_disponivel - i
print(c)






    
