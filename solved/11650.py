import sys
n = int(sys.stdin.readline())
r = []
for i in range(n):
    r.append(list(map(int, sys.stdin.readline().split())))
r.sort(key=lambda x: (x[0], x[1]))
for i in r:
    print(i[0], i[1])