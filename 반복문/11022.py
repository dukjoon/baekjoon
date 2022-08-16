x = int(input())

for i in range(1,x+1):
    a, b = map(int,input().split())
    print("Case #"+str(i)+':',end=' ')
    print(a, end=' ')
    print('+', end=' ')
    print(b, end=' ')
    print("=", a+b)