x, y, w, h = map(int,input().split())
result_x = 0
result_y = 0
if x <= w-x:
    result_x = x
else:
    result_x = w-x

if y <= h-y:
    result_y = y

else:
    result_y = h-y

print(min(result_x,result_y))