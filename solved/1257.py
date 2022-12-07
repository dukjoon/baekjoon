n = int(input())
x = list(map(int,input().split()))
result = 0
result_y = 0
result_m = 0
# p_y = (x // 30 + 1) * 10
# p_m = (x // 60 + 1) * 15

for i in range(0,n):
    result_y += (x[i] // 30 + 1) * 10
    result_m += (x[i] // 60 + 1) * 15
    result += (min(result_y,result_m))

if result_y < result_m:
    print("Y",result_y)

elif result_y > result_m:
    print("M",result_m)

else:
    print("Y","M",result_m)