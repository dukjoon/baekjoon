# 1부터 시작해서 6의 배수로 증가하는 숫자

n = int(input())
cnt = 1
cnt_six = 6
count = 1

while n > cnt:
    count += 1
    cnt += cnt_six
    cnt_six += 6

print(count)
