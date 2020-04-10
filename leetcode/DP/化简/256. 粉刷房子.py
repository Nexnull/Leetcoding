class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = [[0] * 3 for _ in range(len(costs))]

        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

        # dp[-1]包括了 dp[-1][0,1,2],我们把它其中的最小值找出来就好了

        return min(dp[-1])

# todo
# 化简版还没有学习

"""
time: ON space:ON 
https://algocasts.io/episodes/jwmBAzW8
d[i,j] 表示粉刷0-i 号房子，并且第i号房子使用第j中颜色的最小费用

j的取值只有0/1/2 三种，分别表示红/蓝/绿三种颜色

递归的初始：
dp[0,0] = cost[0,0]
dp[0,1] = cost[0,1]
dp[0,2] = cost[0,2]

就是，当你选择第1种颜色的时候，上一个房子不能跟你选相同的颜色，你要从上面两个不同颜色中，挑一个
total cost比较小的一组， 然后再加上当前的cost
dp[i,0] = min(dp[i-1,1], dp[i-1,2]) + cost(i,0)

同理，剩下两种也是
dp[i,1] = min(dp[i-1,0], dp[i-1,2]) + cost(i,1)
dp[i,2] = min(dp[i-1,0], dp[i-1,1]) + cost(i,2)
"""