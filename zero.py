n = int(input())
l=[]


for i in range(n):
    e = int(input())
    if e != 0:
        l.append(e)
    else:
        l.pop()
print(sum(l))  