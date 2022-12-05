# a = str(input())

# if a[-1] == 0:
#     result = 10 + int(a[0:-2])

# else:
#     result = int(a[-1]) + int(a[0:-1])

# print(int(result))

s = input()
if s[1] == '0':
    print(10 + int(s[2:]))
else:
    print(int(s[0]) + int(s[1:]))    