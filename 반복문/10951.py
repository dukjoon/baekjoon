while True:
    try:
        a, b = map(int,input().split())
        print(a + b)
    except:
        break

# 무한루프에 빠지지 않게 while 문을 쓸 떄는 try: , except: 문을 기억하자
