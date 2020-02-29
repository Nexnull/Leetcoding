"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
"""

import sys
class Solution(object):
    def maxProfit(self, n, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if prices is None or len(prices) == 0 or n == 0:
            return 0
        res = 0

        # 买卖两种操作，  k次交易次数，prices天的时间流程
        profit = [[[0 for i in range(2)] for i in range(n)] for i in range(len(prices))]

        profit[0][0][0], profit[0][0][1] = 0, -prices[0]


        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            for k in range(n,0,-1):
                # 交易0次
                # 手头上没股票，正常，因为一开始就没有
                # 手头上有股票，可能是之前买的，也有可能是现在买
                if i == 1 and k == 0:
                    profit[i][k][0] = profit[i - 1][k][0]
                    profit[i][k][1] = max(profit[i - 1][k][1], profit[i - 1][k][0] - prices[i])
                if k == n-1:
                    profit[i][k][0] = max(profit[i - 1][k][0], profit[i - 1][k - 1][1] + prices[i])
                    continue

                profit[i][k][0] = max(profit[i - 1][k][0], profit[i-1][k-1][1] + prices[i])
                profit[i][k][1] = max(profit[i - 1][k][1], profit[i-1][k-1][0] - prices[i])





        end = len(prices) - 1


        return max(profit[end][n-1])


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(4,[3,2,6,5,0,9,1,5,3,8])) #22
    print(solution.maxProfit(5, [3, 2, 6, 5, 0, 9, 1, 5, 3, 8]))  # 24
    print(solution.maxProfit(1, [1,2])) #1
    print(solution.maxProfit(2, [3,2,6,5,0,3])) #7
    print(solution.maxProfit(2, [2,4,1]))  # 2

