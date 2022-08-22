# a = int(input())

# L = list(input().split() for _ in range(a))

# print(L[0][1] * int(L[0][0]))


t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)