prices1 = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) is 1:
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

testRun = Solution()
print(testRun.maxProfit(prices1))