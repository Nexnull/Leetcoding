"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
(最多有两次交易,买和卖合在一起算一次交易)，这题递归就需要有三个状态了
"""
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        res = 0

        # 买卖两种操作，0，1，2三种交易次数，prices天的时间流程
        profit = [[[0 for i in range(2)] for i in range(3)] for i in range(len(prices))]

        profit[0][0][0],profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = -sys.maxsize, -sys.maxsize
        profit[0][2][0], profit[0][2][1] = -sys.maxsize, -sys.maxsize


        for i in range(1, len(prices)):
            # 交易0次
            # 手头上没股票，正常，因为一开始就没有
            # 手头上有股票，可能是之前买的，也有可能是现在买
            profit[i][0][0] = profit[i-1][0][0]
            profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0] - prices[i])

            # 交易1次
            # 手头上没股票，说明之前卖了，或者是现在卖了
            # 手头上有股票，说明之前买了，或者是现在买
            profit[i][1][0] = max(profit[i-1][1][0], profit[i-1][0][1] + prices[i])
            profit[i][1][1] = max(profit[i-1][1][1], profit[i-1][1][0] - prices[i] )

            # 交易2次
            # 手头上没股票（不可能再买了），看股票之前卖赚的多还是现在卖赚最多
            profit[i][2][0] = max(profit[i-1][2][0], profit[i-1][1][1] + prices[i])

        end = len(prices) - 1

        # 这里[end][0][0]就是陪跑的，因为你不做任何操作手中始终0块钱
        # 但是[end][1][0] 和 [end][2][0]不一定， 有时候交易多了说不定赚的少了
        # 中间都是0是因为，手上没股票了，利润才可能是最大的
        return max(profit[end][0][0], profit[end][1][0] ,  profit[end][2][0])

"""
profit[i][k][j]
这个递推有三个状态，i = 天数，  k = 之前交易了多少次,          j = 目前是持有还是不持有股票,还是已经到了买卖限制了 
                i (0-n-1)    k (0,k)k表示总交易次数的限制   j (0,1)                                   

假如说题目要求可以持有多只股票，那么j的含义可以变成目前持有多少只股票
"""