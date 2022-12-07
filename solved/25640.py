a = str(input())
n = int(input())
result = 0
for i in range(0, n):
    x = str(input())
    if a == x:
        result += 1

print(result)