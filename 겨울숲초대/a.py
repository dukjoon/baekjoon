n = int(input())
x = list(map(int,input().split()))
x.sort()

if len(x) % 2 == 0:
    a = len(x) / 2
else:
    a = len(x) // 2

result = x[a] + max(x) - x[a]
if result > 1440:
    print(-1)
else:
    print(result)