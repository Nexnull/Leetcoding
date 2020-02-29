"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
Note: You may not engage in multiple transactions(交易) at the same time （当天可以有无数次买卖）
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        res = 0

        profit = [[0 for i in range(2)] for i in range(len(prices))]

        profit[0][0] , profit[0][1] = 0 , -prices[0]

        for i in range(1, len(prices)):
            # 这里和上一题不同，我们可以无限次买卖股票，所以我们不需要0-1-2不可逆反的转换来决定
            # 只能交易一次，而是0-1可以无限循环来看是否能取到最大的利润
            # 无股票状态，利润最大化是在，上一步无股票状态的利润最大化，假如说上一次持有股票且在这一步卖掉股票的利润，选一个
            profit[i][0] = max(profit[i-1][0], profit[i-1][1] + prices[i])
            # 有股票状态，利润最大化是在，继续持有上次买的股票，还是新买入股票
            profit[i][1] = max(profit[i-1][1] , profit[i-1][0] - prices[i])
            res = max(res, profit[i][0] ,profit[i][1] )

        return res