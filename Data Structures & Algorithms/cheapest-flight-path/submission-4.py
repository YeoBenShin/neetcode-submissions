class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [-1] * n 
        dp[src] = 0

        # iterate through k+1 times because src -> des does not count as 1     
        for _ in range(k+1): # we will try to connect prev endpoint to another endpoint
            tempPrices = dp.copy()
            for start, end, price in flights:
                if tempPrices[start] == -1: # prev endpoint does not exist
                    continue

                if dp[end] != -1: # have existing solution
                    dp[end] = min(dp[end], price + tempPrices[start])
                else:
                    dp[end] = price + tempPrices[start] # continue on from the prev endpoint
        
        minimum = float('inf')
        if dp[dst] != -1:
            minimum = min(minimum, dp[dst])
        else:
            return -1

        return minimum