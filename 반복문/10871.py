n,x = map(int,input().split())
num = list(map(int,input().split()))

for i in range(n):
    if num[i] < x:
        print(num[i], end=' ')

# 대소비교를 할때 map(int,input().split()) 만 사용하면 크기비교가 불가함.