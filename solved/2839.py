n = int(input())

box = 0
while n >= 0 :
    if n % 5 == 0 :  
        box += (n // 5)
        print(box)
        break
    n -= 3  
    box += 1 
else :
    print(-1)