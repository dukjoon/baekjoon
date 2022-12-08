# n = int(input())
# lst = []

# for i in range(n):
#     lst.append(input())

# lst.sort()	## 괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬을 해 준다.
# lst.sort(key = len)	## 문자열 길이 순으로 정렬.

# for i in lst:
#     print(i)


import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)