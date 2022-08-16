# a = int(input())

# if a < 10:
#     a = a*10

# result = 0

# while 1:
#     n = (a % 10) + (a // 10) #일의자리 + 십의자리
#     x = (n % 10) + ((a % 10) * 10)
#     result += 1

#     if (x == a):
#         break

# print(result)

n = int(input())
num = n
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    cnt = cnt + 1

    if num == n:
        break
print(cnt)