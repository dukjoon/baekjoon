a = int(input())
x = []
for i in range(0,a):
    sent = str(input())
    sent_l = sent.lower()
    x.append(sent_l)

for i in range(0, a):
    print(x[i])