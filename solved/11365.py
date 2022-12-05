a = str
while 1:
    if a == 'END':
        break
    else:
        a = str(input())
        result = a[::-1]
        if a == 'END':
            break
        else:
            print(result)