n, w, h, l = map(int,input().split())

result = int((w / l)) * int((h / l))

if result >= n:
    print(n)
else:
    print(result)