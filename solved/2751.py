# n = int(input())
# r = []
# for i in range(n):
#     x = int(input())
#     r.append(x)

# r.sort()

# for i in range(0,n):
#     print(r[i])

import sys

n = int(input())
r = []
for i in range(0,n):
    r.append(int(sys.stdin.readline()))

r.sort()
for i in range(0,n):
    print(r[i])