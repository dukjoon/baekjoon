a = int(input())
L = list(map(int, input().split()))

a_aver = sum(L) / a
M = max(L)

result = a_aver / M * 100
print(result)