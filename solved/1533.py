def count_paths(N, S, E, T, graph):
    mod = 1000003  # 나머지 연산에 사용할 수

    dp = [[0] * (T + 1) for _ in range(N + 1)]
    dp[S][0] = 1  # 시작점에서 시작점으로 도달하는 경로의 개수는 1

    for t in range(1, T + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if graph[j][i] > 0 and t >= graph[j][i]:
                    dp[i][t] += dp[j][t - graph[j][i]]
                    dp[i][t] %= mod

    return dp[E][T]


# 입력 처리
N, S, E, T = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        graph[i][j] = int(row[j - 1])

# 경로 개수 계산
result = count_paths(N, S, E, T, graph)
print(result)
