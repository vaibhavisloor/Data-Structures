def greedy(coins,total):
    coins=sorted(coins,reverse=True)
    # print(coins)

    count=0
    coins_req=[]
    for coin in coins:
        while coin<=total:
            coins_req.append(coin)
            total-=coin
            count+=1
    if total !=0 :
        return "Coins dont add up to the total"        
    return count,coins_req        


coins=[20,25,10,5,15]
total=90

print(greedy(coins,total))