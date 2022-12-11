# import sys

# n = int(sys.stdin.readline())
# r = []
# r = [sys.stdin.readline().strip() for i in range(n)]
# r.sort()

# for i in range(0,n):
#     print(r[i])

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)