result = []
for i in range(0,7):
    x = int(input())
    if x % 2 == 1:
        result.append(x)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))