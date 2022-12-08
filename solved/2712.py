# n = int(input())

# for i in range(0, n):
#     a, b = map(str,input().split())
#     x = int(a)
#     y = str(b)

#     if y == 'kg':
#         x = x * 2.2046
#         print(round(x,4),'lb')
    
#     elif y == 'lb':
#         x = x * 0.4536
#         print(round(x,4),'kg')
    
#     elif y == 'l':
#         x = x * 0.2642
#         print(round(x,4),'g')
    
#     elif y == 'g':
#         x = x * 3.7854
#         print(round(x,4),'l')

for _ in range(int(input())):
    n, s = input().split()
    if s == "kg":
        print("%.4f %s" % (float(n)*2.2046, "lb"))
    elif s == "lb":
        print("%.4f %s" % (float(n)*0.4536, "kg"))
    elif s == "l":
        print("%.4f %s" % (float(n)*0.2642, "g"))
    elif s == "g":
        print("%.4f %s" % (float(n)*3.7854, "l"))