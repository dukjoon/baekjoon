# n = int(input())
# k = []
# result = 0
# for i in range(0, n):
#     a, b, c = map(int,input().split())
#     if a == b == c:
#         result = 10000 + (1000 * a)
    
#     elif a!= b != c:
#         max(a,b,c) * 100
    
#     else:
#         if a == b:
#             r = a
#         elif b == c:
#             r = b
#         else:
#             r = c
#         result = 1000 + r * 100
#     k.append(result)

# print(max(k))

case = int(input())
answer = 0

for _ in range(case):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        answer = max(answer, 10000+a*1000)
    elif a == b:
        answer = max(answer, 1000+a*100)
    elif a == c:
        answer = max(answer, 1000+a*100)
    elif b == c:
        answer = max(answer, 1000+b*100)
    else:
        answer = max(answer, 100 * max(a,b,c))

print(answer)