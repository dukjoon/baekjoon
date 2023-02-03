n = int(input())
for i in range(n):
    a, b, c = map(int,input().split())
    x = (c // a) + 1
    y = (c % a)
    print(y,0,x, sep='')
     