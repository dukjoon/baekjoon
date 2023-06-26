import sys
input = sys.stdin.readline

w, n = map(int, input().split())
A = list(map(int, input().split()))
m = [False] * w
 
for i in range(n):
    for j in range(i + 1, n):
        if A[i] + A[j] < w and m[w - A[i] - A[j]]:
            print("YES")
            sys.exit(0)
    
    for j in range(i):
        if A[i] + A[j] < w:
            m[A[i] + A[j]] = True
 
print("NO")