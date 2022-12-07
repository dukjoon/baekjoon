n = int(input())
a, b = map(int,input().split())

r = ((a // 2) + b)

if n <= r:
    print(n)
else:
    print(r)