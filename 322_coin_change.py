from typing import List
class Solution_1d:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        print(f'dp init:{dp}')
        dp[0] = 0

        for i in range(len(coins)):
            c = coins[i]
            #iterate from coin amount to amount
            for j in range(c, amount+1):
                dp[j] = min(dp[j], dp[j - c] + 1)

            print(f'dp:{dp}')

        print(f'dp[amouunt]:{dp[amount]}')
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1   

class Solution:
    def coinChange(self, coins, amount):
        # assign coins the same weight as the profit
        p = coins
        w = coins
        
        n = len(coins)
        # Initialize DP table with an extra row for "zero coin" case
        V = [[0] * (amount + 1) for _ in range(n + 1)]
        #dp[0][0] = 0  # Zero coins to make amount zero

        for j in range(0, amount + 1):
            V[0][j] = 0

        print("dp init:")
        for row in dp:
            print(row)
        
        print('\n\n')

        j =0
        # Process each coin one by one
        for i in range(1, n + 1):
            for j in range(amount + 1):
                # If we exclude the coin, just carry over the value from the row above
                dp[i][j] = dp[i-1][j]
                # If we include the coin, ensure we don't go out of bounds
                if j >= coins[i-1]: # j - coins[i-1] >= 0 rearranged
                    dp[i][j] = max(dp[i-1][j], dp[i][j - coins[i-1]] + coins[i-1])
            
            print(f"dp {i}:\n")
            for row in dp:
                print(row)

        # If the amount can be formed, return the result from the last cell, else -1
        return dp[n][amount] if dp[n][amount] != float('inf') else -1


# write driver with assertions
if __name__ == "__main__":
    s = Solution()
    assert s.coinChange([1,2,5], 11) == 3, f'Error: {s.coinChange([1,2,5], 11)}'
    #assert s.coinChange([2], 3) == -1, f'Error: {s.coinChange([2], 3)}'
    #assert s.coinChange([1], 0) == 0, f'Error: {s.coinChange([1], 0)}'
    
'''
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
'''