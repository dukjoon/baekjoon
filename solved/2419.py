n, m = map(int, input().split())  # 사탕 바구니의 개수 n, 사탕의 개수 m 입력 받기

c_box = [int(input()) for _ in range(n)]  # 사탕 바구니의 위치 입력 받기

cnt = 0  # 먹을 수 있는 사탕의 개수 초기화
time = 0  # 시간 초기화

while m > 0:  # 사탕이 남아있는 동안 반복
    for i in range(n):  # 각 사탕 바구니에 대해 반복
        if c_box[i] < 0:  # 사탕 바구니의 위치가 음수인 경우
            move = -c_box[i]  # 수아가 이동해야 할 거리 계산
            time += move  # 시간 증가
            c_box[i] += move  # 사탕 바구니 위치 조정
        if m > 0:  # 사탕이 남아있는 경우
            cnt += m  # 사탕 먹기
            m = 0  # 남은 사탕 개수 갱신
        else:  # 사탕이 모두 먹은 경우
            break

print(cnt)  # 먹을 수 있는 사탕의 최대 개수 출력
