a, b, c, d = map(int,input().split())

r = [a,b,c,d]

x = max(a,b,c,d)
y = min(a,b,c,d)

r.remove(x)
r.remove(y)

print(abs(sum(r)-(x+y)))
