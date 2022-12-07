# a, b = map(int,input().split())

# x = abs(b - a)

# if x // 4 == 0:
#     result = 0
# else:
#     result = x // 4

# print((result) + (x % 4))


a,b=map(int,input().split())
a-=1;b-=1
print(abs(a//4-b//4)+abs(a%4-b%4))