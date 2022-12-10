a, b = map(int,input().split())
x = int(input())
k = [a * (1000/b)]
for i in range(0,x):
    n, m = map(int,input().split())
    result = n * (1000 / m)
    k.append(result)

p = min(k)
print(round(p,2))