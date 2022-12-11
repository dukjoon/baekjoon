n = int(input())
r = []
for i in range(n):
    a, b = map(str,input().split())
    a = int(a)
    k = (a, b)
    r.append(k)
r.sort(key = lambda x : x[0])
for i in r:
    print(i[0], i[1])