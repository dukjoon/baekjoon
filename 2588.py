a = int(input())
b = int(input())

x = b % 10 
y = int((b % 100) / 10)
z = int((b / 100))

print(a * x)
print(a * y)
print(a * z)
print(a * b)