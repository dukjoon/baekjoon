a, b = map(int,input().split())
c, d = map(int,input().split())

result = []

p = (a/c + b/d)
q = (c/d + a/b)
r = (d/b + c/a)
s = (b/a + d/c)

result.append(p)
result.append(q)
result.append(r)
result.append(s)

if max(result) == p:
    print(0)
elif max(result) == q:
    print(1)
elif max(result) == r:
    print(2)
elif max(result) == s:
    print(3)

