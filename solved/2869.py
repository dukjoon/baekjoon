# a, b, v = map(int,input().split())
# cnt = 0
# while 1:
#     v -= a
#     cnt += 1
#     v += b
#     if v <= 0:
#         break
# print(cnt)

# a,b,v = map(int,input().split())
# k = 0	
# d = 0
# while 1:
#     k+=1
#     if a*k-b*(k-1)>=v:
#         break
# print(k)

a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)