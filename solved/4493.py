n = int(input())
for i in range(0, n):
    x = int(input())
    score_1 = 0
    score_2 = 0
    for c in range(0, x):
        a, b = map(str,input().split())
        if a == 'R' and b == 'S':
            score_1 += 1
        elif a == 'R' and b == 'P':
            score_2 += 1
        elif a == 'S' and b == 'P':
            score_1 += 1
        elif a == 'S' and b == 'R':
            score_2 += 1
        elif a == 'P' and b == 'R':
            score_1 += 1
        elif a == 'P' and b == 'S':
            score_2 += 1
        
    if int(score_1) > int(score_2):
        print("Player 1")
    elif int(score_1) < int(score_2):
        print("Player 2")
    else:
        print("TIE")