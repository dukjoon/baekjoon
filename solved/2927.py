import sys

# 섬의 수 N 입력 받기
N = int(input())

# 각 섬에 있는 펭귄의 수 입력 받기
penguins = list(map(int, input().split()))

# 명령의 개수 Q 입력 받기
Q = int(input())

# 섬과 다리 정보를 저장할 리스트 생성
islands = [[] for _ in range(N + 1)]
bridges = set()

# 다리 건설 함수 정의
def build_bridge(a, b):
    if (a, b) in bridges or (b, a) in bridges:
        return "no"
    else:
        bridges.add((a, b))
        return "yes"

# 섬 간 이동 가능 여부 확인 함수 정의
def can_excursion(a, b):
    visited = [False] * (N + 1)
    queue = [a]
    visited[a] = True
    total_penguins = penguins[a-1]
    
    while queue:
        current_island = queue.pop(0)
        
        for neighbor in islands[current_island]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                total_penguins += penguins[neighbor-1]
        
        if current_island == b:
            return total_penguins
    
    return "impossible"

# Q개의 명령 수행
for _ in range(Q):
    command = input().split()
    
    if command[0] == "bridge":
        a, b = map(int, command[1:])
        print(build_bridge(a, b))
    
    elif command[0] == "penguins":
        a, x = map(int, command[1:])
        penguins[a-1] = x
    
    elif command[0] == "excursion":
        a, b = map(int, command[1:])
        print(can_excursion(a, b))
