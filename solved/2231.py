n = int(input())
result = 0
for i in range(1, n+1):
    r = list(map(int, str(i)))
    result = sum(r) + i
    if result == n:
        print(i)
        break
    if i == n:
        print(0)