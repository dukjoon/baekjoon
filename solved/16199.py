a, b, c = map(int,input().split())
x, y, z = map(int,input().split())

if b == y:
    if c > z:
        result = (x-a) - 1
    else:
        result = (x-a)

elif b < y:
    result = (x-a)

else:
    result = (x-a) -1

if result <= 0:
    result == 0

print(result)
print(x-a+1)
print(x-a)