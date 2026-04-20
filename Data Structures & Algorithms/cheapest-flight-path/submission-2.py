class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[-1] * n for _ in range(k+1)]
        for start, end, price in flights:
            if start == src:
                dp[0][end] = price # finding all 1 distance end point from src
        
        for i in range(k): # we will try to connect prev endpoint to another endpoint
            for start, end, price in flights:
                if dp[i][start] != -1: # prev endpoint exist
                    if dp[i+1][end] != -1: # have existing solution
                        dp[i+1][end] = min(dp[i+1][end], price + dp[i][start])
                    else:
                        dp[i+1][end] = price + dp[i][start] # continue on from the prev endpoint
        
        minimum = float('inf')
        for w in range(k+1):
            if dp[w][dst] != -1:
                minimum = min(minimum, dp[w][dst])

        print(dp)
        if minimum == float('inf'):
            return -1

        return minimum