a = str(input())
words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(0,len(words)):
    x = a.count(words[i])
    print(x, end=" ")

