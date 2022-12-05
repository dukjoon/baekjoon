a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

x = [a,b,c,d]
y = [e,f]

x.remove(min(a,b,c,d))
y.remove(min(e,f))

print(sum(x) + sum(y))