fish = int(input())
result = []
for i in range(0, fish):
    a = list(map(int,input().split()))
    if a[0] * a[1] > a[2] * a[3]:
        result.append("TelecomParisTech")
    elif a[0] * a[1] < a[2] * a[3]:
        result.append("Eurecom")
    else:
        result.append("Tie")

for i in range(0, fish):
    print(result[i])