#!/usr/bin/python3
"""Greedy Algo """


def makeChange(coins, total):
    """Determine the fewest number of coins
    needed to meet a given amount total."""
    if total <= 0:
        return 0

    # Initialize the dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through each coin
    for coin in coins:
        # Update dp array for amounts that can be formed using current coin
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
