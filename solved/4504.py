n = int(input())
while 1:
    x = int(input())
    if x == 0:
        break
    
    if x % n == 0:
        print(x,end=' ')
        print("is a multiple of",end=' ')
        print(n,end='')
        print('.')
    else:
        print(x,end=' ')
        print("is NOT a multiple of",end=' ')
        print(n,end='')
        print('.')