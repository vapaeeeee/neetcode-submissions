class Solution:

    def profit(self,prices,buy,sell):
        if buy < sell:
            return prices[sell] - prices[buy]
        return 0

    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,0
        maxP = 0
        left, right = 0,0
        # [80,82,50,52,60,20,25,1,2,7] 10
        # [7,1,5,3,6,4] 6
        for i in range(len(prices)):
            if prices[i] < prices[left]:
                left = i
                right = i
            if prices[i] > prices[right]:
                right = i
            profit = self.profit(prices, left, right)
            if profit > maxP:
                print(left,right)
                buy = left
                sell = right
                maxP = profit
            test_left = left
            if right > sell:
                while test_left < right:
                    test_left += 1
                    profit = self.profit(prices, test_left, right)
                    if profit > maxP:
                        left = test_left
                        buy = left
                        maxP = profit

        return maxP
