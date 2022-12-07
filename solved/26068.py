n = int(input())
result = 0
for i in range(0, n):
    x = str(input())
    if int(x[2:]) <= 90:
        result += 1

print(result)
