'''
LEETCODE = 322
Given a list of coins and an amount, return the minimum number of coins needed to make that amount.
'''

def coinchange(coins,amount):
    if amount == 0:
        return 0
    coins.sort()
    dp = [0]*(amount+1)

    for i in range(1,amount+1):
        mini = float('inf')
        for c in coins:
            diff = i-c
            if diff <0:
                break
            mini = min(mini, dp[diff] + 1)
        dp[i] = mini

    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    coins = list(map(int, input("Enter the coins: ").split()))
    amount = int(input("Enter the amount: "))
    result = coinchange(coins, amount)
    print(f"Minimum number of coins needed: {result}")
