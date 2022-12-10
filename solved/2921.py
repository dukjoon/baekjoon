n = int(input())
r = n + 2
result = 0
sum_r = 0
# (n+2) * 1 + n+2 *2 + n

for i in range(0,n+1):
    result = i * (n + 2)
    sum_r += result

print(sum_r)