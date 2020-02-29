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
        if not prices:
            return 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit

"""
time: On space: O1
我们的交易原则是低买高卖，且当天有无数次买卖的机会
例如[1,2,3,4,5].我们从2开始遍历，发现1<2，则等于1买2卖
发现3<2，则等于2买3卖

至于别的更不特殊的情况，就更好判断了。
我们要写的主要就是用[i]-[i-1] > 0来模拟这个贪心产出结果的过程
"""