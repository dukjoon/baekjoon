# 2 1 3 -> 풀 수 있음

a = int(input())
for _ in range(a):
    ox_list = list(input())
    score = 0
    result = 0

    for i in ox_list:
        if i == "O":
            score += 1
            result += score

        else:
            score = 0
    
    print(result)