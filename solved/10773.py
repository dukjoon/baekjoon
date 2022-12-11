k = int(input())
r = []

for i in range(0, k):
    x = int(input())
    if x == 0:
        r.pop()
    else:
        r.append(x)

print(sum(r))