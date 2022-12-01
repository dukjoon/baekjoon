while a!=0 and b!=0:
    a, b = map(int,input().split())

    p =[]
    q =[]

    for row in range(a):
        row = list(map(int,input().split()))
        p.append(row)

    for row in range(b):
        row = list(map(int,input().split()))
        q.append(row)

    for row in range(a):
        for col in range(b):
            print(p[row][col] + q[row][col], end=' ')
        print()
