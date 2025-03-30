n = int(input())
t = list(map(int, input().split()))
p = int(input())
m = int(input())

if t.count(1) == p and t.count(2) == m:
    print("S")
else:
    print("N")
