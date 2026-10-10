class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        maxProfit = 0
        # minPrice = float('inf')
        # for price in prices:
        #     minPrice = min(minPrice, price)
        #     maxProfit = max(maxProfit, price - minPrice)
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         if buy < prices[j]:
        #             sell = prices[j]
        #             maxProfit = max(maxProfit, (sell - buy))

        # return maxProfit

        # Optimized soln
        left, right = 0, 1
        while right < len(prices):
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, (prices[right] - prices[left]))
            else:
                left = right
            right += 1
        return maxProfit
