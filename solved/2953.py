# r = []
# for i in range(0,5):
#     x = list(map(int,input().split()))
#     r.append(x)
#     r_max = max(r)

# print(int(r.index(r_max)+1),sum(r_max))

a = [sum(list(map(int,input().split()))) for i in range(5)]
print(a.index(max(a))+1,max(a))