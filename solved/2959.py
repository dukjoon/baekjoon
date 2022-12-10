r = []
a, b, c, d = map(int,input().split())

r.append(a)
r.append(b)
r.append(c)
r.append(d)
r.sort()

del r[1]
del r[2]

print(int(r[0]) * int(r[1]))