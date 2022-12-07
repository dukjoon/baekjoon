a, b = map(int,input().split())
x, y = map(int,input().split())
p, q = map(int,input().split())
m, n = map(int,input().split())

s_1 = b-x+y
s_2 = s_1 - p + q
r = max(s_1,s_2)

print(max(r,b))
