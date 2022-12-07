for i in range(0,3):
    x = list(map(int,input().split()))
    if x.count(1) == 0:
        print('D')  #1:등 0:배
    elif x.count(1) == 1:
        print('C')
    elif x.count(1) == 2:
        print('B')
    elif x.count(1) == 3:
        print('A')
    else:
        print('E')
