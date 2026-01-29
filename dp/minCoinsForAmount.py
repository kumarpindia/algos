# Given a variety of coin types defining a currency system, find the 
# minimum number of coins required to express a given amount of money. 
# Assume infinite supply of coins of every type.

def minimum_coins(coins, value):
    dp = [float('inf')] * (value+1)
    dp[0] = 0
    
    for i in range(1, value+1):
        min_coins = float('inf')
        for coin in coins:
            if i >= coin: #this works too
            #if i - coin >= 0:
                min_coins = min(dp[i - coin], min_coins)
        dp[i] = min_coins + 1
    return dp[value]


print(minimum_coins([1, 3, 5], 9)) #should be 3
print(minimum_coins([22, 14, 1, 18], 889)) #should be 43