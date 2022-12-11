x = []
while 1:
    x = list(map(int,input().split()))
    x.sort()
    a = x[0]
    b = x[1]
    c = x[2]
    if a == 0 and b == 0 and c == 0:
        break
    elif c**2 == (a**2 + b**2):
        print("right")
    else:
        print("wrong")
    