a = int(input())
x = []
for i in range(0,a):
    sent = input()
    x.append(sent)

for i in range(0,a):
    print(i+1,end='')
    print(".",x[i])