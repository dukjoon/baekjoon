m = list(map(int,input().split()))
x = str(input())

m.sort()
a = m[0]
b = m[1]
c = m[2]

if x == "ABC":
    print(a, b, c)
elif x == "BAC":
    print(b, a, c)
elif x == "CAB":
    print(c, a, b)
elif x == "ACB":
    print(a, c, b)
elif x == "BCA":
    print(b, c, a)
elif x == "CBA":
    print(c, b, a)