class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell at local maximum
        mp = 0
        idx = 0
        current_p = prices[idx]
        n = len(prices)

        while idx < n:
            if (idx+1 < n and prices[idx] >= prices[idx + 1]):
                # sell
                mp += prices[idx] - current_p
                current_p = prices[idx+1] # buy at the next price
            if (idx+1 < n and prices[idx] < prices[idx + 1]):
                # hold and check next price
                pass
            idx+=1
        mp += prices[n-1] - current_p
        return mp 
            