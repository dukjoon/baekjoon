lst = input()

words = 'abcdefghijklmnopqrstuvwxyz'
# words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
# 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
# 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in words:
    if i in lst:
        print(lst.index(i),end=' ')

    else:
        print("-1",end=' ')