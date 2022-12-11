# n = int(input())
# for i in range(0,n):
#     x = int(input())
#     k = format(x,'#b')
#     result = k[2:]
#     r = str(result)
#     print(result)
#     m = r.index('1')
#     print(m)

T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end = " ")