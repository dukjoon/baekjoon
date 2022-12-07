n = int(input())
r = '*'

for i in range(0,n):
    print(' '* i,end='')
    print(r * (n-i))