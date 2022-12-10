# n = int(input())

# # s_n = 1 + (2 * (2**n - 1))
# # r = 0
# # for i in range(1, n+1):
# #     r += 1 + (2 * (2**i -1))

# # print(r**2)

# a = 3
# for i in range(0,n):
#     a = a + 2**n

# print(a)

n = int(input())
a = [4]
f = 2
b = 1
sum = 0
for i in range(1, 16):
    f += b
    sum = f ** 2
    a.append(sum)
    b = b * 2
print(a[n])