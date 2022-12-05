a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

result = 0

if a < 0:
    result = (abs(a) * c) + d + (b * e)

else:
    result = (b-a) * e

print(result)