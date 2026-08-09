class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dp = [[-1] * n for _ in range(k+1)]
        # for start, end, price in flights:
        #     if start == src:
        #         dp[0][end] = price # finding all 1 distance end point from src
        
        # for i in range(k): # we will try to connect prev endpoint to another endpoint
        #     for start, end, price in flights:
        #         if dp[i][start] != -1: # prev endpoint exist
        #             if dp[i+1][end] != -1: # have existing solution
        #                 dp[i+1][end] = min(dp[i+1][end], price + dp[i][start])
        #             else:
        #                 dp[i+1][end] = price + dp[i][start] # continue on from the prev endpoint
        
        # minimum = float('inf')
        # for w in range(k+1):
        #     if dp[w][dst] != -1:
        #         minimum = min(minimum, dp[w][dst])

        # print(dp)
        # if minimum == float('inf'):
        #     return -1

        # return minimum

        dp = [-1] * n 
        dp[src] = 0

        # iterate through k+1 times because src -> des does not count as 1     
        for _ in range(k+1): # we will try to connect prev endpoint to another endpoint
            tempPrices = dp.copy()
            for start, end, price in flights:
                if tempPrices[start] == -1: # prev endpoint does not exist
                    continue
                    
                if dp[end] != -1: # have existing solution
                        dp[end] = min(dp[end], price + dp[start])
                else:
                    dp[end] = price + dp[start] # continue on from the prev endpoint
        
        minimum = float('inf')
        if dp[dst] != -1:
            minimum = min(minimum, dp[dst])
        else:
            return -1

        return minimum