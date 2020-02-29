"""
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
这个题目说的是，给你一个整数数组，数组中的整数表示爬对应阶楼梯的代价。你可以从第 0 阶或第 1 阶楼梯开始爬，每次可以向上爬 1 阶或 2 阶。那么请问，爬完这个楼梯的最小代价是多少？
"""
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        if not cost: return 0

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-1], dp[-2])

"""
https://algocasts.io/episodes/q6G7qZW0
Time: O(n), Space: O(n)
答案：
1.这题比较简单， dp[i] 的状态只能来自dp[i-1] dp[i-2], 所以我们只需要比较那两个状态谁比较小，把它与cost[i],相加就好了
2.由于倒数第一格和倒数第二格都可以跳到终点，所以我们最后返回 dp[-1],dp[-2]的最小值就好了

"""