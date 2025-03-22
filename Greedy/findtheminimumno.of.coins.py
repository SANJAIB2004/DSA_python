def findtheminimum(amount):
    coins = [1,2,5,10,20,50,100,500,1000]
    n=9
    ans =[]
    for i in range(n-1,-1,-1):
        while amount>=coins[i]:
            amount-=coins[i]
            ans.append(coins[i])
    return len(ans)

amount = int(input())
print(findtheminimum(amount))