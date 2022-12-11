# # n = int(input())
# # r = []
# # cnt = []
# # for i in range(0, n):
# #     x = int(input())
# #     r.append(x)
# #     k = r.count(x)
# #     cnt.append(k)

# # r.sort()
# # r_sum = sum(r)
# # r_av = (r_sum / len(r))




# # print(round(r_av,1)) #산술평균
# # print(r[len(r)//2]) #중앙값

# # print(abs(max(r) - min(r))) # 범위

# n = int(input())
# r = []
# for _ in range(n) :
# 	r.append(int(input()))

# print(round(sum(r)/n))

# r.sort()
# print(r[int((n-1)/2)])

# counts = dict()
# for i in range(1,n+1) :
# 	counts[i] = []

# maxCount = 1
# count = 1
# for j in range(1,n) :
# 	if r[j] == r[j-1] :
# 		count += 1
# 	else :
# 		counts[count].append(r[j-1])
# 		if maxCount < count : maxCount = count
# 		count = 1
# 	if j == n-1 : 
# 		counts[count].append(r[j])
# 		if maxCount < count : maxCount = count

# if n == 1 :
# 	counts[1].append(r[0])

# counts[maxCount].sort()
# if len(counts[maxCount]) == 1 :
# 	print(counts[maxCount][0])
# else :
# 	print(counts[maxCount][1])


# print(r[-1]-r[0])

import sys
from collections import Counter
n = int(sys.stdin.readline())
r = []
for _ in range(n):
    r.append(int(sys.stdin.readline()))
 
print(round(sum(r)/n))
 
r.sort()
print(r[n//2])
 
cnt_r = Counter(r).most_common()
if len(cnt_r) > 1 and cnt_r[0][1]==cnt_r[1][1]:
    print(cnt_r[1][0])
else:
    print(cnt_r[0][0])
 
# 범위 - 최댓값-최솟값
print(max(r)-min(r))
