a, b, c = map(int,input().split())

if a + b + c >= 100:
    print("OK")

else:
    result = min(a, b, c)
    if a == result:
        print("Soongsil")
    elif b == result:
        print("Korea")
    else:
        print("Hanyang")