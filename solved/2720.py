t = int(input())
coins=[25,10,5,1]
for _ in range(t):
    change = int(input())
    change_coin = []
    for coin in coins:
        change_coin.append(change//coin)
        change -= (change//coin)*coin
    
    for i in change_coin:
        print(i,end=' ')