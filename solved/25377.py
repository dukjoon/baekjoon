n = int(input())
r =[]
p = []
for i in range (0,n):
    a, b = list(map(int,input().split()))
    r.append(a)
    p.append(b)

for i in range(0, n):
    if r[i] >= p[i]:
        print(-1)
    else:
        print(min(r[i],p[i]))
