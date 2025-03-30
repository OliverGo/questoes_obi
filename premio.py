paes, doces, b = int(input()),int(input()), int(input())
pontos = paes + (doces*2) + (b*3) 
if pontos >= 150:
    print('B')
elif pontos >= 120:
    print('D')
elif pontos >= 100:
    print('P')
elif pontos < 100:
    print('N')


