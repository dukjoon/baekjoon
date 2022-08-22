a = int(input())
M = 0
Lst = []

for _ in range(a):
    L = list(map(int,input(). split())) 
    M = L.pop(0)

    a_aver = sum(L) / len(L)
    Lst = [x for x in L if x > a_aver]
    
    
    # for _ in L:
    #     if L > a_aver:
    #         x.append
        
    result = (len(Lst) / len(L)) * 100

    print('%.3f'% result+'%')