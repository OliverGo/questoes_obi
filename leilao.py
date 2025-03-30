numero_lances = int(input())
lista_lances = []

for i in range(numero_lances):
    lances = (input(), int(input()))
    lista_lances.append(lances)

res = list((max(lista_lances)))
for res in res:
    print(res)