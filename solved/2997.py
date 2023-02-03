# x = []
# x = list(map(int,input().split()))


# x.sort()

# print(x[2] + (x[1]-x[0]))

a = list(map(int, input().split()))
a.sort()
if a[1] - a[0] == a[2] - a[1]:
    print(a[2] * 2 - a[1])
elif a[1] - a[0] > a[2] - a[1]:
    print(a[1] * 2 - a[2])
else:
    print(a[1] * 2 - a[0])