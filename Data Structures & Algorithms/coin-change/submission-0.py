class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min(dp[amount - coin_i]+1)
        if amount == 0:
            return 0
            
        res = [None] * (amount+1)
        res[0] = 0
        for i in range(amount + 1):
            minimum = float('inf')
            for coin in coins: 
                if i - coin < 0 or res[i-coin] == None: # no coin can fit
                    continue
                minimum = min(minimum, res[i-coin] + 1)
            if minimum != float('inf'): # found replacement
                res[i] = minimum

        for i in range(len(res)):
            print(res[i])
        return res[amount] if res[amount] != None else -1


            