n = int(input())
r = []
for i in range(0,n):
    a = list(map(int,input().split()))
    r = []
    for i in range(0,7):
        if a[i] % 2 == 0:
            r.append(a[i])
    print(sum(r), min(r))