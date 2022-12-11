# n = int(input())
# x = list(map(int,input().split()))
# m = int(input())
# y = list(map(int,input().split()))

# for i in range(0,m):
#     if y[i] in x:
#         print(1)
#     else:
#         print(0)

n = int(input())
x = set(map(int,input().split()))
m = int(input())
y = list(map(int,input().split()))

for i in y:
    print(1) if i in x else print(0)