L = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c != 0:
    x = a // c + 1

else:
    x = a //c

if b % d != 0:
    y = b // d + 1

else:
    y = b // d


print(L - max(x,y))