a,b,c = map(int,input().split())

result = 0

if a==b==c:
    result= 10000 + (a*1000)

if a==b:
    result= 1000 + (a*100)

if b==c:
    result = 1000 + (b*100)

if c==a:
    result = 1000 + (c*100)

else:
    result = max(a, b, c) *100

print(result)