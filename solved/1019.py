def count_digits(N):
    counts = [0] * 10  # 0부터 9까지의 숫자의 등장 횟수를 저장할 리스트

    for i in range(1, N + 1):
        num = str(i)  # 숫자를 문자열로 변환하여 자릿수를 계산

        for digit in num:
            counts[int(digit)] += 1

    return counts


N = int(input())
result = count_digits(N)
print(' '.join(map(str, result)))

# 상기 코드는 시간적으로 비효율적



import sys

# ans = 1부터 9까지 각가 몇번 등장했는지 세주는 배열
ans = [0] * 10

# 입력
end = int(sys.stdin.readline())

# 위 글에서 k의 역할을 하는 point
point = 1
# 문제의 조건에 따라 1부터 시작
start = 1

# calc : a,b가 9또는 0으로 끝나지 않을 때 각 자리수를 ans에 카운트 시키는 함수
def cal(x,ans,point):
    while x > 0:
        ans[x % 10] += point
        x //= 10
        

while start <= end:
    while end % 10 != 9:
        cal(end, ans, point)
        end -= 1
    if end < start:
        break
    while start % 10 != 0:
        cal(start, ans, point)
        start += 1
    start //= 10
    end //= 10
    for i in range(10):
        ans[i] += (end - start + 1) * point
    point *= 10

# 출력부
for i in range(10):
    print(ans[i], end= ' ')