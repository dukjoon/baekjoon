# n = int(input())
# result = 0
# for i in range(0,n):
#     x = int(input())
#     result += x

# if result == 0:
#     print(0)
# elif result < 0:
#     print('-')
# else:
#     print('+')

from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    li = [int(stdin.readline()) for i in range(N)]
    if sum(li) == 0:
        print("0")
    elif sum(li) > 0:
        print("+")
    else:
        print("-")