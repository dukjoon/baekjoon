# n = int(input())
# result = 1
# for i in range(0, n):
#     x = int(input())
#     result += (x - 1)

# print(result)

import sys
n = int(sys.stdin.readline())
sum = 0
for i in range(n):
    sum += int(sys.stdin.readline())
print(sum - (n - 1))