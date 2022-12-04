a, b, c, d = map(int,input().split())
x, y, z, w = map(int,input().split())

p = a + b + c + d
q = x + y + z + w

print(max(p,q))