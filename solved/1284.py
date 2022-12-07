# while 1:
#     x = str(input())
#     my_list = list(x)
#     print(my_list)
#     print(my_list.count('1'))
#     y = len(x) + 1
#     if x == 0:
#         break
#     print(y + len(x) + my_list.count('1') + my_list.count('2') * 2 + my_list.count('0') * 3)

while 1:
    N = input()
    if N == '0':
        break
    res = len(N)+1
    for n in N:
        if n == '0':
            res += 4 
        elif n == '1':
            res += 2
        else:
            res += 3
    print(res)