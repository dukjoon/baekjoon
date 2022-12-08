while 1:
    a = str(input())
    if a == '0':
        break
    else:
        b = a
        x = list(a)
        y = list(b)
        x.reverse()
        if x == y:
            print('yes')
        else:
            print('no')
