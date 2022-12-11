# x = []
# y = []
# for i in range(0,3):
#     a, b = map(int,input().split())
#     x.append(a)
#     y.append(b)
#     if x.count(a) == 2:
#         x.remove(a)
#     if y.count(b) == 2:
#         y.remove(b)

# print(x[0],y[0])

x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)