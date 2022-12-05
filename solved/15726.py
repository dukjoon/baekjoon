# a,b,c = map(int,input().split())

# if a*b >= b*c:
#     print(int((a*b)/c))

# else:
#     print(int((a/b)*c))

A, B, C = map(int, input().split())
print(A * max(B, C) // min(B, C))
