# n = int(input())
# result = 0
# for i in range(0,n):
#     x = int(input())
#     for i in range(0, x):
#         a = int(input())
#         result += a
#     if result % x == 0:
#         print("YES")
#     else:
#         print("NO")

if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        student_num = int(input())
        candy = 0
        for __ in range(student_num):
            candy += int(input())

        if candy % student_num == 0:
            print("YES")
        else:
            print("NO")