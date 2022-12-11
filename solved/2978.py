n = int(input())
numbers = map(int, input().split())
s = 0
for num in numbers:
    result = 0
    if num > 1 :
        for i in range(2, num):  
            if num % i == 0:
                result += 1  
        if result == 0:
            s += 1  
print(s)