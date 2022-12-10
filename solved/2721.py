# t = int(input())
# p = []
# for i in range(0, t):
#     n = int(input())
#     for i in range(0,n):
#         k = int(((i+1)*(i+2))/2 * i)
#         p.append(k)
#         print(p)

for _ in range(int(input())):
    n = int(input())
    res = sum(k*sum(range(k+2)) for k in range(1, n+1))
    print(res)
